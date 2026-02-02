import pickle
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

# Load cleaned dataset
movies = pickle.load(open("ML_Model/final_movies.pkl", "rb"))

# Vectorization
vectorizer = CountVectorizer(
    max_features=5000,
    stop_words="english"
)

vectors = vectorizer.fit_transform(movies["tags"])

print("Vector shape:", vectors.shape)

# Save artifacts
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))
pickle.dump(vectors, open("vectors.pkl", "wb"))

print("Saved vectorizer.pkl and vectors.pkl")


