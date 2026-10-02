<template>
  <div class="glass-empty">
    <div class="empty-icon">
      <slot name="icon">
        <svg width="64" height="64" viewBox="0 0 64 64" fill="none">
          <circle cx="32" cy="32" r="30" stroke="rgba(255,255,255,0.2)" stroke-width="2"/>
          <path d="M32 20V32L40 36" stroke="rgba(255,255,255,0.2)" stroke-width="2" stroke-linecap="round"/>
        </svg>
      </slot>
    </div>
    <h3 class="empty-title">{{ title }}</h3>
    <p class="empty-description">{{ description }}</p>
    <div v-if="$slots.action" class="empty-action">
      <slot name="action"></slot>
    </div>
  </div>
</template>

<script setup>
defineProps({
  title: {
    type: String,
    default: '暂无数据'
  },
  description: {
    type: String,
    default: '这里什么都没有'
  }
})
</script>

<style scoped>
.glass-empty {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 60px 20px;
  text-align: center;
}

.empty-icon {
  margin-bottom: 16px;
  opacity: 0.5;
}

.empty-title {
  margin: 0 0 8px 0;
  font-size: 18px;
  font-weight: 600;
  color: rgba(255, 255, 255, 0.8);
}

.empty-description {
  margin: 0 0 24px 0;
  font-size: 14px;
  color: rgba(255, 255, 255, 0.5);
}

.empty-action {
  margin-top: 16px;
}
</style>
