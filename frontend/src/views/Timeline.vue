<template>
  <div class="timeline">
    <div class="timeline-header">
      <h1 class="timeline-title">时间线</h1>
      <GlassButton variant="primary" @click="$router.push('/post')">
        发布八卦
      </GlassButton>
    </div>

    <div class="timeline-tabs">
      <button
        v-for="tab in tabs"
        :key="tab.key"
        class="tab-button"
        :class="{ 'is-active': activeTab === tab.key }"
        @click="activeTab = tab.key"
      >
        {{ tab.label }}
      </button>
    </div>

    <div class="timeline-content">
      <div v-if="loading" class="timeline-loading">
        <Loader type="glow" />
      </div>
      <div v-else-if="posts.length === 0" class="timeline-empty">
        <EmptyState title="暂无内容" description="成为第一个发布八卦的人吧">
          <GlassButton variant="primary" @click="$router.push('/post')">
            发布八卦
          </GlassButton>
        </EmptyState>
      </div>
      <div v-else class="posts-list">
        <LiquidGlass v-for="post in posts" :key="post.id" variant="card">
          <div class="post-card">
            <div class="post-header">
              <div class="post-author">
                <div class="author-avatar">
                  <SVGMorph shape="blob" :size="40" color1="#667eea" color2="#764ba2" />
                </div>
                <div class="author-info">
                  <span class="author-name">{{ post.author }}</span>
                  <span class="post-time">{{ post.created_at }}</span>
                </div>
              </div>
              <span class="post-type" :class="`type-${post.type}`">
                {{ post.type }}
              </span>
            </div>
            <p class="post-content">{{ post.content }}</p>
            <div v-if="post.images && post.images.length > 0" class="post-images">
              <img
                v-for="(img, index) in post.images"
                :key="index"
                :src="img"
                class="post-image"
              />
            </div>
            <div class="post-actions">
              <button class="action-button" @click="likePost(post)">
                <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
                  <path d="M10 17.5L3.5 11C1.5 9 1.5 6 3.5 4C5.5 2 8.5 2 10 4C11.5 2 14.5 2 16.5 4C18.5 6 18.5 9 16.5 11L10 17.5Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
                <span>{{ post.likes }}</span>
              </button>
              <button class="action-button" @click="viewPost(post)">
                <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
                  <path d="M10 4C5 4 1.5 10 1.5 10C1.5 10 5 16 10 16C15 16 18.5 10 18.5 10C18.5 10 15 4 10 4Z" stroke="currentColor" stroke-width="1.5"/>
                  <circle cx="10" cy="10" r="3" stroke="currentColor" stroke-width="1.5"/>
                </svg>
                <span>{{ post.views }}</span>
              </button>
              <button class="action-button" @click="commentPost(post)">
                <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
                  <path d="M10 1C5 1 1 5 1 10C1 12 2 14 4 15.5L3 19L7 17.5C8 18 9 18 10 18C15 18 19 14 19 10C19 5 15 1 10 1Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
                <span>{{ post.comments }}</span>
              </button>
            </div>
          </div>
        </LiquidGlass>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import GlassButton from '../components/GlassButton.vue'
import LiquidGlass from '../components/LiquidGlass.vue'
import SVGMorph from '../components/SVGMorph.vue'
import Loader from '../components/Loader.vue'
import EmptyState from '../components/EmptyState.vue'

const tabs = [
  { key: 'latest', label: '最新' },
  { key: 'hot', label: '热点' },
  { key: 'most_viewed', label: '浏览最多' }
]

const activeTab = ref('latest')
const posts = ref([])
const loading = ref(true)

function likePost(post) {
  // TODO: 实现点赞逻辑
}

function viewPost(post) {
  // TODO: 跳转到详情页
}

function commentPost(post) {
  // TODO: 实现评论逻辑
}

onMounted(async () => {
  // TODO: 从 API 获取数据
  setTimeout(() => {
    loading.value = false
    posts.value = []
  }, 1000)
})
</script>

<style scoped>
.timeline {
  max-width: 800px;
  margin: 0 auto;
  padding: 40px 24px;
}

.timeline-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 32px;
}

.timeline-title {
  font-size: 36px;
  font-weight: 800;
  color: white;
  text-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
}

.timeline-tabs {
  display: flex;
  gap: 8px;
  margin-bottom: 32px;
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  padding: 4px;
  border-radius: 12px;
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.tab-button {
  flex: 1;
  padding: 12px 24px;
  border: none;
  border-radius: 8px;
  background: transparent;
  color: rgba(255, 255, 255, 0.7);
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.tab-button:hover {
  color: white;
}

.tab-button.is-active {
  background: rgba(255, 255, 255, 0.2);
  color: white;
}

.timeline-loading {
  display: flex;
  justify-content: center;
  padding: 60px;
}

.timeline-empty {
  padding: 60px;
}

.posts-list {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.post-card {
  padding: 20px;
}

.post-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 16px;
}

.post-author {
  display: flex;
  align-items: center;
  gap: 12px;
}

.author-avatar {
  width: 40px;
  height: 40px;
}

.author-info {
  display: flex;
  flex-direction: column;
}

.author-name {
  font-size: 14px;
  font-weight: 600;
  color: #1f2937;
}

.post-time {
  font-size: 12px;
  color: #9ca3af;
}

.post-type {
  padding: 4px 12px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 600;
  text-transform: uppercase;
}

.type-gossip {
  background: rgba(102, 126, 234, 0.1);
  color: #667eea;
}

.type-cp {
  background: rgba(240, 147, 251, 0.1);
  color: #f093fb;
}

.type-prediction {
  background: rgba(79, 172, 254, 0.1);
  color: #4facfe;
}

.post-content {
  font-size: 16px;
  color: #374151;
  line-height: 1.6;
  margin-bottom: 16px;
}

.post-images {
  display: flex;
  gap: 8px;
  margin-bottom: 16px;
  flex-wrap: wrap;
}

.post-image {
  width: 100px;
  height: 100px;
  object-fit: cover;
  border-radius: 8px;
}

.post-actions {
  display: flex;
  gap: 16px;
}

.action-button {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 8px 12px;
  border: none;
  border-radius: 8px;
  background: transparent;
  color: #6b7280;
  font-size: 14px;
  cursor: pointer;
  transition: all 0.2s ease;
}

.action-button:hover {
  background: rgba(102, 126, 234, 0.1);
  color: #667eea;
}
</style>
