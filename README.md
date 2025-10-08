# Sample JSON TMDB Dataset

A sample JSON dataset from TMDB. This will generate a small set of JSON files based on TMDB data. One file per movie.

## Dev Setup

You will need a valid TMDB API key to run this project. You can get one by creating an account on [TMDB](https://developer.themoviedb.org/) and requesting an API key.

Add your TMDB API key to a `.env` file in the root of the project:

```bash
TMDB_API_KEY=your_tmdb_api_key_here
```

### Prerequisites

Ensure you have the following installed:

-   Python >= 3.13
-   poetry >= 2.0.0

### Installation

1. Clone the repository and drop to the root directory:
2. Poetry install dependencies:

    ```bash
    poetry install
    ```

3. Run the main script:

    ```bash
    poetry run python src/app.py
    ```

### Configuration

#### Number of Movies

You can configure the number of JSON files to generate by setting the `NUM_RESULTS` environment variable in your `.env` file.

```bash
NUM_RESULTS=1000
```

## Data Files

Data files are located in the `data` directory. Each file is named using the movie's TMDB ID. The github repo, includes 1000 sample files.

For schema definition, read the [TMDB API Top Rated documentation](https://developer.themoviedb.org/reference/movie-top-rated-list).

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.
