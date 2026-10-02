<template>
  <div class="glass-slider">
    <input
      type="range"
      :value="modelValue"
      :min="min"
      :max="max"
      :step="step"
      :disabled="disabled"
      @input="onChange"
    />
    <div class="slider-track">
      <div class="slider-fill" :style="{ width: fillWidth + '%' }"></div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  modelValue: {
    type: Number,
    default: 0
  },
  min: {
    type: Number,
    default: 0
  },
  max: {
    type: Number,
    default: 100
  },
  step: {
    type: Number,
    default: 1
  },
  disabled: {
    type: Boolean,
    default: false
  }
})

const emit = defineEmits(['update:modelValue'])

const fillWidth = computed(() => {
  return ((props.modelValue - props.min) / (props.max - props.min)) * 100
})

function onChange(e) {
  emit('update:modelValue', Number(e.target.value))
}
</script>

<style scoped>
.glass-slider {
  position: relative;
  width: 100%;
  height: 28px;
  display: flex;
  align-items: center;
}

.glass-slider input {
  position: absolute;
  width: 100%;
  height: 100%;
  opacity: 0;
  cursor: pointer;
  z-index: 2;
}

.slider-track {
  position: relative;
  width: 100%;
  height: 6px;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 3px;
  overflow: hidden;
}

.slider-fill {
  height: 100%;
  background: linear-gradient(90deg, #667eea, #764ba2);
  border-radius: 3px;
  transition: width 0.1s ease;
}

.glass-slider::after {
  content: '';
  position: absolute;
  top: 50%;
  left: 0;
  width: 16px;
  height: 16px;
  border-radius: 50%;
  background: white;
  transform: translate(-50%, -50%);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
  transition: left 0.1s ease;
  pointer-events: none;
}
</style>
