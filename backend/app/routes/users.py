from fastapi import APIRouter, Depends, HTTPException
from app.models import User, UserCreate
from app.database import get_db

router = APIRouter()

@router.get("/me", response_model=User)
async def get_current_user(db=Depends(get_db)):
    # TODO: 从 JWT token 获取当前用户
    result = db.table("users").select("*").limit(1).execute()
    if not result.data:
        raise HTTPException(status_code=404, detail="User not found")
    return result.data[0]

@router.post("/", response_model=User)
async def create_user(user: UserCreate, db=Depends(get_db)):
    result = db.table("users").insert(user.model_dump()).execute()
    return result.data[0]

@router.put("/me", response_model=User)
async def update_user(user: User, db=Depends(get_db)):
    result = db.table("users").update(user.model_dump()).eq("id", user.id).execute()
    return result.data[0]

@router.get("/{user_id}", response_model=User)
async def get_user(user_id: str, db=Depends(get_db)):
    result = db.table("users").select("*").eq("id", user_id).execute()
    if not result.data:
        raise HTTPException(status_code=404, detail="User not found")
    return result.data[0]
