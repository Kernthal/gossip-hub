<template>
  <div class="glass-grid" :style="{ gridTemplateColumns: `repeat(${columns}, 1fr)` }">
    <slot></slot>
  </div>
</template>

<script setup>
defineProps({
  columns: {
    type: Number,
    default: 3
  }
})
</script>

<style scoped>
.glass-grid {
  display: grid;
  gap: 20px;
}

@media (max-width: 768px) {
  .glass-grid {
    grid-template-columns: 1fr !important;
  }
}

@media (max-width: 1024px) {
  .glass-grid {
    grid-template-columns: repeat(2, 1fr) !important;
  }
}
</style>
