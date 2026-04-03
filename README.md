
# Movie Recommender System

This project is a movie recommendation system built with the MovieLens dataset.  
It recommends five similar movies based on one selected input movie.

The system uses a content-based filtering approach and combines movie genres with user-generated tags.  
The final application is presented with a Dash frontend.

## Features

- Loads MovieLens data from `movies.csv`, `ratings.csv`, and `tags.csv`
- Cleans and merges movie metadata, tags, and rating summaries
- Uses TF-IDF vectorization on genres and tags
- Uses cosine similarity to find similar movies
- Recommends five movies based on a selected title
- Includes a Dash web interface for user interaction

## Method

The recommendation method is content-based filtering.

Each movie is represented using:
- cleaned genres from `movies.csv`
- aggregated user tags from `tags.csv`

These text features are combined into one text field and transformed into numeric vectors using TF-IDF.

Similarity between movies is then measured using cosine similarity.  
Given one movie title as input, the system compares that movie to all others and returns the five most similar movies.

To improve recommendation quality, the system also uses rating summary information:
- average rating
- number of ratings

## Project Structure

```text
lab1/
  app.py
  data.py
  pipeline.py
  proccessing.py
  recommender.py
  assets/
    style.css
  data/
    movies.csv
    ratings.csv
    tags.csv
  notebooks/
```

## Files

- `data.py`  
  Loads MovieLens data files.

- `proccessing.py`  
  Cleans tags, summarizes ratings, cleans genres, and builds the merged movie dataset.

- `recommender.py`  
  Builds TF-IDF features and generates movie recommendations.

- `pipeline.py`  
  Connects the data loading, preprocessing, and recommendation logic.

- `app.py`  
  Runs the Dash frontend.

- `assets/style.css`  
  Contains custom CSS styling for the Dash app.

## Requirements

Install dependencies with:

```bash
pip install -r requirements.txt
```

If Dash is not included in `requirements.txt`, install it with:

```bash
pip install dash
```

## How To Run

From the project root:

```bash
python lab1/app.py
```

Then open this address in your browser:

```text
http://127.0.0.1:8050/
```

## Example

If the input movie is:

```text
Toy Story (1995)
```

Example recommendations may include:
- Toy Story 2 (1999)
- A Bug's Life (1998)
- Toy Story 3 (2010)
- Finding Dory (2016)
- Monsters, Inc. (2001)

## Notes

- `ratings.csv` is very large, so the project uses movie-level rating summaries instead of building a full user-movie matrix.
- Tags are used because they provide richer semantic information than genres alone.
- The current system is not personalized per user; it recommends movies based on similarity between movie content.


