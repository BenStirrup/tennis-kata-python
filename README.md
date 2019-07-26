# Instructions
By following these instructions, you will be able:
- modify the kata,
- modify the tests run against the kata's code,
- run the tests,

on any platform (Windows, MacOS, Linux).

## Tennis rules supported
- Traditional tennis display scores: 0, 15, 30, 40, DEUCE, ADVANTAGE, WIN
- Deuce rule: if both players reach 40 in a game, the deuce mode is activated.
  - If the score is DEUCE, the player who wins the points takes the ADVANTAGE
  - If the player who has the ADVANTAGE win the point, they win the game
  - If the player who has the ADVANTAGE lose the point, the score is DEUCE again
- A player wins the Set when they win 6 games or when they win 7 games if the opponent had won 5 games previously

## Pre-requisites
1. Download and install docker engine by following these [instructions](https://docs.docker.com/install/).
2. Download and install docker compose by following these [instructions](https://docs.docker.com/compose/install/).

## Run the tests
1. Build and start the container in detached mode: `docker-compose up -d`
2. Run static code analysis with [Python hints](https://docs.python.org/3/library/typing.html) and [mypy](http://mypy-lang.org/): `docker-compose exec tennis-kata mypy .`
3. Run the unit tests: `docker-compose exec tennis-kata python3 -m unittest tennis_test.py`

## When you're done with testing
Stop the container, remove it and its associated volume and image: `docker-compose down`