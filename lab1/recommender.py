import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


def fit_tfidf(movie_data):
    tfidf = TfidfVectorizer(stop_words="english")
    tfidf_matrix = tfidf.fit_transform(movie_data["text_features"])
    return tfidf, tfidf_matrix


def recommend_movies(title, movie_data, tfidf_matrix, n=5, min_ratings=50):
    indices = pd.Series(movie_data.index, index=movie_data["title"]).drop_duplicates()

    if title not in indices:
        return f"Movie '{title}' not found."

    idx = indices[title]

    sim_scores = linear_kernel(tfidf_matrix[idx:idx + 1], tfidf_matrix).flatten()

    similar_movies = movie_data.copy()
    similar_movies["similarity"] = sim_scores

    similar_movies = similar_movies[similar_movies["title"] != title]
    similar_movies = similar_movies[similar_movies["rating_count"] >= min_ratings]

    similar_movies = similar_movies.sort_values(
        by=["similarity", "avg_rating"],
        ascending=[False, False]
    )

    return similar_movies[["title", "similarity", "avg_rating", "rating_count"]].head(n)

if __name__ == "__main__":
    from data import load_movielens_data
    from proccessing import build_movie_dataset

    movies, ratings, tags = load_movielens_data()
    movie_data = build_movie_dataset(movies, ratings, tags)
    _, tfidf_matrix = fit_tfidf(movie_data)

    print(recommend_movies("Toy Story (1995)", movie_data, tfidf_matrix))
