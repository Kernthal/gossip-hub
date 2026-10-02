<template>
  <div class="glass-progress">
    <div class="progress-header">
      <span class="progress-label">{{ label }}</span>
      <span class="progress-value">{{ value }}%</span>
    </div>
    <div class="progress-track">
      <div class="progress-fill" :style="{ width: value + '%' }">
        <div class="progress-shine"></div>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  label: {
    type: String,
    default: ''
  },
  value: {
    type: Number,
    default: 0
  }
})
</script>

<style scoped>
.glass-progress {
  width: 100%;
}

.progress-header {
  display: flex;
  justify-content: space-between;
  margin-bottom: 8px;
}

.progress-label {
  font-size: 14px;
  font-weight: 600;
  color: rgba(255, 255, 255, 0.8);
}

.progress-value {
  font-size: 14px;
  font-weight: 700;
  color: white;
}

.progress-track {
  width: 100%;
  height: 8px;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 4px;
  overflow: hidden;
}

.progress-fill {
  height: 100%;
  background: linear-gradient(90deg, #667eea, #764ba2);
  border-radius: 4px;
  position: relative;
  transition: width 0.3s ease;
}

.progress-shine {
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.3), transparent);
  animation: shine 2s infinite;
}

@keyframes shine {
  0% { left: -100%; }
  100% { left: 100%; }
}
</style>
