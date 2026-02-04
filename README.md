# 🎬 Movie Recommender System – Backend API

A production-ready Flask REST API for a content-based movie recommender system, powered by machine learning (NLP + vector similarity) and integrated with TMDB API for movie posters.

This backend serves movie recommendations to a React frontend and is optimized for deployment, performance, and scalability.


## 🚀 Features

- Content-based movie recommendation engine
- ML-powered similarity search using vectorization
- Real-time movie posters from TMDB API
- Model loaded once at startup (high performance)
- RESTful API with JSON responses
- CORS enabled for frontend communication
- Production-ready (Gunicorn + Render compatible)


## 🧠 Tech Stack

1. Backend - Flask
2. ML / NLP- Skit-learn
3. Data Processing	Pandas, NumPy
4. Model Artifacts	Pickle (.pkl)   
5. API Integration	TMDB API
6. Server	Gunicorn
7. Deployment	Render


## Folder Structure
```
movie-recommender-backend/
│
├── app.py                 # Flask entry point
├── recommender.py         # Recommendation logic
├── requirements.txt       # Dependencies
├── ML_Model/
│   ├── final_movies.pkl   # Movie metadata (titles, ids)
│   └── vectors.pkl        # Precomputed vectors (ignored in Git)
│
├── .gitignore
└── README.md
```

## 🔗 Live Demo

- Frontend: https://ek-movie-dekho.vercel.app  
- Backend API: https://movies-recommender-backend-zog1.onrender.com  

---

## API Endpoints

```
# GET /

{
  "status": "ok",
  "message": "Movie Recommender API is running"
}

```

## Get Movie Recommendations

```
POST /recommend 


# Request Body

{
  "movie_name": "Superman"
}


# Response

{
  "input_movie": "Superman",
  "results": [
    {
      "id": 8536,
      "title": "Superman II",
      "poster": "https://image.tmdb.org/t/p/w500/xyz.jpg",
      "similarity_score": 0.3876
    }
  ]
}


```

## 🎯 Get All Movie Titles (Autocomplete)

GET /movies

```
[
  "The Dark Knight",
  "Inception",
  "Interstellar",
  "Superman"
]

```

## ⚙️ Setup Instructions (Local)

### 1️. Clone the Repository
```
git clone https://github.com/your-username/movie-recommender-backend.git
cd movie-recommender-backend
```

### 2️. Create Virtual Environment
```
python -m venv venv
source venv/bin/activate     # Linux / macOS
venv\Scripts\activate        # Windows
```

### 3️. Install Dependencies
```
pip install -r requirements.txt
```

### 4️. Set Environment Variables
```
export TMDB_API_KEY=your_api_key   # macOS/Linux
set TMDB_API_KEY=your_api_key      # Windows
```

### 5️. Run the Server
```
python app.py

# Server runs at:
http://localhost:5000
```

## 🔮 Future Enhancements

- Authentication
- Logging & monitoring
- Redis caching
- Hybrid recommendation (content + collaborative)
- Multilingual movie support


## 👨‍💻 Author

`Sanish Kumar`

`Aspiring ML Engineer | Backend Developer`

`Focused on AI, ML, and scalable systems`


- Email: ***sanishbux42@gmail.com***
- Linkedin: https://www.linkedin.com/in/sanish-kumar-singh-163679289
- Kaggle Notebook: https://www.kaggle.com/code/sanishkumarsingh/content-based-movies-recommender-system
- Movies Recommender project demo: "https://ek-movie-dekho.vercel.app"


### ⭐ Support

If you like this project:

- ⭐ Star the repository
- Learn from it