<template>
  <div class="svg-morph" :class="`svg-morph--${shape}`">
    <svg :width="size" :height="size" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <linearGradient :id="`grad-${id}`" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" :stop-color="color1" />
          <stop offset="100%" :stop-color="color2" />
        </linearGradient>
        <filter :id="`glow-${id}`">
          <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
          <feMerge>
            <feMergeNode in="coloredBlur"/>
            <feMergeNode in="SourceGraphic"/>
          </feMerge>
        </filter>
      </defs>
      <path
        :d="currentPath"
        :fill="`url(#grad-${id})`"
        :filter="`url(#glow-${id})`"
        class="morph-path"
      />
    </svg>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'

const props = defineProps({
  size: {
    type: Number,
    default: 100
  },
  shape: {
    type: String,
    default: 'blob',
    validator: (v) => ['blob', 'star', 'heart', 'hexagon', 'triangle'].includes(v)
  },
  color1: {
    type: String,
    default: '#667eea'
  },
  color2: {
    type: String,
    default: '#764ba2'
  },
  animate: {
    type: Boolean,
    default: true
  }
})

const id = Math.random().toString(36).substr(2, 9)

const paths = {
  blob: [
    'M50 5C75 5 95 25 95 50C95 75 75 95 50 95C25 95 5 75 5 50C5 25 25 5 50 5Z',
    'M50 10C70 10 90 30 90 50C90 70 70 90 50 90C30 90 10 70 10 50C10 30 30 10 50 10Z',
    'M50 15C65 15 85 35 85 50C85 65 65 85 50 85C35 85 15 65 15 50C15 35 35 15 50 15Z',
  ],
  star: [
    'M50 5L61 38L95 38L68 58L79 92L50 72L21 92L32 58L5 38L39 38Z',
    'M50 10L58 35L88 35L63 53L72 85L50 68L28 85L37 53L12 35L42 35Z',
    'M50 15L55 32L80 32L60 48L67 78L50 65L33 78L40 48L20 32L45 32Z',
  ],
  heart: [
    'M50 88C20 65 5 50 5 35C5 20 15 10 30 10C40 10 47 15 50 20C53 15 60 10 70 10C85 10 95 20 95 35C95 50 80 65 50 88Z',
    'M50 80C25 60 10 48 10 35C10 22 20 15 32 15C41 15 47 19 50 24C53 19 59 15 68 15C80 15 90 22 90 35C90 48 75 60 50 80Z',
    'M50 72C30 55 15 45 15 35C15 25 23 18 33 18C41 18 47 22 50 27C53 22 59 18 67 18C77 18 85 25 85 35C85 45 70 55 50 72Z',
  ],
  hexagon: [
    'M50 5L90 27.5L90 72.5L50 95L10 72.5L10 27.5Z',
    'M50 10L85 30L85 70L50 90L15 70L15 30Z',
    'M50 15L80 32.5L80 67.5L50 85L20 67.5L20 32.5Z',
  ],
  triangle: [
    'M50 5L95 90L5 90Z',
    'M50 10L90 85L10 85Z',
    'M50 15L85 80L15 80Z',
  ]
}

const currentPathIndex = ref(0)
let interval = null

const currentPath = computed(() => {
  const shapePaths = paths[props.shape] || paths.blob
  return shapePaths[currentPathIndex.value % shapePaths.length]
})

onMounted(() => {
  if (props.animate) {
    interval = setInterval(() => {
      currentPathIndex.value = (currentPathIndex.value + 1) % 3
    }, 2000)
  }
})

onUnmounted(() => {
  if (interval) {
    clearInterval(interval)
  }
})
</script>

<style scoped>
.svg-morph {
  display: inline-flex;
  align-items: center;
  justify-content: center;
}

.morph-path {
  transition: d 1s ease-in-out;
}
</style>
