<template>
  <div class="glass-card" :class="{ 'is-hovered': isHovered }" @mouseenter="isHovered = true" @mouseleave="isHovered = false">
    <div class="glass-card__shine"></div>
    <div class="glass-card__content">
      <slot></slot>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const isHovered = ref(false)
</script>

<style scoped>
.glass-card {
  position: relative;
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  border-radius: 16px;
  border: 1px solid rgba(255, 255, 255, 0.2);
  overflow: hidden;
  transition: all 0.3s ease;
}

.glass-card.is-hovered {
  background: rgba(255, 255, 255, 0.15);
  border-color: rgba(255, 255, 255, 0.3);
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
  transform: translateY(-2px);
}

.glass-card__shine {
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.1), transparent);
  transition: left 0.5s ease;
  pointer-events: none;
}

.glass-card.is-hovered .glass-card__shine {
  left: 100%;
}

.glass-card__content {
  position: relative;
  z-index: 1;
}
</style>
