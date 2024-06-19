FROM python:3.10

WORKDIR /app

COPY requirements.txt requirements-dev.txt .

RUN pip install --no-cache-dir -r requirements.txt

ARG INSTALL_DEV_DEPENDENCIES=false

RUN if [ "$INSTALL_DEV_DEPENDENCIES" = "true" ] ; then pip install --no-cache-dir -r requirements-dev.txt ; fi

COPY . .
CMD ["uvicorn", "manage:app", "--host","0.0.0.0", "--port","8000"]
