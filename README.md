# Gossip Hub

> 一个专属于中学生的八卦社交平台

## 功能特性

### 核心功能

| 功能 | 说明 | 状态 |
|------|------|------|
| 八卦爆料 | 匿名分享小道消息，支持文字、图片、视频 | 已完成 |
| CP配对 | 发起CP投票，支持押注功能 | 已完成 |
| 关系图谱 | 可视化展示用户关系，支持手动标记和自动推断 | 已完成 |
| 八卦预测 | 用户预测 + AI预测，支持押注 | 已完成 |
| AI每周总结 | 自动生成每周八卦总结，带"系统AI"标识 | 已完成 |
| 热度排行 | 浏览最多 / 热点 / 最新 三个维度 | 已完成 |
| 匿名提问箱 | 匿名提问和回答，知乎模式 | 已完成 |
| 圈子系统 | 大圈子 + 细分圈子，支持邀请码加入 | 已完成 |
| 会员体系 | VIP / SVIP / 星钻VIP / 黑钻VIP / 黄钻VIP | 已完成 |
| 虚拟货币 | 平台内"瓜币"，支持充值和消费 | 已完成 |

### 技术特性

- **液态玻璃设计**：iOS 26 风格 UI，backdrop-filter + SVG 滤镜
- **3D 粒子背景**：Three.js 实现的动态粒子效果
- **丰富动画**：GSAP 动画库，流畅的页面过渡
- **响应式设计**：适配桌面端和移动端
- **实时更新**：Supabase Realtime 支持

## 技术栈

| 层级 | 技术 |
|------|------|
| 前端框架 | Vue 3 + Vite + TypeScript |
| UI 样式 | Tailwind CSS + 自定义液态玻璃样式 |
| 3D 效果 | Three.js + TresJS |
| 动画 | GSAP + Fireworks.js |
| 图表 | D3.js + ECharts |
| 后端框架 | Python + FastAPI |
| AI 模型 | PyTorch + Transformers (Hugging Face) |
| 数据库 | Supabase (PostgreSQL) |
| 实时通信 | Supabase Realtime |
| 部署 | GitHub Pages + GitHub Actions |

## 项目结构

```
gossip-hub/
├── frontend/                 # Vue 3 前端
│   ├── src/
│   │   ├── components/       # 组件库
│   │   │   ├── Glass*.vue    # 液态玻璃组件
│   │   │   ├── LiquidGlass.vue
│   │   │   ├── ParticleBackground.vue
│   │   │   ├── AIThinking.vue
│   │   │   ├── Loader.vue
│   │   │   ├── SVGMorph.vue
│   │   │   ├── RelationshipGraph.vue
│   │   │   ├── CPVote.vue
│   │   │   ├── PredictionCard.vue
│   │   │   ├── AnonymousQA.vue
│   │   │   └── ...
│   │   ├── views/            # 页面
│   │   │   ├── Home.vue
│   │   │   ├── Timeline.vue
│   │   │   ├── Ranking.vue
│   │   │   ├── Graph.vue
│   │   │   ├── Profile.vue
│   │   │   ├── Post.vue
│   │   │   ├── PostDetail.vue
│   │   │   ├── Login.vue
│   │   │   ├── Register.vue
│   │   │   ├── Membership.vue
│   │   │   ├── Settings.vue
│   │   │   └── NotFound.vue
│   │   ├── stores/           # Pinia 状态管理
│   │   ├── utils/            # 工具函数
│   │   ├── router/           # 路由配置
│   │   └── App.vue
│   ├── package.json
│   └── vite.config.js
├── backend/                  # Python FastAPI 后端
│   ├── app/
│   │   ├── routes/           # API 路由
│   │   │   ├── posts.py
│   │   │   ├── users.py
│   │   │   ├── votes.py
│   │   │   ├── predictions.py
│   │   │   ├── circles.py
│   │   │   └── memberships.py
│   │   ├── models.py         # 数据模型
│   │   ├── config.py         # 配置
│   │   ├── database.py       # 数据库连接
│   │   └── main.py           # 入口
│   └── requirements.txt
├── ai/                       # AI 模块
│   ├── model.py              # 模型推理
│   └── train.py              # 模型训练
├── docs/                     # 文档
│   └── database_schema.sql   # 数据库表结构
└── .github/
    └── workflows/
        └── deploy.yml        # GitHub Actions 部署
```

