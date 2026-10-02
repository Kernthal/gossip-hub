<template>
  <div class="glass-error">
    <div class="error-icon">
      <svg width="48" height="48" viewBox="0 0 48 48" fill="none">
        <circle cx="24" cy="24" r="22" stroke="rgba(255,255,255,0.2)" stroke-width="2"/>
        <path d="M24 16V24L30 28" stroke="rgba(255,255,255,0.2)" stroke-width="2" stroke-linecap="round"/>
      </svg>
    </div>
    <h3 class="error-title">{{ title }}</h3>
    <p class="error-message">{{ message }}</p>
    <div v-if="$slots.action" class="error-action">
      <slot name="action"></slot>
    </div>
  </div>
</template>

<script setup>
defineProps({
  title: {
    type: String,
    default: '出错了'
  },
  message: {
    type: String,
    default: '发生了未知错误'
  }
})
</script>

<style scoped>
.glass-error {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 60px 20px;
  text-align: center;
}

.error-icon {
  margin-bottom: 16px;
  opacity: 0.5;
}

.error-title {
  margin: 0 0 8px 0;
  font-size: 20px;
  font-weight: 700;
  color: rgba(255, 255, 255, 0.8);
}

.error-message {
  margin: 0 0 24px 0;
  font-size: 14px;
  color: rgba(255, 255, 255, 0.5);
  max-width: 400px;
}

.error-action {
  margin-top: 16px;
}
</style>
