<template>
  <div class="glass-pie-chart">
    <div class="pie-header">
      <h3 class="pie-title">{{ title }}</h3>
    </div>
    <div class="pie-chart">
      <svg :width="size" :height="size" :viewBox="`0 0 ${size} ${size}`">
        <circle
          v-for="(slice, index) in slices"
          :key="index"
          :cx="center"
          :cy="center"
          :r="radius"
          :fill="slice.color"
          :stroke="strokeColor"
          :stroke-width="strokeWidth"
          :stroke-dasharray="`${slice.length} ${circumference}`"
          :stroke-dashoffset="slice.offset"
          :transform="`rotate(-90 ${center} ${center})`"
        />
        <circle
          :cx="center"
          :cy="center"
          :r="radius * 0.6"
          fill="rgba(0, 0, 0, 0.3)"
        />
        <text
          :x="center"
          :y="center"
          fill="white"
          font-size="24"
          font-weight="700"
          text-anchor="middle"
          dominant-baseline="middle"
        >
          {{ total }}
        </text>
      </svg>
    </div>
    <div class="pie-legend">
      <div v-for="(item, index) in data" :key="index" class="legend-item">
        <span class="legend-color" :style="{ background: colors[index % colors.length] }"></span>
        <span class="legend-label">{{ item.label }}</span>
        <span class="legend-value">{{ item.value }}</span>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  title: {
    type: String,
    default: '饼图'
  },
  data: {
    type: Array,
    default: () => []
  },
  colors: {
    type: Array,
    default: () => ['#667eea', '#764ba2', '#f093fb', '#4facfe', '#00f2fe']
  },
  size: {
    type: Number,
    default: 200
  },
  strokeColor: {
    type: String,
    default: 'transparent'
  },
  strokeWidth: {
    type: Number,
    default: 0
  }
})

const center = computed(() => props.size / 2)
const radius = computed(() => props.size / 2 - 10)
const circumference = computed(() => 2 * Math.PI * radius.value)
const total = computed(() => props.data.reduce((sum, item) => sum + item.value, 0))

const slices = computed(() => {
  let offset = 0
  return props.data.map((item, index) => {
    const length = (item.value / total.value) * circumference.value
    const slice = {
      color: props.colors[index % props.colors.length],
      length,
      offset: -offset
    }
    offset += length
    return slice
  })
})
</script>

<style scoped>
.glass-pie-chart {
  padding: 24px;
}

.pie-header {
  margin-bottom: 20px;
}

.pie-title {
  font-size: 18px;
  font-weight: 700;
  color: white;
  margin: 0;
}

.pie-chart {
  display: flex;
  justify-content: center;
  margin-bottom: 20px;
}

.pie-legend {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.legend-item {
  display: flex;
  align-items: center;
  gap: 8px;
}

.legend-color {
  width: 12px;
  height: 12px;
  border-radius: 3px;
}

.legend-label {
  flex: 1;
  font-size: 14px;
  color: rgba(255, 255, 255, 0.7);
}

.legend-value {
  font-size: 14px;
  font-weight: 600;
  color: white;
}
</style>
