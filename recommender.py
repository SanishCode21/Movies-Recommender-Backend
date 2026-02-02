import pickle
import difflib
import requests
import os
from sklearn.metrics.pairwise import cosine_similarity

TMDB_API_KEY = os.getenv("TMDB_API_KEY")
POSTER_BASE_URL = "https://image.tmdb.org/t/p/w500"


class MovieRecommender:
    def __init__(self, movies_path, vectors_path):
        self.movies = pickle.load(open(movies_path, "rb"))
        self.vectors = pickle.load(open(vectors_path, "rb"))

        self.movie_index = {
            title.lower(): idx
            for idx, title in enumerate(self.movies["title"])
        }

    def closest_title(self, movie_name):
        matches = difflib.get_close_matches(
            movie_name.lower(),
            self.movie_index.keys(),
            n=1,
            cutoff=0.6
        )
        return matches[0] if matches else None

    def fetch_poster(self, movie_id):
        url = f"https://api.themoviedb.org/3/movie/{movie_id}"
        params = {
            "api_key": TMDB_API_KEY,
            "language": "en-US"
        }

        try:
            res = requests.get(url, params=params)

            if res.status_code != 200:
                print("TMDB error:", res.status_code, res.text)
                return None

            data = res.json()
            poster_path = data["poster_path"]

            if not poster_path:
                return "https://via.placeholder.com/300x450?text=No+Poster"

            return POSTER_BASE_URL + poster_path

        except Exception as e:
            print("Poster fetch error:", e)
            return None


    def recommend(self, movie_name, top_n=10):
        movie_name = movie_name.lower().strip()

        if movie_name not in self.movie_index:
            movie_name = self.closest_title(movie_name)
            if not movie_name:
                return {"error": "Movie not found"}

        idx = self.movie_index[movie_name]

        scores = cosine_similarity(
            self.vectors[idx],
            self.vectors
        ).flatten()

        top_indices = scores.argsort()[::-1][1:top_n + 1]

        results = []
        for i in top_indices:
            movie_id = int(self.movies.iloc[i]["id"])
            results.append({
                "id": movie_id,
                "title": self.movies.iloc[i]["title"],
                "similarity_score": round(float(scores[i]), 4),
                "poster": self.fetch_poster(movie_id)
            })

        return {
            "input_movie": self.movies.iloc[idx]["title"],
            "results": results
        }



