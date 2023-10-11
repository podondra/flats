FROM python:3.10
WORKDIR /code
COPY . .
RUN pip install flask psycopg
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
CMD ["flask", "run"]
