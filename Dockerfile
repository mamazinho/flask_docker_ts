FROM python:3.8.5

LABEL maintainer="Matheus <matheus.tessaroli@olist.com>"
LABEL version="1.0.0"

WORKDIR /var/www
ENV PORT=80

EXPOSE $PORT
COPY poetry.lock pyproject.toml ./

RUN pip install poetry 
RUN poetry config virtualenvs.create false
RUN poetry install

COPY . .

ENTRYPOINT python -m flask run --host=0.0.0.0 --port=$PORT --reload