<template>
  <div class="glass-gauge">
    <div class="gauge-header">
      <h3 class="gauge-title">{{ title }}</h3>
    </div>
    <div class="gauge-chart">
      <svg :width="size" :height="size / 2 + 20" :viewBox="`0 0 ${size} ${size / 2 + 20}`">
        <!-- Background arc -->
        <path
          :d="arcPath"
          fill="none"
          stroke="rgba(255, 255, 255, 0.1)"
          stroke-width="12"
          stroke-linecap="round"
        />
        <!-- Value arc -->
        <path
          :d="arcPath"
          fill="none"
          :stroke="color"
          stroke-width="12"
          stroke-linecap="round"
          :stroke-dasharray="`${arcLength * value / maxValue} ${arcLength}`"
        />
        <!-- Value text -->
        <text
          :x="center"
          :y="center + 10"
          fill="white"
          font-size="32"
          font-weight="700"
          text-anchor="middle"
        >
          {{ value }}
        </text>
        <!-- Label -->
        <text
          :x="center"
          :y="center + 35"
          fill="rgba(255, 255, 255, 0.5)"
          font-size="14"
          text-anchor="middle"
        >
          {{ label }}
        </text>
      </svg>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  title: {
    type: String,
    default: '仪表盘'
  },
  value: {
    type: Number,
    default: 0
  },
  maxValue: {
    type: Number,
    default: 100
  },
  label: {
    type: String,
    default: ''
  },
  color: {
    type: String,
    default: '#667eea'
  },
  size: {
    type: Number,
    default: 200
  }
})

const center = computed(() => props.size / 2)
const radius = computed(() => props.size / 2 - 20)
const arcLength = computed(() => Math.PI * radius.value)

const arcPath = computed(() => {
  const startAngle = Math.PI
  const endAngle = 2 * Math.PI
  const x1 = center.value + radius.value * Math.cos(startAngle)
  const y1 = center.value + radius.value * Math.sin(startAngle)
  const x2 = center.value + radius.value * Math.cos(endAngle)
  const y2 = center.value + radius.value * Math.sin(endAngle)
  return `M ${x1} ${y1} A ${radius.value} ${radius.value} 0 0 1 ${x2} ${y2}`
})
</script>

<style scoped>
.glass-gauge {
  padding: 24px;
}

.gauge-header {
  margin-bottom: 20px;
}

.gauge-title {
  font-size: 18px;
  font-weight: 700;
  color: white;
  margin: 0;
}

.gauge-chart {
  display: flex;
  justify-content: center;
}
</style>
