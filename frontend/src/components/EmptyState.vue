<template>
  <div class="empty-state">
    <div class="empty-state__icon">
      <slot name="icon">
        <svg width="64" height="64" viewBox="0 0 64 64" fill="none">
          <circle cx="32" cy="32" r="30" stroke="#e5e7eb" stroke-width="2"/>
          <path d="M32 20V32L40 36" stroke="#e5e7eb" stroke-width="2" stroke-linecap="round"/>
        </svg>
      </slot>
    </div>
    <h3 class="empty-state__title">{{ title }}</h3>
    <p class="empty-state__description">{{ description }}</p>
    <div v-if="$slots.action" class="empty-state__action">
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
.empty-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 60px 20px;
  text-align: center;
}

.empty-state__icon {
  margin-bottom: 16px;
}

.empty-state__title {
  margin: 0 0 8px 0;
  font-size: 18px;
  font-weight: 600;
  color: #4b5563;
}

.empty-state__description {
  margin: 0 0 24px 0;
  font-size: 14px;
  color: #9ca3af;
}

.empty-state__action {
  margin-top: 16px;
}
</style>
