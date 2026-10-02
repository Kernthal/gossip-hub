<template>
  <div class="glass-chart">
    <div class="chart-header">
      <h3 class="chart-title">{{ title }}</h3>
      <div class="chart-legend">
        <div v-for="item in legend" :key="item.label" class="legend-item">
          <span class="legend-color" :style="{ background: item.color }"></span>
          <span class="legend-label">{{ item.label }}</span>
        </div>
      </div>
    </div>
    <div class="chart-body">
      <canvas ref="canvasRef"></canvas>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import { Chart, registerables } from 'chart.js'

Chart.register(...registerables)

const props = defineProps({
  title: {
    type: String,
    default: ''
  },
  type: {
    type: String,
    default: 'bar',
    validator: (v) => ['bar', 'line', 'pie', 'doughnut', 'radar'].includes(v)
  },
  data: {
    type: Object,
    required: true
  },
  options: {
    type: Object,
    default: () => ({})
  }
})

const canvasRef = ref(null)
let chart = null

const legend = ref([])

onMounted(() => {
  initChart()
})

watch(() => props.data, () => {
  updateChart()
}, { deep: true })

function initChart() {
  if (!canvasRef.value) return

  const ctx = canvasRef.value.getContext('2d')

  chart = new Chart(ctx, {
    type: props.type,
    data: props.data,
    options: {
      responsive: true,
      maintainAspectRatio: false,
      ...props.options
    }
  })

  updateLegend()
}

function updateChart() {
  if (!chart) return

  chart.data = props.data
  chart.update()
  updateLegend()
}

function updateLegend() {
  if (!chart || !chart.data.datasets) return

  legend.value = chart.data.datasets.map((dataset, index) => ({
    label: dataset.label,
    color: Array.isArray(dataset.backgroundColor) ? dataset.backgroundColor[0] : dataset.backgroundColor
  }))
}
</script>

<style scoped>
.glass-chart {
  padding: 20px;
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  border-radius: 12px;
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.chart-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 16px;
}

.chart-title {
  font-size: 16px;
  font-weight: 600;
  color: white;
}

.chart-legend {
  display: flex;
  gap: 12px;
}

.legend-item {
  display: flex;
  align-items: center;
  gap: 6px;
}

.legend-color {
  width: 12px;
  height: 12px;
  border-radius: 3px;
}

.legend-label {
  font-size: 12px;
  color: rgba(255, 255, 255, 0.7);
}

.chart-body {
  height: 300px;
  position: relative;
}
</style>
