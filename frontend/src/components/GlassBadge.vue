<template>
  <span class="glass-badge" :class="`glass-badge--${variant}`">
    <slot></slot>
  </span>
</template>

<script setup>
defineProps({
  variant: {
    type: String,
    default: 'primary',
    validator: (v) => ['primary', 'secondary', 'success', 'warning', 'danger'].includes(v)
  }
})
</script>

<style scoped>
.glass-badge {
  display: inline-flex;
  align-items: center;
  padding: 4px 12px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 600;
  text-transform: uppercase;
}

.glass-badge--primary {
  background: rgba(102, 126, 234, 0.2);
  color: #667eea;
}

.glass-badge--secondary {
  background: rgba(240, 147, 251, 0.2);
  color: #f093fb;
}

.glass-badge--success {
  background: rgba(16, 185, 129, 0.2);
  color: #10b981;
}

.glass-badge--warning {
  background: rgba(245, 158, 11, 0.2);
  color: #f59e0b;
}

.glass-badge--danger {
  background: rgba(239, 68, 68, 0.2);
  color: #ef4444;
}
</style>
