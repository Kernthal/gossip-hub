from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List, Optional
from app.models import Post, PostCreate
from app.database import get_db

router = APIRouter()

@router.get("/", response_model=List[Post])
async def get_posts(
    skip: int = 0,
    limit: int = 20,
    sort: str = "latest",
    circle_id: Optional[str] = None,
    db=Depends(get_db)
):
    query = db.table("posts").select("*")
    if circle_id:
        query = query.eq("circle_id", circle_id)
    if sort == "latest":
        query = query.order("created_at", desc=True)
    elif sort == "hot":
        query = query.order("likes", desc=True)
    elif sort == "most_viewed":
        query = query.order("views", desc=True)
    result = query.range(skip, skip + limit).execute()
    return result.data

@router.get("/{post_id}", response_model=Post)
async def get_post(post_id: str, db=Depends(get_db)):
    result = db.table("posts").select("*").eq("id", post_id).execute()
    if not result.data:
        raise HTTPException(status_code=404, detail="Post not found")
    db.table("posts").update({"views": result.data[0]["views"] + 1}).eq("id", post_id).execute()
    return result.data[0]

@router.post("/", response_model=Post)
async def create_post(post: PostCreate, db=Depends(get_db)):
    result = db.table("posts").insert(post.model_dump()).execute()
    return result.data[0]

@router.post("/{post_id}/like")
async def like_post(post_id: str, db=Depends(get_db)):
    result = db.table("posts").select("likes").eq("id", post_id).execute()
    if not result.data:
        raise HTTPException(status_code=404, detail="Post not found")
    db.table("posts").update({"likes": result.data[0]["likes"] + 1}).eq("id", post_id).execute()
    return {"message": "Liked"}

@router.delete("/{post_id}")
async def delete_post(post_id: str, db=Depends(get_db)):
    result = db.table("posts").delete().eq("id", post_id).execute()
    return {"message": "Deleted"}
