from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import fridge, recipes, onboarding

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://kitchen-sink-lujetvpmy-machelle-s-projects.vercel.app",
        "https://kitchen-sink-eight-lac.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],  # allows OPTIONS, GET, POST, PATCH etc.
    allow_headers=["*"],  # allows X-Device-ID and Content-Type
)

app.include_router(fridge.router)
app.include_router(recipes.router)
app.include_router(onboarding.router)
