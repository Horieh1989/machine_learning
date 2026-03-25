from data import load_movielens_data
from proccessing import build_movie_dataset
from recommender import fit_tfidf, recommend_movies


def setup_model():
    movies, ratings, tags = load_movielens_data()
    movie_data = build_movie_dataset(movies, ratings, tags)
    tfidf_model, tfidf_matrix = fit_tfidf(movie_data)

    return {
        "movies": movies,
        "ratings": ratings,
        "tags": tags,
        "movie_data": movie_data,
        "tfidf_model": tfidf_model,
        "tfidf_matrix": tfidf_matrix,
    }


def predict_movie_recommendations(movie_title, model_state, n_recommendations=5, min_ratings=50):
    return recommend_movies(
        title=movie_title,
        movie_data=model_state["movie_data"],
        tfidf_matrix=model_state["tfidf_matrix"],
        n=n_recommendations,
        min_ratings=min_ratings,
    )
if __name__ == "__main__":
    model_state = setup_model()
    recommendations = predict_movie_recommendations("Toy Story (1995)", model_state)
    print(recommendations)
