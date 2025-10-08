import tmdbsimple as tmdb
import os
from loguru import logger


def main():
    tmdb.API_KEY = os.getenv("TMDB_API_KEY")
    logger.info("TMDB API Key set.")

    movie = tmdb.Movies(550)  # Example movie ID for "Fight Club"
    response = movie.info()
    logger.info(f"Movie Title: {response['title']}")
    logger.info(f"Release Date: {response['release_date']}")

    # recursive pagination example
    max_pages = 5
    page = 1
    while page <= max_pages:
        logger.info(f"Fetching page {page} of top rated movies...")
        top_rated = tmdb.Movies().top_rated(page=page)
        if not top_rated["results"]:
            break
        for movie in top_rated["results"]:
            logger.info(
                f"Top Rated Movie: {movie['title']} - Rating: {movie['vote_average']}"
            )
        page += 1


if __name__ == "__main__":
    main()
