FROM docker.arvancloud.ir/python:3.11
RUN apt-get update

ENV PYTHONUNBUFFERED=1
WORKDIR /app
ENV PYTHONPATH=/app

COPY requirements-linux.txt .

RUN pip install -r requirements-linux.txt

CMD ["python", "__main__.py"]
