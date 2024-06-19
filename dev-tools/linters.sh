#!/bin/bash -e

IMAGE_NAME="{{ cookiecutter.project_name }}"
IMAGE_TAG=${DOCKER_IMAGE_TAG:-'dev'}
PROJECT_PATH="$(pwd)"
USE_DOCKER=0

for arg in "$@"
do
  case $arg in
    --docker)
    USE_DOCKER=1
    shift
    ;;
  esac
done

if [ $USE_DOCKER -eq 1 ]; then
  echo "Running linters in Docker container..."

  echo "Checking Flake8..."
  docker run --rm -v "${PROJECT_PATH}:/code" --entrypoint /code/docker_entrypoint_local.sh  "${IMAGE_NAME}:${IMAGE_TAG}" flake8 /code

  echo "Checking Black..."
  docker run --rm -v "${PROJECT_PATH}:/code" --entrypoint /code/docker_entrypoint_local.sh "${IMAGE_NAME}:${IMAGE_TAG}" black --check --diff --color /code

  echo "Checking PyDocStyle..."
  docker run --rm -v "${PROJECT_PATH}:/code" --entrypoint /code/docker_entrypoint_local.sh "${IMAGE_NAME}:${IMAGE_TAG}" pydocstyle /code

  echo "Checking MyPY..."
  docker run --rm -v "${PROJECT_PATH}:/code" --entrypoint /code/docker_entrypoint_local.sh "${IMAGE_NAME}:${IMAGE_TAG}" mypy --ignore-missing-imports /code

else
  echo "Running linters on local machine..."

  export PYTHONPATH="${PROJECT_PATH}"

  echo "Checking Flake8..."
  flake8 "${PROJECT_PATH}"

  echo "Checking Black..."
  black --check --diff --color "${PROJECT_PATH}"

  echo "Checking PyDocStyle..."
  pydocstyle "${PROJECT_PATH}"

  echo "Checking MyPY..."
  mypy --ignore-missing-imports "${PROJECT_PATH}"
fi