<template>
  <div class="glass-carousel">
    <div class="carousel-container" @mouseenter="pause" @mouseleave="resume">
      <div class="carousel-track" :style="{ transform: `translateX(-${currentIndex * 100}%)` }">
        <div v-for="(item, index) in items" :key="index" class="carousel-slide">
          <slot :item="item" :index="index"></slot>
        </div>
      </div>
      <button class="carousel-button prev" @click="prev" :disabled="currentIndex === 0">
        <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
          <path d="M12 4L6 10L12 16" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
      </button>
      <button class="carousel-button next" @click="next" :disabled="currentIndex === items.length - 1">
        <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
          <path d="M8 4L14 10L8 16" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
      </button>
    </div>
    <div class="carousel-indicators">
      <button
        v-for="(item, index) in items"
        :key="index"
        class="indicator"
        :class="{ 'is-active': currentIndex === index }"
        @click="goTo(index)"
      ></button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const props = defineProps({
  items: {
    type: Array,
    required: true
  },
  autoplay: {
    type: Boolean,
    default: true
  },
  interval: {
    type: Number,
    default: 3000
  }
})

const currentIndex = ref(0)
let autoplayInterval = null

onMounted(() => {
  if (props.autoplay) {
    startAutoplay()
  }
})

onUnmounted(() => {
  stopAutoplay()
})

function startAutoplay() {
  autoplayInterval = setInterval(() => {
    next()
  }, props.interval)
}

function stopAutoplay() {
  if (autoplayInterval) {
    clearInterval(autoplayInterval)
    autoplayInterval = null
  }
}

function pause() {
  stopAutoplay()
}

function resume() {
  if (props.autoplay) {
    startAutoplay()
  }
}

function prev() {
  if (currentIndex.value > 0) {
    currentIndex.value--
  }
}

function next() {
  if (currentIndex.value < props.items.length - 1) {
    currentIndex.value++
  } else {
    currentIndex.value = 0
  }
}

function goTo(index) {
  currentIndex.value = index
}
</script>

<style scoped>
.glass-carousel {
  position: relative;
}

.carousel-container {
  position: relative;
  overflow: hidden;
  border-radius: 12px;
}

.carousel-track {
  display: flex;
  transition: transform 0.5s ease;
}

.carousel-slide {
  flex-shrink: 0;
  width: 100%;
}

.carousel-button {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  border: none;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.9);
  color: #374151;
  cursor: pointer;
  transition: all 0.2s ease;
  z-index: 10;
}

.carousel-button:hover:not(:disabled) {
  background: white;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

.carousel-button:disabled {
  opacity: 0.3;
  cursor: not-allowed;
}

.carousel-button.prev {
  left: 16px;
}

.carousel-button.next {
  right: 16px;
}

.carousel-indicators {
  display: flex;
  justify-content: center;
  gap: 8px;
  margin-top: 16px;
}

.indicator {
  width: 8px;
  height: 8px;
  border: none;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.3);
  cursor: pointer;
  transition: all 0.2s ease;
}

.indicator:hover {
  background: rgba(255, 255, 255, 0.5);
}

.indicator.is-active {
  background: white;
  width: 24px;
  border-radius: 4px;
}
</style>
