<template>
  <span class="glass-tag" :class="`glass-tag--${variant}`">
    <slot></slot>
    <button v-if="closable" class="tag-close" @click="onClose">
      <svg width="12" height="12" viewBox="0 0 12 12" fill="none">
        <path d="M9 3L3 9M3 3L9 9" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
      </svg>
    </button>
  </span>
</template>

<script setup>
defineProps({
  variant: {
    type: String,
    default: 'primary',
    validator: (v) => ['primary', 'secondary', 'success', 'warning', 'danger'].includes(v)
  },
  closable: {
    type: Boolean,
    default: false
  }
})

const emit = defineEmits(['close'])

function onClose() {
  emit('close')
}
</script>

<style scoped>
.glass-tag {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 4px 12px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 600;
}

.glass-tag--primary {
  background: rgba(102, 126, 234, 0.2);
  color: #667eea;
}

.glass-tag--secondary {
  background: rgba(240, 147, 251, 0.2);
  color: #f093fb;
}

.glass-tag--success {
  background: rgba(16, 185, 129, 0.2);
  color: #10b981;
}

.glass-tag--warning {
  background: rgba(245, 158, 11, 0.2);
  color: #f59e0b;
}

.glass-tag--danger {
  background: rgba(239, 68, 68, 0.2);
  color: #ef4444;
}

.tag-close {
  background: none;
  border: none;
  color: inherit;
  cursor: pointer;
  padding: 2px;
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0.7;
  transition: opacity 0.2s;
}

.tag-close:hover {
  opacity: 1;
}
</style>
