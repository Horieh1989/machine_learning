from pathlib import Path
import pandas as pd


def find_data_dir():
    candidates = [
        Path("data"),
        Path("lab1/data"),
        Path("../data"),
        Path("data/ml-latest"),
        Path("lab1/data/ml-latest"),
        Path("../data/ml-latest"),
    ]

    for data_dir in candidates:
        if all((data_dir / name).exists() for name in ["movies.csv", "ratings.csv", "tags.csv"]):
            return data_dir

    raise FileNotFoundError(
        "Could not find MovieLens data directory containing movies.csv, ratings.csv, and tags.csv."
    )


def load_movies(data_dir=None):
    data_dir = find_data_dir() if data_dir is None else Path(data_dir)
    return pd.read_csv(data_dir / "movies.csv")


def load_ratings(data_dir=None):
    data_dir = find_data_dir() if data_dir is None else Path(data_dir)
    return pd.read_csv(data_dir / "ratings.csv")


def load_tags(data_dir=None):
    data_dir = find_data_dir() if data_dir is None else Path(data_dir)
    return pd.read_csv(data_dir / "tags.csv")


def load_movielens_data(data_dir=None):
    data_dir = find_data_dir() if data_dir is None else Path(data_dir)

    movies = pd.read_csv(data_dir / "movies.csv")
    ratings = pd.read_csv(data_dir / "ratings.csv")
    tags = pd.read_csv(data_dir / "tags.csv")

    return movies, ratings, tags


if __name__ == "__main__":
    movies, ratings, tags = load_movielens_data()
    print(movies.head())
    print(ratings.head())
    print(tags.head())
