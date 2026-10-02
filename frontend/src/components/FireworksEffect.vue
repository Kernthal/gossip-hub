<template>
  <div ref="containerRef" class="fireworks-container"></div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { Fireworks } from 'fireworks-js'

const containerRef = ref(null)
let fireworks = null

onMounted(() => {
  if (containerRef.value) {
    fireworks = new Fireworks(containerRef.value, {
      opacity: 0.9,
      acceleration: 1.05,
      friction: 0.97,
      gravity: 1.5,
      particles: 50,
      traceLength: 3,
      traceSpeed: 10,
      explosion: 5,
      intensity: 30,
      flickering: 50,
      lineStyle: 'round',
      hue: {
        min: 0,
        max: 360
      },
      delay: {
        min: 30,
        max: 60
      },
      rocketsPoint: {
        min: 50,
        max: 50
      },
      sound: {
        enabled: false,
        files: [
          'https://fireworks.js.org/sounds/explosion0.mp3',
          'https://fireworks.js.org/sounds/explosion1.mp3',
          'https://fireworks.js.org/sounds/explosion2.mp3'
        ],
        volume: {
          min: 4,
          max: 8
        }
      }
    })

    // Auto launch fireworks
    const launchInterval = setInterval(() => {
      if (fireworks) {
        fireworks.launch(1)
      }
    }, 3000)

    onUnmounted(() => {
      clearInterval(launchInterval)
      if (fireworks) {
        fireworks.stop()
      }
    })
  }
})

function start() {
  if (fireworks) {
    fireworks.start()
  }
}

function stop() {
  if (fireworks) {
    fireworks.stop()
  }
}

function launch(count = 1) {
  if (fireworks) {
    fireworks.launch(count)
  }
}

defineExpose({ start, stop, launch })
</script>

<style scoped>
.fireworks-container {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 100;
  pointer-events: none;
}
</style>
