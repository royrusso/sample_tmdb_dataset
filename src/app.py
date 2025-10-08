import tmdbsimple as tmdb
import os
import json
from loguru import logger


def main():
    tmdb.API_KEY = os.getenv("TMDB_API_KEY")
    logger.info("TMDB API Key set.")

    try:
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        data_dir = os.path.join(project_root, "data")
        os.makedirs(data_dir, exist_ok=True)
        logger.info(f"Data directory created or already exists at {data_dir}.")

        # recursive fetching of top rated movies
        num_results = int(os.getenv("NUM_RESULTS", 100))
        max_pages = (num_results // 20) + 1  # TMDB returns 20 results per page
        page = 1
        while page < max_pages:
            logger.info(f"Fetching page {page} of top rated movies...")
            top_rated = tmdb.Movies().top_rated(page=page)
            if not top_rated["results"]:
                break
            for movie in top_rated["results"]:
                logger.info(
                    f"Top Rated Movie: {movie['title']} - Rating: {movie['vote_average']}"
                )

                # write each movie JSON object to a separate file under /data in project root
                with open(os.path.join(data_dir, f"{movie['id']}.json"), "w") as f:
                    json.dump(movie, f, ensure_ascii=False, indent=2)
            page += 1
    except Exception as e:
        logger.error(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
