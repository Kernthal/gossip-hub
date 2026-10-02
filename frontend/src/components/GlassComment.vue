<template>
  <div class="glass-comment">
    <div class="comment-header">
      <div class="comment-avatar">
        <GlassAvatar :src="avatar" size="small" />
      </div>
      <div class="comment-info">
        <span class="comment-author">{{ author }}</span>
        <span class="comment-time">{{ time }}</span>
      </div>
    </div>
    <div class="comment-body">
      <p class="comment-text">{{ content }}</p>
    </div>
    <div class="comment-actions">
      <button class="action-button" @click="like">
        <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
          <path d="M8 14L2 8C0.5 6.5 0.5 4 2 2.5C3.5 1 6 1 7 2.5C7.5 3 8 3.5 8 3.5C8 3.5 8.5 3 9 2.5C10 1 12.5 1 14 2.5C15.5 4 15.5 6.5 14 8L8 14Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
        <span>{{ likes }}</span>
      </button>
      <button class="action-button" @click="reply">
        <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
          <path d="M8 1C4 1 1 4 1 8C1 9.5 1.5 11 2.5 12L2 15L5 13.5C6 14 7 14 8 14C12 14 15 11 15 8C15 4 12 1 8 1Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
        <span>回复</span>
      </button>
    </div>
  </div>
</template>

<script setup>
import GlassAvatar from './GlassAvatar.vue'

defineProps({
  avatar: {
    type: String,
    default: ''
  },
  author: {
    type: String,
    required: true
  },
  time: {
    type: String,
    default: ''
  },
  content: {
    type: String,
    required: true
  },
  likes: {
    type: Number,
    default: 0
  }
})

const emit = defineEmits(['like', 'reply'])

function like() {
  emit('like')
}

function reply() {
  emit('reply')
}
</script>

<style scoped>
.glass-comment {
  padding: 16px;
  background: rgba(255, 255, 255, 0.05);
  border-radius: 12px;
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.comment-header {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 12px;
}

.comment-avatar {
  width: 32px;
  height: 32px;
}

.comment-info {
  display: flex;
  flex-direction: column;
}

.comment-author {
  font-size: 14px;
  font-weight: 600;
  color: white;
}

.comment-time {
  font-size: 12px;
  color: rgba(255, 255, 255, 0.5);
}

.comment-body {
  margin-bottom: 12px;
}

.comment-text {
  font-size: 14px;
  color: rgba(255, 255, 255, 0.8);
  line-height: 1.6;
}

.comment-actions {
  display: flex;
  gap: 16px;
}

.action-button {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 6px 12px;
  border: none;
  border-radius: 6px;
  background: transparent;
  color: rgba(255, 255, 255, 0.5);
  font-size: 12px;
  cursor: pointer;
  transition: all 0.2s ease;
}

.action-button:hover {
  background: rgba(255, 255, 255, 0.1);
  color: white;
}
</style>
