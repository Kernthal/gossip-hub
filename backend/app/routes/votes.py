from fastapi import APIRouter, Depends, HTTPException
from app.models import Vote, VoteCreate
from app.database import get_db

router = APIRouter()

@router.get("/", response_model=list[Vote])
async def get_votes(post_id: str = None, db=Depends(get_db)):
    query = db.table("votes").select("*")
    if post_id:
        query = query.eq("post_id", post_id)
    result = query.execute()
    return result.data

@router.post("/", response_model=Vote)
async def create_vote(vote: VoteCreate, db=Depends(get_db)):
    result = db.table("votes").insert(vote.model_dump()).execute()
    return result.data[0]

@router.get("/{vote_id}", response_model=Vote)
async def get_vote(vote_id: str, db=Depends(get_db)):
    result = db.table("votes").select("*").eq("id", vote_id).execute()
    if not result.data:
        raise HTTPException(status_code=404, detail="Vote not found")
    return result.data[0]
