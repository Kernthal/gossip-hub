<template>
  <div class="progress-bar">
    <div class="progress-bar__track">
      <div
        class="progress-bar__fill"
        :style="{ width: `${progress}%` }"
      >
        <div class="progress-bar__shine"></div>
      </div>
    </div>
    <span class="progress-bar__text">{{ progress }}%</span>
  </div>
</template>

<script setup>
import { ref, watch, onMounted } from 'vue'
import { gsap } from 'gsap'

const props = defineProps({
  value: {
    type: Number,
    default: 0
  },
  max: {
    type: Number,
    default: 100
  },
  animated: {
    type: Boolean,
    default: true
  }
})

const progress = ref(0)

onMounted(() => {
  if (props.animated) {
    gsap.to(progress, {
      value: (props.value / props.max) * 100,
      duration: 1,
      ease: 'power2.out',
      onUpdate: () => {
        progress.value = Math.round(progress.value)
      }
    })
  } else {
    progress.value = Math.round((props.value / props.max) * 100)
  }
})

watch(() => props.value, (newVal) => {
  if (props.animated) {
    gsap.to(progress, {
      value: (newVal / props.max) * 100,
      duration: 0.5,
      ease: 'power2.out',
      onUpdate: () => {
        progress.value = Math.round(progress.value)
      }
    })
  } else {
    progress.value = Math.round((newVal / props.max) * 100)
  }
})
</script>

<style scoped>
.progress-bar {
  display: flex;
  align-items: center;
  gap: 12px;
  width: 100%;
}

.progress-bar__track {
  flex: 1;
  height: 8px;
  background: rgba(0, 0, 0, 0.1);
  border-radius: 4px;
  overflow: hidden;
  position: relative;
}

.progress-bar__fill {
  height: 100%;
  background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
  border-radius: 4px;
  position: relative;
  transition: width 0.3s ease;
}

.progress-bar__shine {
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.4), transparent);
  animation: shine 2s infinite;
}

.progress-bar__text {
  font-size: 14px;
  font-weight: 600;
  color: #4b5563;
  min-width: 40px;
  text-align: right;
}

@keyframes shine {
  0% { left: -100%; }
  100% { left: 100%; }
}
</style>
