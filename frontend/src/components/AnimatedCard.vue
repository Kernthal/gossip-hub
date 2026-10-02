<template>
  <div
    ref="cardRef"
    class="animated-card"
    :class="{ 'is-hovered': isHovered }"
    @mouseenter="onMouseEnter"
    @mouseleave="onMouseLeave"
  >
    <div class="card-glow"></div>
    <div class="card-content">
      <slot></slot>
    </div>
    <div class="card-shine"></div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { gsap } from 'gsap'

const cardRef = ref(null)
const isHovered = ref(false)

function onMouseEnter() {
  isHovered.value = true
  if (cardRef.value) {
    gsap.to(cardRef.value, {
      scale: 1.02,
      y: -5,
      duration: 0.3,
      ease: 'power2.out'
    })
    gsap.to(cardRef.value.querySelector('.card-glow'), {
      opacity: 1,
      duration: 0.3
    })
  }
}

function onMouseLeave() {
  isHovered.value = false
  if (cardRef.value) {
    gsap.to(cardRef.value, {
      scale: 1,
      y: 0,
      duration: 0.3,
      ease: 'power2.out'
    })
    gsap.to(cardRef.value.querySelector('.card-glow'), {
      opacity: 0,
      duration: 0.3
    })
  }
}
</script>

<style scoped>
.animated-card {
  position: relative;
  background: rgba(255, 255, 255, 0.95);
  border-radius: 16px;
  padding: 24px;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
  transition: box-shadow 0.3s ease;
  overflow: hidden;
}

.animated-card.is-hovered {
  box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
}

.card-glow {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: radial-gradient(circle at var(--mouse-x, 50%) var(--mouse-y, 50%), rgba(99, 102, 241, 0.15), transparent 50%);
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.3s ease;
}

.card-content {
  position: relative;
  z-index: 1;
}

.card-shine {
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.3), transparent);
  transition: left 0.5s ease;
  pointer-events: none;
}

.animated-card.is-hovered .card-shine {
  left: 100%;
}
</style>
