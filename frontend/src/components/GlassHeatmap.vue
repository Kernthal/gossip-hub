<template>
  <div class="glass-heatmap">
    <div class="heatmap-header">
      <h3 class="heatmap-title">{{ title }}</h3>
      <div class="heatmap-legend">
        <span class="legend-label">少</span>
        <div class="legend-gradient"></div>
        <span class="legend-label">多</span>
      </div>
    </div>
    <div class="heatmap-grid">
      <div
        v-for="(cell, index) in cells"
        :key="index"
        class="heatmap-cell"
        :style="{ backgroundColor: getColor(cell.value) }"
        :title="`${cell.label}: ${cell.value}`"
      ></div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  title: {
    type: String,
    default: '热力图'
  },
  cells: {
    type: Array,
    default: () => []
  },
  maxValue: {
    type: Number,
    default: 100
  }
})

function getColor(value) {
  const ratio = Math.min(value / props.maxValue, 1)
  const r = Math.round(102 + (240 - 102) * ratio)
  const g = Math.round(126 + (147 - 126) * ratio)
  const b = Math.round(234 + (251 - 234) * ratio)
  return `rgba(${r}, ${g}, ${b}, 0.8)`
}
</script>

<style scoped>
.glass-heatmap {
  padding: 24px;
}

.heatmap-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 20px;
}

.heatmap-title {
  font-size: 18px;
  font-weight: 700;
  color: white;
  margin: 0;
}

.heatmap-legend {
  display: flex;
  align-items: center;
  gap: 8px;
}

.legend-label {
  font-size: 12px;
  color: rgba(255, 255, 255, 0.5);
}

.legend-gradient {
  width: 60px;
  height: 8px;
  border-radius: 4px;
  background: linear-gradient(90deg, rgba(102, 126, 234, 0.3), rgba(240, 147, 251, 0.8));
}

.heatmap-grid {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  gap: 4px;
}

.heatmap-cell {
  aspect-ratio: 1;
  border-radius: 4px;
  transition: all 0.2s ease;
}

.heatmap-cell:hover {
  transform: scale(1.1);
  z-index: 1;
}
</style>
