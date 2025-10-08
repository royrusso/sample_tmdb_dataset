# Sample JSON TMDB Dataset

A sample JSON dataset from TMDB. This will generate a small set of JSON files based on TMDB data. One file per movie.

# Dev Setup

You will need a valid TMDB API key to run this project. You can get one by creating an account on [TMDB](https://developer.themoviedb.org/) and requesting an API key.

Add your TMDB API key to a `.env` file in the root of the project:

```bash
TMDB_API_KEY=your_tmdb_api_key_here
```

## Prerequisites

Ensure you have the following installed:

-   Python >= 3.13
-   poetry

## Installation

1. Clone the repository and drop to the root directory:
2. Poetry install and activate the virtual environment:

    ```bash
    poetry install
    ```

3. Run the main script:

    ```bash
    poetry run python src/app.py
    ```

## Configuration

### Number of JSON Files

You can configure the number of JSON files to generate by setting the `NUM_RESULTS` environment variable in your `.env` file.

```bash
NUM_RESULTS=1000
```
