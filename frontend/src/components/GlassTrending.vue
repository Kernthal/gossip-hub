<template>
  <div class="glass-trending">
    <div class="trending-header">
      <h3 class="trending-title">热门话题</h3>
    </div>
    <div class="trending-list">
      <div v-for="(topic, index) in topics" :key="topic.id" class="trending-item">
        <div class="trending-rank">{{ index + 1 }}</div>
        <div class="trending-content">
          <p class="trending-name">{{ topic.name }}</p>
          <span class="trending-count">{{ topic.count }} 讨论</span>
        </div>
        <div class="trending-change" :class="topic.change > 0 ? 'is-up' : 'is-down'">
          <svg v-if="topic.change > 0" width="12" height="12" viewBox="0 0 12 12" fill="none">
            <path d="M6 2L10 8H2L6 2Z" fill="currentColor"/>
          </svg>
          <svg v-else width="12" height="12" viewBox="0 0 12 12" fill="none">
            <path d="M6 10L2 4H10L6 10Z" fill="currentColor"/>
          </svg>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  topics: {
    type: Array,
    required: true
  }
})
</script>

<style scoped>
.glass-trending {
  padding: 24px;
}

.trending-header {
  margin-bottom: 20px;
}

.trending-title {
  font-size: 18px;
  font-weight: 700;
  color: white;
  margin: 0;
}

.trending-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.trending-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 16px;
  background: rgba(255, 255, 255, 0.05);
  border-radius: 12px;
  border: 1px solid rgba(255, 255, 255, 0.1);
  transition: all 0.2s ease;
}

.trending-item:hover {
  background: rgba(255, 255, 255, 0.1);
}

.trending-rank {
  width: 24px;
  height: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 6px;
  background: rgba(255, 255, 255, 0.1);
  font-size: 12px;
  font-weight: 700;
  color: rgba(255, 255, 255, 0.7);
}

.trending-item:nth-child(1) .trending-rank {
  background: linear-gradient(135deg, #ffd700, #ffaa00);
  color: white;
}

.trending-item:nth-child(2) .trending-rank {
  background: linear-gradient(135deg, #c0c0c0, #a0a0a0);
  color: white;
}

.trending-item:nth-child(3) .trending-rank {
  background: linear-gradient(135deg, #cd7f32, #b87333);
  color: white;
}

.trending-content {
  flex: 1;
}

.trending-name {
  font-size: 14px;
  font-weight: 600;
  color: white;
  margin: 0 0 2px 0;
}

.trending-count {
  font-size: 12px;
  color: rgba(255, 255, 255, 0.5);
}

.trending-change {
  display: flex;
  align-items: center;
}

.trending-change.is-up {
  color: #10b981;
}

.trending-change.is-down {
  color: #ef4444;
}
</style>
