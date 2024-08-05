FROM python:3-slim as base

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

ADD task.py /

RUN pip install psycopg2-binary

CMD ["python", "./task.py"]