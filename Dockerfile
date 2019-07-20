FROM python:2.7-slim
RUN apt update
WORKDIR /app
RUN pip install futures
ADD requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
ADD . /app
ENV SERVE_PORT 8080
CMD ["gunicorn", "app:app", "--config=configuration.py"]
