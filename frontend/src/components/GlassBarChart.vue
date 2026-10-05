<template>
  <div class="glass-bar-chart">
    <div class="bar-header">
      <h3 class="bar-title">{{ title }}</h3>
    </div>
    <div class="bar-chart">
      <div v-for="(item, index) in data" :key="index" class="bar-item">
        <div class="bar-wrapper">
          <div
            class="bar-fill"
            :style="{
              height: (item.value / maxValue * 100) + '%',
              background: `linear-gradient(180deg, ${colors[index % colors.length]}, ${colors[index % colors.length]}88)`
            }"
          >
            <span class="bar-value">{{ item.value }}</span>
          </div>
        </div>
        <span class="bar-label">{{ item.label }}</span>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  title: {
    type: String,
    default: '柱状图'
  },
  data: {
    type: Array,
    default: () => []
  },
  colors: {
    type: Array,
    default: () => ['#667eea', '#764ba2', '#f093fb', '#4facfe', '#00f2fe']
  },
  maxValue: {
    type: Number,
    default: 100
  }
})
</script>

<style scoped>
.glass-bar-chart {
  padding: 24px;
}

.bar-header {
  margin-bottom: 20px;
}

.bar-title {
  font-size: 18px;
  font-weight: 700;
  color: white;
  margin: 0;
}

.bar-chart {
  display: flex;
  align-items: flex-end;
  gap: 16px;
  height: 200px;
  padding: 20px 0;
}

.bar-item {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
}

.bar-wrapper {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: flex-end;
}

.bar-fill {
  width: 100%;
  border-radius: 8px 8px 0 0;
  position: relative;
  transition: all 0.3s ease;
  min-height: 4px;
}

.bar-fill:hover {
  opacity: 0.8;
  transform: scaleY(1.02);
}

.bar-value {
  position: absolute;
  top: -24px;
  left: 50%;
  transform: translateX(-50%);
  font-size: 12px;
  font-weight: 600;
  color: white;
}

.bar-label {
  font-size: 12px;
  color: rgba(255, 255, 255, 0.6);
  text-align: center;
}
</style>
