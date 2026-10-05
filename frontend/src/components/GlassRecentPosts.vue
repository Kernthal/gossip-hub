<template>
  <div class="glass-recent-posts">
    <div class="recent-header">
      <h3 class="recent-title">最新八卦</h3>
      <router-link to="/timeline" class="recent-more">查看更多</router-link>
    </div>
    <div class="recent-list">
      <div v-for="post in posts" :key="post.id" class="recent-item">
        <div class="recent-avatar">
          <SVGMorph shape="blob" :size="40" color1="#667eea" color2="#764ba2" />
        </div>
        <div class="recent-content">
          <p class="recent-text">{{ post.content }}</p>
          <div class="recent-meta">
            <span class="recent-author">{{ post.author }}</span>
            <span class="recent-time">{{ post.created_at }}</span>
          </div>
        </div>
        <div class="recent-stats">
          <span class="stat">
            <svg width="14" height="14" viewBox="0 0 14 14" fill="none">
              <path d="M7 12L1 7C0 6 0 4.5 1 3.5C2 2.5 4 2.5 5 3.5C5.5 4 7 4 7 4C7 4 8.5 4 9 3.5C10 2.5 12 2.5 13 3.5C14 4.5 14 6 13 7L7 12Z" stroke="currentColor" stroke-width="1.5"/>
            </svg>
            {{ post.likes }}
          </span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import SVGMorph from './SVGMorph.vue'

defineProps({
  posts: {
    type: Array,
    default: () => []
  }
})
</script>

<style scoped>
.glass-recent-posts {
  padding: 24px;
}

.recent-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 20px;
}

.recent-title {
  font-size: 18px;
  font-weight: 700;
  color: white;
  margin: 0;
}

.recent-more {
  font-size: 14px;
  color: #667eea;
  text-decoration: none;
  transition: color 0.2s;
}

.recent-more:hover {
  color: #764ba2;
}

.recent-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.recent-item {
  display: flex;
  align-items: flex-start;
  gap: 12px;
  padding: 16px;
  background: rgba(255, 255, 255, 0.05);
  border-radius: 12px;
  border: 1px solid rgba(255, 255, 255, 0.1);
  transition: all 0.2s ease;
}

.recent-item:hover {
  background: rgba(255, 255, 255, 0.1);
}

.recent-avatar {
  width: 40px;
  height: 40px;
  flex-shrink: 0;
}

.recent-content {
  flex: 1;
  min-width: 0;
}

.recent-text {
  font-size: 14px;
  color: rgba(255, 255, 255, 0.8);
  margin: 0 0 8px 0;
  line-height: 1.5;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.recent-meta {
  display: flex;
  align-items: center;
  gap: 8px;
}

.recent-author {
  font-size: 12px;
  color: #667eea;
  font-weight: 600;
}

.recent-time {
  font-size: 12px;
  color: rgba(255, 255, 255, 0.4);
}

.recent-stats {
  display: flex;
  align-items: center;
}

.stat {
  display: flex;
  align-items: center;
  gap: 4px;
  font-size: 12px;
  color: rgba(255, 255, 255, 0.5);
}
</style>
