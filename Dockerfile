FROM tiangolo/meinheld-gunicorn-flask:python3.7-alpine3.8

RUN python -m pip install --upgrade pip
RUN python -m pip install pipenv

COPY Pipfile Pipfile
RUN pipenv lock -r > requirements.txt
RUN pip install -r requirements.txt

COPY ./app /app
