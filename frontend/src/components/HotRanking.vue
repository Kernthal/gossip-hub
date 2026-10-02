<template>
  <div class="hot-ranking">
    <div class="ranking-header">
      <h3 class="ranking-title">热度排行</h3>
      <div class="ranking-tabs">
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
    </div>

    <div class="ranking-list">
      <div v-if="loading" class="ranking-loading">
        <Loader type="dots" />
      </div>
      <div v-else-if="items.length === 0" class="ranking-empty">
        <EmptyState title="暂无排行" description="还没有足够的数据" />
      </div>
      <div v-else class="ranking-items">
        <div
          v-for="(item, index) in items"
          :key="item.id"
          class="ranking-item"
          :class="{ 'top-3': index < 3 }"
        >
          <div class="ranking-position">
            <span class="position-number">{{ index + 1 }}</span>
          </div>
          <div class="ranking-info">
            <h4 class="item-title">{{ item.title }}</h4>
            <p class="item-desc">{{ item.description }}</p>
          </div>
          <div class="ranking-stats">
            <span class="stat-value">{{ formatNumber(item.views) }}</span>
            <span class="stat-label">浏览</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import Loader from './Loader.vue'
import EmptyState from './EmptyState.vue'

const tabs = [
  { key: 'most_viewed', label: '浏览最多' },
  { key: 'hot', label: '热点' },
  { key: 'latest', label: '最新' }
]

const activeTab = ref('most_viewed')
const items = ref([])
const loading = ref(true)

function formatNumber(num) {
  if (num >= 10000) {
    return (num / 10000).toFixed(1) + 'w'
  }
  if (num >= 1000) {
    return (num / 1000).toFixed(1) + 'k'
  }
  return num.toString()
}

onMounted(async () => {
  // TODO: 从 API 获取排行数据
  setTimeout(() => {
    loading.value = false
    items.value = []
  }, 1000)
})
</script>

<style scoped>
.hot-ranking {
  padding: 24px;
}

.ranking-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 20px;
}

.ranking-title {
  font-size: 20px;
  font-weight: 700;
  color: #1f2937;
}

.ranking-tabs {
  display: flex;
  gap: 4px;
  background: rgba(102, 126, 234, 0.1);
  padding: 4px;
  border-radius: 8px;
}

.tab-button {
  padding: 6px 12px;
  border: none;
  border-radius: 6px;
  background: transparent;
  color: #6b7280;
  font-size: 12px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
}

.tab-button.is-active {
  background: white;
  color: #667eea;
}

.ranking-loading {
  display: flex;
  justify-content: center;
  padding: 40px;
}

.ranking-empty {
  padding: 40px;
}

.ranking-items {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.ranking-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px;
  background: rgba(102, 126, 234, 0.05);
  border-radius: 12px;
  transition: all 0.2s ease;
}

.ranking-item:hover {
  background: rgba(102, 126, 234, 0.1);
}

.ranking-item.top-3 {
  background: linear-gradient(135deg, rgba(255, 215, 0, 0.1), rgba(255, 170, 0, 0.1));
}

.ranking-position {
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  background: rgba(102, 126, 234, 0.1);
}

.position-number {
  font-size: 14px;
  font-weight: 700;
  color: #667eea;
}

.ranking-item.top-3 .ranking-position {
  background: linear-gradient(135deg, #ffd700, #ffaa00);
}

.ranking-item.top-3 .position-number {
  color: white;
}

.ranking-info {
  flex: 1;
}

.item-title {
  font-size: 14px;
  font-weight: 600;
  color: #1f2937;
  margin-bottom: 4px;
}

.item-desc {
  font-size: 12px;
  color: #6b7280;
}

.ranking-stats {
  text-align: right;
}

.stat-value {
  display: block;
  font-size: 16px;
  font-weight: 700;
  color: #667eea;
}

.stat-label {
  font-size: 12px;
  color: #9ca3af;
}
</style>