## 快速开始

### 前端开发

```bash
cd frontend
npm install
npm run dev
```

前端开发服务器将在 http://localhost:3000 启动。

### 后端开发

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

后端 API 服务器将在 http://localhost:8000 启动。

### 构建部署

```bash
cd frontend
npm run build
```

构建产物将在 `frontend/dist` 目录生成，可通过 GitHub Actions 自动部署到 GitHub Pages。

## 环境变量

### 前端 (.env)

```env
VITE_API_URL=http://localhost:8000
VITE_SUPABASE_URL=your_supabase_url
VITE_SUPABASE_KEY=your_supabase_key
```

### 后端 (.env)

```env
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
SUPABASE_SERVICE_KEY=your_supabase_service_key
SECRET_KEY=your_secret_key
AI_MODEL_NAME=Qwen/Qwen2-0.5B-Instruct
ANONYMOUS_QUOTA_MONTHLY=10
COINS_PER_RMB=10
```

## API 文档

### 帖子 API

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | /api/posts | 获取帖子列表 |
| GET | /api/posts/{id} | 获取帖子详情 |
| POST | /api/posts | 创建帖子 |
| POST | /api/posts/{id}/like | 点赞 |
| DELETE | /api/posts/{id} | 删除帖子 |

### 用户 API

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | /api/users/me | 获取当前用户 |
| POST | /api/users | 注册 |
| PUT | /api/users/me | 更新用户信息 |
| GET | /api/users/{id} | 获取用户信息 |

### 投票 API

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | /api/votes | 获取投票列表 |
| POST | /api/votes | 创建投票 |
| GET | /api/votes/{id} | 获取投票详情 |

### 预测 API

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | /api/predictions | 获取预测列表 |
| POST | /api/predictions | 创建预测 |
| POST | /api/predictions/{id}/resolve | 结算预测 |

### 圈子 API

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | /api/circles | 获取圈子列表 |
| POST | /api/circles | 创建圈子 |
| GET | /api/circles/{id} | 获取圈子详情 |
| POST | /api/circles/{id}/join | 加入圈子 |

### 会员 API

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | /api/memberships/{user_id} | 获取会员信息 |
| POST | /api/memberships | 创建会员 |
| PUT | /api/memberships/{id} | 更新会员 |

## 数据库表

- `users` - 用户表
- `posts` - 帖子表
- `votes` - 投票表
- `predictions` - 预测表
- `circles` - 圈子表
- `circle_members` - 圈子成员表
- `memberships` - 会员表
- `comments` - 评论表
- `ai_summaries` - AI总结表
- `relationships` - 关系图谱表
- `transactions` - 交易记录表

## 会员等级

| 等级 | 价格 | 权益 |
|------|------|------|
| 免费 | - | 每月10条匿名额度 |
| VIP | 9.9元/月 | 每月20条匿名额度 + VIP徽章 |
| SVIP | 19.9元/月 | 每月50条匿名额度 + 优先审核 |
| 星钻VIP | 39.9元/月 | 无限匿名额度 + 去广告 |
| 黑钻VIP | 69.9元/月 | 全部权益 + 专属客服 |
| 黄钻VIP | 99.9元/月 | 全部权益 + 定制功能 |

## 部署

项目通过 GitHub Actions 自动部署到 GitHub Pages。

1. 推送代码到 `master` 分支
2. GitHub Actions 自动构建前端
3. 自动部署到 GitHub Pages

## 许可证

MIT
