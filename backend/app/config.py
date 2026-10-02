import os
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL", "")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "")
SUPABASE_SERVICE_KEY = os.getenv("SUPABASE_SERVICE_KEY", "")

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")

SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-here")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# AI Model settings
AI_MODEL_NAME = os.getenv("AI_MODEL_NAME", "Qwen/Qwen2-0.5B-Instruct")
AI_USE_LOCAL = os.getenv("AI_USE_LOCAL", "false").lower() == "true"
AI_MODEL_PATH = os.getenv("AI_MODEL_PATH", "./models/gossip-model")

# Anonymous quota
ANONYMOUS_QUOTA_MONTHLY = int(os.getenv("ANONYMOUS_QUOTA_MONTHLY", "10"))

# Virtual currency
COINS_PER_RMB = int(os.getenv("COINS_PER_RMB", "10"))
