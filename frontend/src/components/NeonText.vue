<template>
  <span class="neon-text" :class="`neon-text--${color}`">
    <slot></slot>
  </span>
</template>

<script setup>
defineProps({
  color: {
    type: String,
    default: 'blue',
    validator: (v) => ['blue', 'pink', 'purple', 'green', 'orange'].includes(v)
  }
})
</script>

<style scoped>
.neon-text {
  display: inline-block;
  font-weight: 700;
  text-shadow: 0 0 10px currentColor, 0 0 20px currentColor, 0 0 40px currentColor;
  animation: neon-pulse 2s ease-in-out infinite;
}

.neon-text--blue {
  color: #00d4ff;
}

.neon-text--pink {
  color: #ff00ff;
}

.neon-text--purple {
  color: #b026ff;
}

.neon-text--green {
  color: #00ff88;
}

.neon-text--orange {
  color: #ff6600;
}

@keyframes neon-pulse {
  0%, 100% {
    text-shadow: 0 0 10px currentColor, 0 0 20px currentColor, 0 0 40px currentColor;
  }
  50% {
    text-shadow: 0 0 5px currentColor, 0 0 10px currentColor, 0 0 20px currentColor;
  }
}
</style>
