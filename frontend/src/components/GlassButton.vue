<template>
  <button
    class="glass-button"
    :class="[`glass-button--${variant}`, { 'is-loading': loading }]"
    :disabled="disabled || loading"
    @click="onClick"
  >
    <span class="glass-button__text">
      <slot></slot>
    </span>
    <span class="glass-button__shine"></span>
  </button>
</template>

<script setup>
import { ref } from 'vue'

const props = defineProps({
  variant: {
    type: String,
    default: 'primary',
    validator: (v) => ['primary', 'secondary', 'danger', 'success', 'ghost'].includes(v)
  },
  disabled: {
    type: Boolean,
    default: false
  },
  loading: {
    type: Boolean,
    default: false
  }
})

const emit = defineEmits(['click'])

function onClick(e) {
  emit('click', e)
}
</script>

<style scoped>
.glass-button {
  position: relative;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 14px 28px;
  border: none;
  border-radius: 16px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  overflow: hidden;
  transition: all 0.3s ease;
  color: white;
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  box-shadow: inset 0 0 2px 1px rgba(255, 255, 255, 0.35), inset 0 0 10px 4px rgba(255, 255, 255, 0.15), inset 0 4px 16px rgba(17, 17, 26, 0.05), inset 0 8px 24px rgba(17, 17, 26, 0.05), inset 0 6px 56px rgba(17, 17, 26, 0.05);
}

.glass-button--primary {
  background: linear-gradient(135deg, rgba(102, 126, 234, 0.8) 0%, rgba(118, 75, 162, 0.8) 100%);
}

.glass-button--secondary {
  background: linear-gradient(135deg, rgba(240, 147, 251, 0.8) 0%, rgba(245, 87, 108, 0.8) 100%);
}

.glass-button--danger {
  background: linear-gradient(135deg, rgba(250, 112, 154, 0.8) 0%, rgba(254, 225, 64, 0.8) 100%);
}

.glass-button--success {
  background: linear-gradient(135deg, rgba(79, 172, 254, 0.8) 0%, rgba(0, 242, 254, 0.8) 100%);
}

.glass-button--ghost {
  background: rgba(255, 255, 255, 0.05);
}

.glass-button:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: inset 0 0 2px 1px rgba(255, 255, 255, 0.5), inset 0 0 10px 4px rgba(255, 255, 255, 0.2), inset 0 4px 16px rgba(17, 17, 26, 0.08), inset 0 8px 24px rgba(17, 17, 26, 0.08), inset 0 6px 56px rgba(17, 17, 26, 0.08), 0 10px 30px rgba(0, 0, 0, 0.2);
}

.glass-button:active:not(:disabled) {
  transform: translateY(0);
}

.glass-button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.glass-button__text {
  position: relative;
  z-index: 2;
}

.glass-button__shine {
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
  transition: left 0.5s ease;
  pointer-events: none;
}

.glass-button:hover .glass-button__shine {
  left: 100%;
}

.is-loading {
  position: relative;
}

.is-loading::after {
  content: '';
  position: absolute;
  width: 16px;
  height: 16px;
  border: 2px solid rgba(255, 255, 255, 0.3);
  border-top-color: white;
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
  right: 12px;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}
</style>
