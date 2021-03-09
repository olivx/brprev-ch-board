FROM python:3.7.3-slim-stretch
WORKDIR /app

RUN apt-get update && apt-get install git -y

COPY Pipfile* /app/

RUN pip install --upgrade pip && \
    pip install pipenv && \
    pipenv install --system --deploy

RUN groupadd -g 999 appuser && \
    useradd -r -u 999 -g appuser appuser

COPY . /app

RUN chown appuser /app

USER appuser

ENTRYPOINT ["python", "-m", "boardgame.main"]
