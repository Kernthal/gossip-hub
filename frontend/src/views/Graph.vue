<template>
  <div class="graph">
    <h1 class="graph-title">关系图谱</h1>

    <div class="graph-tabs">
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

    <div class="graph-container">
      <LiquidGlass variant="card">
        <div class="graph-canvas">
          <div v-if="loading" class="graph-loading">
            <Loader type="morph" />
          </div>
          <div v-else class="graph-placeholder">
            <SVGMorph shape="blob" :size="100" color1="#667eea" color2="#764ba2" />
            <p>关系图谱可视化</p>
            <p class="placeholder-text">点击节点查看详细信息</p>
          </div>
        </div>
      </LiquidGlass>
    </div>

    <div class="graph-details">
      <LiquidGlass variant="card">
        <div class="details-content">
          <h3>关系详情</h3>
          <p>点击节点查看详细信息</p>
        </div>
      </LiquidGlass>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import LiquidGlass from '../components/LiquidGlass.vue'
import SVGMorph from '../components/SVGMorph.vue'
import Loader from '../components/Loader.vue'

const tabs = [
  { key: 'all', label: '全部关系' },
  { key: 'cp', label: 'CP关系' },
  { key: 'friend', label: '朋友关系' },
  { key: 'custom', label: '自定义' }
]

const activeTab = ref('all')
const loading = ref(true)

// TODO: 初始化 D3.js 关系图谱
</script>

<style scoped>
.graph {
  max-width: 1000px;
  margin: 0 auto;
  padding: 40px 24px;
}

.graph-title {
  font-size: 36px;
  font-weight: 800;
  color: white;
  text-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
  margin-bottom: 32px;
}

.graph-tabs {
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

.graph-container {
  margin-bottom: 32px;
}

.graph-canvas {
  height: 400px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.graph-loading {
  display: flex;
  justify-content: center;
}

.graph-placeholder {
  text-align: center;
  color: #6b7280;
}

.graph-placeholder p {
  margin-top: 16px;
  font-size: 16px;
}

.placeholder-text {
  font-size: 14px;
  color: #9ca3af;
}

.details-content {
  padding: 20px;
}

.details-content h3 {
  font-size: 18px;
  font-weight: 700;
  color: #1f2937;
  margin-bottom: 8px;
}

.details-content p {
  font-size: 14px;
  color: #6b7280;
}
</style>
