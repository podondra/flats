Use scrapy framework to scrape the first 500 items (title, image url) from sreality.cz (flats, sell)
and save it in the PostgreSQL database.
Implement a simple HTTP server in Python
and show these 500 items on a simple page (title and image)
and put everything to single docker compose command
so that I can just run "docker-compose up" in the GitHub repository
and see the scraped ads on http://127.0.0.1:8080 page.

    $ docker compose up
