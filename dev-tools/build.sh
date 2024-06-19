#!/bin/bash -e
PROJECT_NAME=meli_challenge
IMAGE_NAME=${IMAGE_NAME:-"meli_challenge_ms"}
IMAGE_TAG=${DOCKER_IMAGE_TAG:-'dev'}
# Variables for directory structure.
REPO_ROOT_DIR="$(git rev-parse --show-toplevel)"

# parse arguments.
cmd=$1
shift

case ${cmd} in
    h | help)
        print_usage
        ;;

    b | build)
        # build Docker image.
        echo "Build Docker image: ${IMAGE_NAME}:${IMAGE_TAG}"
        docker build -t "${IMAGE_NAME}:${IMAGE_TAG}" --build-arg INSTALL_DEV_DEPENDENCIES=true -f "${REPO_ROOT_DIR}"/Dockerfile "${REPO_ROOT_DIR}"
        ;;

    l | linters)
        echo "Run linters"
        ${REPO_ROOT_DIR}/tools/linters.sh
        ;;
    
    t | tests)
        if [[ -z "${TARGET_COV}" ]]; then
            pytest --cov=./ ./tests
        else
            pytest --cov=./ ./tests  --cov-fail-under=${TARGET_COV}
        fi
        ;;

    f | format)
        echo "Format the code"
        pyupgrade --exit-zero-even-if-changed --py310-plus **/*.py
        isort --settings-path pyproject.toml ./
        black --config pyproject.toml ./
        ;;

    v | conda-env)
        # create a conda environment with the requirements of this project.
        source ${CONDA_PREFIX}/etc/profile.d/conda.sh
        conda create -fqy --name ${PROJECT_NAME} python=3.10
        conda activate ${PROJECT_NAME}
        conda install pip
        pip install -r ${REPO_ROOT_DIR}/requirements-dev.txt
        pip install -r ${REPO_ROOT_DIR}/requirements.txt
        ;;

    *)
        echo "Bad command. Options are:"
        grep -E "^    . \| .*\)$" $0
    ;;

esac

print_usage() {
    echo "Options:"
    echo "h | help: Display this help message."
    echo "b | build: Build Docker image."
    echo "l | linters: Run the linters."
    echo "t | tests: Run the tests. If TARGET_COV is set, run tests with coverage and fail if coverage is under TARGET_COV."
    echo "v | conda-env: Create a conda environment with the requirements of this project, and activate it."
}