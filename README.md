# Instructions
By following these instructions, you will be able:
- modify the kata,
- modify the tests run against the kata's code,
- run the tests,

on any platform (Windows, MacOS, Linux).

## Pre-requisites
1. Download and install docker engine by following these [instructions](https://docs.docker.com/install/).
2. Download and install docker compose by following these [instructions](https://docs.docker.com/compose/install/).

## Run the tests
1. Build and start the container in detached mode: `docker-compose up -d`
2. Run static code analysis with [Python hints](https://docs.python.org/3/library/typing.html) and [mypy](http://mypy-lang.org/): `docker-compose exec tennis-kata mypy .`
3. Run the unit tests: `docker-compose exec tennis-kata python3 -m unittest tennis_test.py`

## When you're done with testing
Stop the container, remove it and its associated volume and image: `docker-compose down`