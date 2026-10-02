<template>
  <div class="glass-divider" :class="`glass-divider--${orientation}`">
    <div class="divider-line"></div>
    <span v-if="text" class="divider-text">{{ text }}</span>
    <div class="divider-line"></div>
  </div>
</template>

<script setup>
defineProps({
  text: {
    type: String,
    default: ''
  },
  orientation: {
    type: String,
    default: 'horizontal',
    validator: (v) => ['horizontal', 'vertical'].includes(v)
  }
})
</script>

<style scoped>
.glass-divider {
  display: flex;
  align-items: center;
  gap: 12px;
}

.glass-divider--horizontal {
  flex-direction: row;
}

.glass-divider--vertical {
  flex-direction: column;
}

.divider-line {
  flex: 1;
  height: 1px;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.3), transparent);
}

.divider-text {
  padding: 0 12px;
  font-size: 12px;
  color: rgba(255, 255, 255, 0.5);
  white-space: nowrap;
}
</style>
