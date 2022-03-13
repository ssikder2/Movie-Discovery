"""Movie.py file"""
import os
import random
import requests
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

movies = ["634649", "284052", "299534", "51876", "671"]


def get_movie_id():
    """Get Movie ID method"""
    random_movie = random.choice(movies)
    return random_movie


def get_wiki_data(title):
    """Get Wikipedia Data method"""
    wiki_url = (
        "https://en.wikipedia.org/w/api.php?action=query&titles="
        + title
        + "&format=json&formatversion=2"
    )
    response = requests.get(wiki_url)
    wiki = response.json()
    return wiki


def get_movie_data(movie_id):
    """Get Movie Data method"""
    tmdb_key = os.getenv("TMDB_KEY")
    base_url = (
        "https://api.themoviedb.org/3/movie/"
        + movie_id
        + "?api_key="
        + tmdb_key
        + "&language=en-US"
    )

    query_params = {"api-key": tmdb_key}

    response = requests.get(
        base_url,
        params=query_params,
    )

    movie = response.json()

    title = movie["title"]
    tagline = movie["tagline"]
    genres = movie["genres"]
    poster_path = movie["poster_path"]

    return {
        "title": title,
        "tagline": tagline,
        "genres": genres,
        "poster_path": poster_path,
    }
