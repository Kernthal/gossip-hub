<template>
  <div class="ranking">
    <h1 class="ranking-title">热度排行</h1>

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

    <div class="ranking-content">
      <div v-if="loading" class="ranking-loading">
        <Loader type="orbit" />
      </div>
      <div v-else-if="rankings.length === 0" class="ranking-empty">
        <EmptyState title="暂无排行数据" description="还没有足够的八卦数据" />
      </div>
      <div v-else class="ranking-list">
        <LiquidGlass v-for="(item, index) in rankings" :key="item.id" variant="card">
          <div class="ranking-item">
            <div class="ranking-position" :class="{ 'top-3': index < 3 }">
              {{ index + 1 }}
            </div>
            <div class="ranking-info">
              <h3 class="ranking-item-title">{{ item.title }}</h3>
              <p class="ranking-item-desc">{{ item.description }}</p>
            </div>
            <div class="ranking-stats">
              <span class="stat">{{ item.views }} 浏览</span>
            </div>
          </div>
        </LiquidGlass>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import LiquidGlass from '../components/LiquidGlass.vue'
import Loader from '../components/Loader.vue'
import EmptyState from '../components/EmptyState.vue'

const tabs = [
  { key: 'most_viewed', label: '浏览最多' },
  { key: 'hot', label: '热点' },
  { key: 'latest', label: '最新' }
]

const activeTab = ref('most_viewed')
const rankings = ref([])
const loading = ref(true)

onMounted(async () => {
  // TODO: 从 API 获取排行数据
  setTimeout(() => {
    loading.value = false
    rankings.value = []
  }, 1000)
})
</script>

<style scoped>
.ranking {
  max-width: 800px;
  margin: 0 auto;
  padding: 40px 24px;
}

.ranking-title {
  font-size: 36px;
  font-weight: 800;
  color: white;
  text-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
  margin-bottom: 32px;
}

.ranking-tabs {
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

.ranking-loading {
  display: flex;
  justify-content: center;
  padding: 60px;
}

.ranking-empty {
  padding: 60px;
}

.ranking-list {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.ranking-item {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 16px;
}

.ranking-position {
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.1);
  color: rgba(255, 255, 255, 0.7);
  font-size: 18px;
  font-weight: 700;
}

.ranking-position.top-3 {
  background: linear-gradient(135deg, #ffd700, #ffaa00);
  color: white;
}

.ranking-info {
  flex: 1;
}

.ranking-item-title {
  font-size: 16px;
  font-weight: 600;
  color: #1f2937;
  margin-bottom: 4px;
}

.ranking-item-desc {
  font-size: 14px;
  color: #6b7280;
}

.ranking-stats {
  display: flex;
  gap: 12px;
}

.stat {
  font-size: 14px;
  color: #9ca3af;
}
</style>
