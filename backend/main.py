from typing import List
from uuid import uuid4, UUID
from fastapi import FastAPI, HTTPException
from datetime import date
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Path

from models import Movie
from models import MovieUpdateRequest

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"], 
)

db: List[Movie] = [
    Movie(id=UUID("ea2fc03d-a0db-4348-a629-81d5c0ba7a2c"), 
    name="The Avengers",
    rating=12,
    release_date=date(2018, 10, 3),
    description="A group of superheroes must work together to stop an alien invasion."
    ),
    Movie(id=UUID("12b39888-7483-491a-acfc-b9b1b5a1ce5a"), 
    name="After",
    rating=16,
    release_date=date(2013, 8, 1),
    description="A romantic drama about a young woman discovering a love that will change her life."
    )
]


@app.get("/")
async def root():
    return {"Hello": "Mundo"}

@app.get("/api/v1/movies")
async def fetch_movies():
    return db;

@app.get("/api/v1/movies/{movie_id}")
async def fetch_movie_by_id(movie_id: UUID = Path(..., title="The ID of the movie")):
    for movie in db:
        if movie.id == movie_id:
            return movie
    raise HTTPException(
        status_code=404,
        detail=f"Movie with id: {movie_id} not found"
    )

@app.post("/api/v1/movies")
async def register_movie(movie: Movie):
    db.append(movie)
    return {"id": movie.id}

@app.delete("/api/v1/movies/{movie_id}")
async def delete_movie(movie_id: UUID):
    for movie in db:
        if movie.id == movie_id:
            db.remove(movie)
            return
    # Mova a exceção para fora do loop for
    raise HTTPException(
        status_code=404,
        detail=f"Movie with id: {movie_id} does not exists"
    )

@app.put("/api/v1/movies/{movie_id}")
async def update_movie(movie_update: MovieUpdateRequest, movie_id: UUID):
    for movie in db:
        if movie.id == movie_id:
            if movie_update.name is not None:
                movie.name = movie_update.name
            if movie_update.rating is not None:
                movie.rating = movie_update.rating
            if movie_update.release_date is not None:
                movie.release_date = movie_update.release_date
            if movie_update.description is not None:
                movie.description = movie_update.description  # Atualiza a descrição
            return
    raise HTTPException(
        status_code=404,
        detail=f"Movie with id: {movie_id} does not exist"
    )


