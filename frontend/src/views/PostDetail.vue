<template>
  <div class="post-detail">
    <div v-if="loading" class="post-loading">
      <Loader type="glow" />
    </div>
    <div v-else-if="post" class="post-content">
      <LiquidGlass variant="card">
        <div class="post-main">
          <div class="post-header">
            <div class="post-author">
              <div class="author-avatar">
                <SVGMorph shape="blob" :size="50" color1="#667eea" color2="#764ba2" />
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
          <p class="post-text">{{ post.content }}</p>
          <div v-if="post.images && post.images.length > 0" class="post-images">
            <img
              v-for="(img, index) in post.images"
              :key="index"
              :src="img"
              class="post-image"
            />
          </div>
          <div class="post-actions">
            <button class="action-button" @click="like">
              <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
                <path d="M10 17.5L3.5 11C1.5 9 1.5 6 3.5 4C5.5 2 8.5 2 10 4C11.5 2 14.5 2 16.5 4C18.5 6 18.5 9 16.5 11L10 17.5Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
              <span>{{ post.likes }}</span>
            </button>
            <button class="action-button">
              <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
                <path d="M10 4C5 4 1.5 10 1.5 10C1.5 10 5 16 10 16C15 16 18.5 10 18.5 10C18.5 10 15 4 10 4Z" stroke="currentColor" stroke-width="1.5"/>
                <circle cx="10" cy="10" r="3" stroke="currentColor" stroke-width="1.5"/>
              </svg>
              <span>{{ post.views }}</span>
            </button>
            <button class="action-button">
              <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
                <path d="M10 1C5 1 1 5 1 10C1 12 2 14 4 15.5L3 19L7 17.5C8 18 9 18 10 18C15 18 19 14 19 10C19 5 15 1 10 1Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
              <span>{{ post.comments }}</span>
            </button>
          </div>
        </div>
      </LiquidGlass>

      <div class="comments-section">
        <h3 class="comments-title">评论</h3>
        <div v-if="comments.length === 0" class="comments-empty">
          <EmptyState title="暂无评论" description="成为第一个评论的人吧" />
        </div>
        <div v-else class="comments-list">
          <LiquidGlass v-for="comment in comments" :key="comment.id" variant="card">
            <div class="comment-item">
              <div class="comment-header">
                <span class="comment-author">{{ comment.author }}</span>
                <span class="comment-time">{{ comment.created_at }}</span>
              </div>
              <p class="comment-content">{{ comment.content }}</p>
            </div>
          </LiquidGlass>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import LiquidGlass from '../components/LiquidGlass.vue'
import SVGMorph from '../components/SVGMorph.vue'
import Loader from '../components/Loader.vue'
import EmptyState from '../components/EmptyState.vue'

const route = useRoute()
const post = ref(null)
const comments = ref([])
const loading = ref(true)

function like() {
  // TODO: 点赞逻辑
}

onMounted(async () => {
  // TODO: 从 API 获取帖子详情
  setTimeout(() => {
    loading.value = false
  }, 1000)
})
</script>

<style scoped>
.post-detail {
  max-width: 800px;
  margin: 0 auto;
  padding: 40px 24px;
}

.post-loading {
  display: flex;
  justify-content: center;
  padding: 60px;
}

.post-main {
  padding: 24px;
}

.post-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 20px;
}

.post-author {
  display: flex;
  align-items: center;
  gap: 12px;
}

.author-avatar {
  width: 50px;
  height: 50px;
}

.author-info {
  display: flex;
  flex-direction: column;
}

.author-name {
  font-size: 16px;
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

.post-text {
  font-size: 18px;
  color: #374151;
  line-height: 1.8;
  margin-bottom: 20px;
}

.post-images {
  display: flex;
  gap: 12px;
  margin-bottom: 20px;
  flex-wrap: wrap;
}

.post-image {
  width: 150px;
  height: 150px;
  object-fit: cover;
  border-radius: 12px;
}

.post-actions {
  display: flex;
  gap: 20px;
}

.action-button {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 10px 16px;
  border: none;
  border-radius: 10px;
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

.comments-section {
  margin-top: 32px;
}

.comments-title {
  font-size: 24px;
  font-weight: 700;
  color: white;
  margin-bottom: 20px;
}

.comments-empty {
  padding: 40px;
}

.comments-list {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.comment-item {
  padding: 16px;
}

.comment-header {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 8px;
}

.comment-author {
  font-size: 14px;
  font-weight: 600;
  color: #1f2937;
}

.comment-time {
  font-size: 12px;
  color: #9ca3af;
}

.comment-content {
  font-size: 14px;
  color: #4b5563;
  line-height: 1.6;
}
</style>
