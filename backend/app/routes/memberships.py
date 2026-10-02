from fastapi import APIRouter, Depends, HTTPException
from app.models import Membership, MembershipCreate
from app.database import get_db

router = APIRouter()

@router.get("/{user_id}", response_model=Membership)
async def get_membership(user_id: str, db=Depends(get_db)):
    result = db.table("memberships").select("*").eq("user_id", user_id).execute()
    if not result.data:
        raise HTTPException(status_code=404, detail="Membership not found")
    return result.data[0]

@router.post("/", response_model=Membership)
async def create_membership(membership: MembershipCreate, db=Depends(get_db)):
    result = db.table("memberships").insert(membership.model_dump()).execute()
    return result.data[0]

@router.put("/{membership_id}", response_model=Membership)
async def update_membership(membership_id: str, membership: MembershipCreate, db=Depends(get_db)):
    result = db.table("memberships").update(membership.model_dump()).eq("id", membership_id).execute()
    return result.data[0]
