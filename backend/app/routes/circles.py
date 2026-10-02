from fastapi import APIRouter, Depends, HTTPException
from app.models import Circle, CircleCreate
from app.database import get_db

router = APIRouter()

@router.get("/", response_model=list[Circle])
async def get_circles(parent_id: str = None, db=Depends(get_db)):
    query = db.table("circles").select("*")
    if parent_id:
        query = query.eq("parent_id", parent_id)
    result = query.execute()
    return result.data

@router.post("/", response_model=Circle)
async def create_circle(circle: CircleCreate, db=Depends(get_db)):
    result = db.table("circles").insert(circle.model_dump()).execute()
    return result.data[0]

@router.get("/{circle_id}", response_model=Circle)
async def get_circle(circle_id: str, db=Depends(get_db)):
    result = db.table("circles").select("*").eq("id", circle_id).execute()
    if not result.data:
        raise HTTPException(status_code=404, detail="Circle not found")
    return result.data[0]

@router.post("/{circle_id}/join")
async def join_circle(circle_id: str, invite_code: str, db=Depends(get_db)):
    result = db.table("circles").select("*").eq("id", circle_id).execute()
    if not result.data:
        raise HTTPException(status_code=404, detail="Circle not found")
    circle = result.data[0]
    if circle.get("invite_code") and circle["invite_code"] != invite_code:
        raise HTTPException(status_code=403, detail="Invalid invite code")
    return {"message": "Joined circle"}
