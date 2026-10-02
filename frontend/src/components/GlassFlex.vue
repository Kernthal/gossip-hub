<template>
  <div class="glass-flex" :class="`glass-flex--${direction}`" :style="{ gap: gap + 'px' }">
    <slot></slot>
  </div>
</template>

<script setup>
defineProps({
  direction: {
    type: String,
    default: 'row',
    validator: (v) => ['row', 'column'].includes(v)
  },
  gap: {
    type: Number,
    default: 16
  }
})
</script>

<style scoped>
.glass-flex {
  display: flex;
}

.glass-flex--row {
  flex-direction: row;
}

.glass-flex--column {
  flex-direction: column;
}
</style>
