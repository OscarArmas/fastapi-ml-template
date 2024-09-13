



# fastapi-ml-template 🚀

A repository demonstrating how to build a robust service for deploying machine learning models using FastAPI. This example includes several best practices, such as:


- **Hexagonal Architecture**: Implementing a flexible, maintainable structure for the application.
- **Code Style**: Enforcing clean, readable, and professional code standards.
- **Dependency Injection**: Promoting modularity and testability of components.
- **Linting and Testing**: Ensuring code quality and reliability through automated checks.
- **Cache Memory**: Utilizing caching to enhance performance and reduce latency.
- **Docker Containerization**: Simplifying deployment and environment consistency.

Introduction
--------

This project develops a system for anomaly detection. It encompasses all stages of the model lifecycle, from exploratory data analysis (EDA) and model development to the deployment of an inference API. This system is designed for deployment in a real-time API environment, ensuring scalability for large-scale applications. The README.md file describes main components of this project.

Requirements to run this project:
1. A Linux-like OS.
2. Docker.
3. Python 3.10


-------------
#### Analysis and Model Development
In essence, we analyze the time series for each item and calculate its 1% and 99% quantiles. If new prices arrive, we assume that a price falling below the 1% quantile or above the 99% quantile is considered an anomaly.

All the EDA can be review on folder `notebooks/`

-------------

#### Inference Job

We need three services:

* Redis
* MongoDB
* API

We can execute this three services via docker-compose:

```
docker-compose -f docker-local.yml up --build
```

and just try the next Curl:

```
curl -X 'POST' \
  'http://127.0.0.1:8000/api/v1/anomaly-detection/item_price' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "item_id": "MLB1073354076",
  "price": 15
}'
```
For ingest new data use this:

```
curl -X 'POST' "http://127.0.0.1:8000/api/v1/load/item_stats" \
     -H "Content-Type: application/json" \
     -d '{
           "items": [
             {
               "_id": "MLB1073354076",
               "historical_prices": [15.62, 113.6, 134.9, 157.62, 166.14, 191.7, 244.95, 269.8, 281.16, 357.84, 374.88, 378.43, 397.6, 426.0, 461.5, 480.67, 497.0, 531.08, 533.21, 558.77, 606.34, 623.38, 795.2, 836.38, 891.76, 898.86, 979.8, 989.74, 1033.76, 1073.52, 1086.3, 1097.66, 1378.82, 1390.18, 1469.7, 1519.4, 1571.94, 2061.84, 2201.0, 2861.3, 4173.38],
               "lower_bound": 54.812,
               "upper_bound": 3648.548000000002,
               "metadata": {}
             },
             {
               "_id": "MLB1073354077",
               "historical_prices": [10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0],
               "lower_bound": 5.0,
               "upper_bound": 105.0,
               "metadata": {}
             }
           ]
         }'
```

If you want to Debug locally:

* [1] create a conda environmet with:
```
sh dev-tools/build.sh conda-env
```

* [2] start just Redis and MongoDB services:
```
docker-compose -f docker-local.yml up mongo redis --build
```
for deleting the images and volumes use:

```
docker-compose -f docker-local.yml down --rmi all --volumes
```

Directory structure
--------
The directory structure looks like this:

```
├── Makefile                <- Makefile with commands like `make check-codestyle` or `make test`
├── README.md               <- The top-level README for developers using this project.
├── Dockerfile              <- Dockerfile to run API on container.
├── docker-local.yml        <- Configuration file for setting up local Docker services.
├── application
│   ├── main                
│   │    ├── domain         <- Business logic and data access layer.
│   │    ├── infrastructure <- Infrastructure setup including databases.
│   │    ├── routers        <- Routing the requests to the appropriate services.
│   │    ├── services       <- Business logic layer for handling the application's operations.
│   │    ├── config.py      
│   │    ├── container.py   <- Dependency injection container setup.
│
├── models                  <- Directory for storing trained model artifacts (DEPRECATED)
├── notebooks               <- Jupyter notebooks for exploratory data analysis (EDA).
├── dev-tools               <- Scripts and utilities to support development activities.
├── data                    <- Directory for data used by the application.
│   ├── bulk_data.sh        <- Script to bulk load data into MongoDB.
```

API Docs
--------

```
http://127.0.0.1:8080/docs
```

Linting
--------

```
make lint
```

Style
--------

```
make codestyle
```

TODOs:
--------

In this section, I list some missing components to be implemented further.

1. Write unit tests.
2. Write docstrings.
3. Test other solutions using ML models.
4. Define a ground truth label to measure performance on diff solutions.




How to scale this API::
--------
![Scalable Infrastructure](https://github.com/OscarArmas/meli-challenge/blob/master/images/scalabre_infra.png)
