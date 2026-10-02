# Gossip Hub

> A gossip social platform for middle school students

## Features

- Anonymous gossip posting
- CP pairing and voting
- Relationship graph visualization
- Gossip prediction and betting
- AI weekly summary
- Hot ranking (views / trending / latest)
- Anonymous Q&A
- Circle system (large + small circles)
- Membership tiers (VIP to Black Diamond)
- Virtual currency + payment

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | Vue 3 + Vite + Tailwind CSS |
| Visualization | D3.js + ECharts |
| Backend | Python + FastAPI |
| AI | PyTorch + Transformers |
| Database | Supabase (PostgreSQL) |
| Realtime | Supabase Realtime |
| Deployment | GitHub Pages + Vercel |

## Project Structure

```
gossip-hub/
├── frontend/          # Vue 3 frontend
├── backend/           # Python FastAPI backend
├── ai/                # AI model training/inference
├── docs/              # Documentation
└── scripts/           # Utility scripts
```

## Getting Started

### Prerequisites

- Node.js 18+
- Python 3.10+
- Supabase account

### Installation

```bash
# Clone the repository
git clone https://github.com/Kernthal/gossip-hub.git
cd gossip-hub

# Install frontend dependencies
cd frontend
npm install

# Install backend dependencies
cd ../backend
pip install -r requirements.txt
```

### Environment Variables

Create `.env` files in both `frontend/` and `backend/` directories.

## License

MIT
