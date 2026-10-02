from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import posts, users, votes, predictions, circles, memberships

app = FastAPI(
    title="Gossip Hub API",
    description="A gossip social platform for middle school students",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(posts.router, prefix="/api/posts", tags=["posts"])
app.include_router(users.router, prefix="/api/users", tags=["users"])
app.include_router(votes.router, prefix="/api/votes", tags=["votes"])
app.include_router(predictions.router, prefix="/api/predictions", tags=["predictions"])
app.include_router(circles.router, prefix="/api/circles", tags=["circles"])
app.include_router(memberships.router, prefix="/api/memberships", tags=["memberships"])

@app.get("/")
async def root():
    return {"message": "Welcome to Gossip Hub API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
