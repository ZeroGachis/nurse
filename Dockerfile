FROM 007065811408.dkr.ecr.eu-west-3.amazonaws.com/python-3-12-alpine-slim:1

WORKDIR /app

RUN apk add --no-cache git=2.49.0-r0

COPY pyproject.toml poetry.lock poetry.toml ./

RUN POETRY_NO_INTERACTION=1 poetry install

COPY . .

CMD ["bash"]
