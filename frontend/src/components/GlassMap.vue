<template>
  <div class="glass-map">
    <div class="map-container">
      <div ref="mapRef" class="map-canvas"></div>
      <div class="map-controls">
        <button class="map-control" @click="zoomIn">
          <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
            <path d="M8 3V13M3 8H13" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
          </svg>
        </button>
        <button class="map-control" @click="zoomOut">
          <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
            <path d="M3 8H13" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
          </svg>
        </button>
      </div>
    </div>
    <div class="map-markers">
      <div
        v-for="marker in markers"
        :key="marker.id"
        class="map-marker"
        :style="{ left: marker.x + '%', top: marker.y + '%' }"
        @click="selectMarker(marker)"
      >
        <div class="marker-pin"></div>
        <div class="marker-label">{{ marker.label }}</div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const props = defineProps({
  markers: {
    type: Array,
    default: () => []
  },
  center: {
    type: Object,
    default: () => ({ x: 50, y: 50 })
  },
  zoom: {
    type: Number,
    default: 1
  }
})

const emit = defineEmits(['select-marker'])

const mapRef = ref(null)
const currentZoom = ref(props.zoom)

onMounted(() => {
  // TODO: 初始化地图
})

function zoomIn() {
  currentZoom.value = Math.min(currentZoom.value + 0.5, 3)
}

function zoomOut() {
  currentZoom.value = Math.max(currentZoom.value - 0.5, 0.5)
}

function selectMarker(marker) {
  emit('select-marker', marker)
}
</script>

<style scoped>
.glass-map {
  position: relative;
  height: 400px;
  border-radius: 12px;
  overflow: hidden;
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.map-container {
  position: relative;
  width: 100%;
  height: 100%;
}

.map-canvas {
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.1));
}

.map-controls {
  position: absolute;
  top: 16px;
  right: 16px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.map-control {
  width: 36px;
  height: 36px;
  display: flex;
  align-items: center;
  justify-content: center;
  border: none;
  border-radius: 8px;
  background: rgba(255, 255, 255, 0.9);
  color: #374151;
  cursor: pointer;
  transition: all 0.2s ease;
}

.map-control:hover {
  background: white;
}

.map-markers {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  pointer-events: none;
}

.map-marker {
  position: absolute;
  transform: translate(-50%, -100%);
  cursor: pointer;
  pointer-events: auto;
}

.marker-pin {
  width: 24px;
  height: 24px;
  border-radius: 50% 50% 50% 0;
  background: linear-gradient(135deg, #667eea, #764ba2);
  transform: rotate(-45deg);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
  transition: all 0.2s ease;
}

.map-marker:hover .marker-pin {
  transform: rotate(-45deg) scale(1.2);
}

.marker-label {
  position: absolute;
  bottom: 100%;
  left: 50%;
  transform: translateX(-50%);
  padding: 4px 8px;
  background: rgba(0, 0, 0, 0.8);
  color: white;
  font-size: 12px;
  border-radius: 4px;
  white-space: nowrap;
  margin-bottom: 8px;
  opacity: 0;
  transition: opacity 0.2s ease;
}

.map-marker:hover .marker-label {
  opacity: 1;
}
</style>
