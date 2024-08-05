ARG PYTHON_VERSION=3.12.4
FROM python:${PYTHON_VERSION}-slim as base

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN python -m pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "app.py"]
