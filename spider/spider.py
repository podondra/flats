import psycopg
import scrapy


N = 500


class FlatsSpider(scrapy.Spider):
    name = "flats"
    # there is an API, so why not to use it (see Malach, 2021)
    # flat: category_main_cb=1
    # sell: category_type_cb=1
    start_urls = [f"https://www.sreality.cz/api/cs/v2/estates?category_main_cb=1&category_type_cb=1&per_page={N}"]

    def parse(self, response):
        with psycopg.connect("host=db dbname=postgres user=postgres password=flats port=5432") as conn:
            with conn.cursor() as cur:
                dictionary = response.json()
                flats = dictionary["_embedded"]["estates"]
                for flat in flats:
                    name = flat["name"]
                    locality = flat["locality"]
                    image_url = flat["_links"]["images"][0]["href"]
                    cur.execute(f"""
                        INSERT INTO flats (name, locality, image_url)
                        VALUES ('{name}', '{locality}', '{image_url}')""")
                conn.commit()
