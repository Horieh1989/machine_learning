from dash import Dash, html, dcc, dash_table, Input, Output, State
from pipeline import setup_model, predict_movie_recommendations

model_state = setup_model()
movie_titles = sorted(model_state["movie_data"]["title"].dropna().unique())

app = Dash(__name__)
app.title = "Movie Recommender"

app.layout = html.Div(
    className="app-container",
    children=[
        html.H1("Movie Recommender", className="app-title"),
        html.P(
            "Enter a movie title and get five similar recommendations.",
            className="app-subtitle",
        ),
        dcc.Dropdown(
            id="movie-dropdown",
            options=[{"label": title, "value": title} for title in movie_titles],
            placeholder="Select a movie",
            searchable=True,
        ),
        html.Br(),
        html.Button(
            "Recommend",
            id="recommend-button",
            n_clicks=0,
            className="primary-button",
        ),
        html.Br(),
        html.Br(),
        html.Div(id="message", className="message"),
        dash_table.DataTable(
            id="recommendation-table",
            columns=[
                {"name": "Title", "id": "title"},
                {"name": "Similarity", "id": "similarity"},
                {"name": "Average Rating", "id": "avg_rating"},
                {"name": "Rating Count", "id": "rating_count"},
            ],
            data=[],
            style_table={
                "overflowX": "auto",
                "borderRadius": "12px",
                "overflow": "hidden",
            },
            style_cell={
                "textAlign": "left",
                "padding": "10px",
                "backgroundColor": "#fffdf8",
                "color": "#1f2a44",
                "border": "1px solid #e6dfd2",
            },
            style_header={
                "fontWeight": "bold",
                "backgroundColor": "#102542",
                "color": "white",
                "border": "1px solid #102542",
            },
        ),
    ],
)


@app.callback(
    Output("recommendation-table", "data"),
    Output("message", "children"),
    Input("recommend-button", "n_clicks"),
    State("movie-dropdown", "value"),
)
def update_recommendations(n_clicks, movie_title):
    if not n_clicks:
        return [], ""

    if not movie_title:
        return [], "Please select a movie title."

    recommendations = predict_movie_recommendations(
        movie_title=movie_title,
        model_state=model_state,
        n_recommendations=5,
    )

    if isinstance(recommendations, str):
        return [], recommendations

    result = recommendations.copy()
    result["similarity"] = result["similarity"].round(4)
    result["avg_rating"] = result["avg_rating"].round(2)
    result["rating_count"] = result["rating_count"].astype(int)

    return result.to_dict("records"), f"Top 5 recommendations for: {movie_title}"


if __name__ == "__main__":
    print("Starting Dash app...")
    app.run(debug=False)
