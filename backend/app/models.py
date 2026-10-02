from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class PostBase(BaseModel):
    content: str
    type: str = "gossip"
    is_anonymous: bool = True

class PostCreate(PostBase):
    images: Optional[List[str]] = []
    circle_id: Optional[str] = None

class Post(PostBase):
    id: str
    author: str
    author_id: Optional[str] = None
    created_at: datetime
    views: int = 0
    likes: int = 0
    comments: int = 0
    images: List[str] = []
    circle_id: Optional[str] = None
    is_verified: bool = False

    class Config:
        from_attributes = True

class UserBase(BaseModel):
    email: str
    name: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: str
    membership_tier: str = "free"
    anonymous_quota: int = 10
    coins: int = 0
    created_at: datetime

    class Config:
        from_attributes = True

class VoteBase(BaseModel):
    post_id: str
    vote_type: str  # "cp" or "prediction"
    target_id: Optional[str] = None

class VoteCreate(VoteBase):
    coins: int = 0

class Vote(VoteBase):
    id: str
    user_id: str
    created_at: datetime

    class Config:
        from_attributes = True

class PredictionBase(BaseModel):
    post_id: str
    content: str
    target_date: Optional[datetime] = None

class PredictionCreate(PredictionBase):
    coins: int = 0

class Prediction(PredictionBase):
    id: str
    user_id: str
    ai_confidence: Optional[float] = None
    created_at: datetime
    is_resolved: bool = False
    is_correct: Optional[bool] = None

    class Config:
        from_attributes = True

class CircleBase(BaseModel):
    name: str
    description: Optional[str] = None
    parent_id: Optional[str] = None

class CircleCreate(CircleBase):
    invite_code: Optional[str] = None

class Circle(CircleBase):
    id: str
    owner_id: str
    member_count: int = 0
    max_members: int = 500
    created_at: datetime

    class Config:
        from_attributes = True

class MembershipBase(BaseModel):
    user_id: str
    tier: str = "free"

class MembershipCreate(MembershipBase):
    pass

class Membership(MembershipBase):
    id: str
    started_at: datetime
    expires_at: Optional[datetime] = None

    class Config:
        from_attributes = True
