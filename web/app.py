import flask
import psycopg


app = flask.Flask(__name__)


@app.route('/')
def flats():
    with psycopg.connect("host=db dbname=postgres user=postgres password=flats port=5432") as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT name, locality, image_url FROM flats")
            items = list(cur)
    return flask.render_template("flats.html", items=items)
