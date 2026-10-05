<template>
  <div class="glass-line-chart">
    <div class="line-header">
      <h3 class="line-title">{{ title }}</h3>
    </div>
    <div class="line-chart">
      <svg :width="width" :height="height" :viewBox="`0 0 ${width} ${height}`">
        <!-- Grid lines -->
        <line
          v-for="i in 5"
          :key="i"
          :x1="padding"
          :y1="padding + (i - 1) * (height - 2 * padding) / 4"
          :x2="width - padding"
          :y2="padding + (i - 1) * (height - 2 * padding) / 4"
          stroke="rgba(255, 255, 255, 0.1)"
          stroke-width="1"
        />
        <!-- Line -->
        <path
          :d="linePath"
          fill="none"
          :stroke="color"
          stroke-width="3"
          stroke-linecap="round"
          stroke-linejoin="round"
        />
        <!-- Area -->
        <path
          :d="areaPath"
          :fill="`url(#gradient)`"
          opacity="0.3"
        />
        <!-- Points -->
        <circle
          v-for="(point, index) in points"
          :key="index"
          :cx="point.x"
          :cy="point.y"
          r="4"
          :fill="color"
        />
        <!-- Gradient definition -->
        <defs>
          <linearGradient id="gradient" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" :stop-color="color" stop-opacity="0.5"/>
            <stop offset="100%" :stop-color="color" stop-opacity="0"/>
          </linearGradient>
        </defs>
      </svg>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  title: {
    type: String,
    default: '折线图'
  },
  data: {
    type: Array,
    default: () => []
  },
  labels: {
    type: Array,
    default: () => []
  },
  color: {
    type: String,
    default: '#667eea'
  },
  width: {
    type: Number,
    default: 400
  },
  height: {
    type: Number,
    default: 200
  }
})

const padding = 40
const maxValue = computed(() => Math.max(...props.data, 1))

const points = computed(() => {
  return props.data.map((value, index) => {
    const x = padding + (index * (props.width - 2 * padding) / (props.data.length - 1))
    const y = props.height - padding - (value / maxValue.value) * (props.height - 2 * padding)
    return { x, y }
  })
})

const linePath = computed(() => {
  return points.value.map((p, i) => `${i === 0 ? 'M' : 'L'} ${p.x} ${p.y}`).join(' ')
})

const areaPath = computed(() => {
  if (points.value.length === 0) return ''
  const first = points.value[0]
  const last = points.value[points.value.length - 1]
  return `${linePath.value} L ${last.x} ${props.height - padding} L ${first.x} ${props.height - padding} Z`
})
</script>

<style scoped>
.glass-line-chart {
  padding: 24px;
}

.line-header {
  margin-bottom: 20px;
}

.line-title {
  font-size: 18px;
  font-weight: 700;
  color: white;
  margin: 0;
}

.line-chart {
  display: flex;
  justify-content: center;
}
</style>
