<template>
  <div class="glass-radar">
    <div class="radar-header">
      <h3 class="radar-title">{{ title }}</h3>
    </div>
    <div class="radar-chart">
      <svg :width="size" :height="size" :viewBox="`0 0 ${size} ${size}`">
        <!-- Background circles -->
        <circle
          v-for="i in 5"
          :key="i"
          :cx="center"
          :cy="center"
          :r="(i / 5) * maxRadius"
          fill="none"
          stroke="rgba(255, 255, 255, 0.1)"
          stroke-width="1"
        />
        <!-- Axis lines -->
        <line
          v-for="(axis, index) in axes"
          :key="index"
          :x1="center"
          :y1="center"
          :x2="getPoint(index, maxRadius).x"
          :y2="getPoint(index, maxRadius).y"
          stroke="rgba(255, 255, 255, 0.1)"
          stroke-width="1"
        />
        <!-- Data polygon -->
        <polygon
          :points="dataPoints"
          fill="rgba(102, 126, 234, 0.3)"
          stroke="#667eea"
          stroke-width="2"
        />
        <!-- Data points -->
        <circle
          v-for="(point, index) in dataPointsArray"
          :key="index"
          :cx="point.x"
          :cy="point.y"
          r="4"
          fill="#667eea"
        />
        <!-- Labels -->
        <text
          v-for="(axis, index) in axes"
          :key="index"
          :x="getLabelPoint(index).x"
          :y="getLabelPoint(index).y"
          fill="rgba(255, 255, 255, 0.7)"
          font-size="12"
          text-anchor="middle"
          dominant-baseline="middle"
        >
          {{ axis }}
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
    default: '雷达图'
  },
  axes: {
    type: Array,
    default: () => ['A', 'B', 'C', 'D', 'E']
  },
  values: {
    type: Array,
    default: () => [80, 60, 90, 70, 50]
  },
  maxValue: {
    type: Number,
    default: 100
  },
  size: {
    type: Number,
    default: 300
  }
})

const center = computed(() => props.size / 2)
const maxRadius = computed(() => props.size / 2 - 40)

function getPoint(index, radius) {
  const angle = (index * 2 * Math.PI / props.axes.length) - Math.PI / 2
  return {
    x: center.value + radius * Math.cos(angle),
    y: center.value + radius * Math.sin(angle)
  }
}

function getLabelPoint(index) {
  const angle = (index * 2 * Math.PI / props.axes.length) - Math.PI / 2
  return {
    x: center.value + (maxRadius.value + 20) * Math.cos(angle),
    y: center.value + (maxRadius.value + 20) * Math.sin(angle)
  }
}

const dataPointsArray = computed(() => {
  return props.values.map((value, index) => {
    const radius = (value / props.maxValue) * maxRadius.value
    return getPoint(index, radius)
  })
})

const dataPoints = computed(() => {
  return dataPointsArray.value.map(p => `${p.x},${p.y}`).join(' ')
})
</script>

<style scoped>
.glass-radar {
  padding: 24px;
}

.radar-header {
  margin-bottom: 20px;
}

.radar-title {
  font-size: 18px;
  font-weight: 700;
  color: white;
  margin: 0;
}

.radar-chart {
  display: flex;
  justify-content: center;
}
</style>
