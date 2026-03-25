import pandas as pd


def clean_tags(tags):
    tags_clean = tags.dropna(subset=["tag"]).copy()
    tags_clean["tag"] = tags_clean["tag"].str.lower().str.strip()
    tags_clean = tags_clean[tags_clean["tag"] != ""]
    return tags_clean


def aggregate_movie_tags(tags):
    return (
        tags.groupby("movieId")["tag"]
        .apply(lambda x: " ".join(x))
        .reset_index(name="tag_text")
    )


def summarize_ratings(ratings):
    return (
        ratings.groupby("movieId")["rating"]
        .agg(rating_count="count", avg_rating="mean")
        .reset_index()
    )


def clean_genres(movies):
    movies = movies.copy()
    movies["genres_clean"] = (
        movies["genres"]
        .str.replace("|", " ", regex=False)
        .str.lower()
        .str.strip()
    )
    return movies


def build_movie_dataset(movies, ratings, tags):
    tags_clean = clean_tags(tags)
    movie_tags = aggregate_movie_tags(tags_clean)
    rating_summary = summarize_ratings(ratings)
    movies_clean = clean_genres(movies)

    movie_data = (
        movies_clean
        .merge(movie_tags, on="movieId", how="left")
        .merge(rating_summary, on="movieId", how="left")
    )

    movie_data["tag_text"] = movie_data["tag_text"].fillna("")
    movie_data["rating_count"] = movie_data["rating_count"].fillna(0)
    movie_data["avg_rating"] = movie_data["avg_rating"].fillna(0)

    movie_data["text_features"] = (
        movie_data["genres_clean"] + " " + movie_data["tag_text"]
    ).str.strip()

    return movie_data
if __name__ == "__main__":
    from data import load_movielens_data

    movies, ratings, tags = load_movielens_data()
    movie_data = build_movie_dataset(movies, ratings, tags)

    print(movie_data[["movieId", "title", "genres_clean", "tag_text", "rating_count", "avg_rating", "text_features"]].head())
    print(movie_data.shape)
