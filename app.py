# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from recommender import MovieRecommender
import os

app = Flask(__name__)

FRONTEND_URL = os.getenv("FRONTEND_URL")

CORS(app, resources={
    r"/*": {
        "origins": [
            "http://localhost:5173",
            "https://ek-movie-dekho.vercel.app",
            FRONTEND_URL
        ]
    }
})

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# correct constructor usage
recommender = MovieRecommender(
    movies_path=os.path.join(BASE_DIR, "ML_Model/final_movies.pkl"),
    vectors_path=os.path.join(BASE_DIR, "ML_Model/vectors.pkl")
)

@app.route("/", methods=["GET"])
def health_check():
    return jsonify({
        "status": "ok",
        "message": "Movie Recommender API is running"
    })

@app.route("/recommend", methods=["POST"])
def recommend_movie():
    data = request.get_json()
    movie_name = data.get("movie_name")

    if not movie_name:
        return jsonify({"error": "movie_name is required"}), 400

    return jsonify(recommender.recommend(movie_name))

@app.route("/movies", methods=["GET"])
def get_all_movies():
    return jsonify(recommender.movies["title"].tolist())



#  do NOT use debug=True on Render
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

