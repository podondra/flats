FROM python:3.10
WORKDIR /code
COPY . .
RUN pip install scrapy psycopg
CMD ["scrapy", "runspider", "spider.py"]
