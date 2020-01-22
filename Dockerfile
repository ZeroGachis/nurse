FROM python:3.7-stretch

RUN \
    apt-get -y update \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip==20.0.1 \
    && pip3 install -U setuptools

RUN pip install poetry

COPY poetry.lock /home/src/nurse/poetry.lock
COPY pyproject.toml /home/src/nurse/pyproject.toml

WORKDIR /home/src/nurse

ARG REQUIREMENTS=common
ENV REQUIREMENTS $REQUIREMENTS
RUN mkdir requirements
RUN poetry export -f requirements.txt --without-hashes > requirements/$REQUIREMENTS.txt
RUN poetry export -f requirements.txt --without-hashes --dev > requirements/dev.txt

RUN pip3 install -r requirements/$REQUIREMENTS.txt

COPY . /home/src/nurse
CMD ["bash"]