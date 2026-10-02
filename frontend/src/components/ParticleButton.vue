<template>
  <button
    ref="buttonRef"
    class="particle-button"
    :class="[`particle-button--${variant}`, { 'is-loading': loading }]"
    :disabled="disabled || loading"
    @click="onClick"
    @mouseenter="onMouseEnter"
    @mouseleave="onMouseLeave"
  >
    <span class="particle-button__text">
      <slot></slot>
    </span>
    <span class="particle-button__ripple"></span>
    <canvas ref="canvasRef" class="particle-button__canvas"></canvas>
  </button>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const props = defineProps({
  variant: {
    type: String,
    default: 'primary',
    validator: (v) => ['primary', 'secondary', 'danger', 'success'].includes(v)
  },
  disabled: {
    type: Boolean,
    default: false
  },
  loading: {
    type: Boolean,
    default: false
  }
})

const emit = defineEmits(['click'])

const buttonRef = ref(null)
const canvasRef = ref(null)
let particles = []
let animationId = null

onMounted(() => {
  initParticles()
})

onUnmounted(() => {
  if (animationId) {
    cancelAnimationFrame(animationId)
  }
})

function initParticles() {
  const canvas = canvasRef.value
  if (!canvas) return

  const ctx = canvas.getContext('2d')
  const rect = canvas.parentElement.getBoundingClientRect()
  canvas.width = rect.width
  canvas.height = rect.height

  particles = []
  for (let i = 0; i < 20; i++) {
    particles.push(createParticle(canvas.width, canvas.height))
  }

  animate(ctx, canvas)
}

function createParticle(width, height) {
  return {
    x: Math.random() * width,
    y: height + Math.random() * 10,
    vx: (Math.random() - 0.5) * 0.5,
    vy: -Math.random() * 2 - 1,
    size: Math.random() * 3 + 1,
    opacity: Math.random() * 0.5 + 0.2,
    color: `hsl(${Math.random() * 60 + 200}, 70%, 60%)`
  }
}

function animate(ctx, canvas) {
  animationId = requestAnimationFrame(() => animate(ctx, canvas))
  ctx.clearRect(0, 0, canvas.width, canvas.height)

  particles.forEach((p, index) => {
    p.x += p.vx
    p.y += p.vy
    p.opacity -= 0.005

    if (p.opacity <= 0 || p.y < -10) {
      particles[index] = createParticle(canvas.width, canvas.height)
    }

    ctx.beginPath()
    ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2)
    ctx.fillStyle = p.color
    ctx.globalAlpha = p.opacity
    ctx.fill()
    ctx.globalAlpha = 1
  })
}

function onClick(e) {
  createRipple(e)
  emit('click', e)
}

function createRipple(e) {
  const button = buttonRef.value
  if (!button) return

  const ripple = button.querySelector('.particle-button__ripple')
  const rect = button.getBoundingClientRect()
  const size = Math.max(rect.width, rect.height)
  const x = e.clientX - rect.left - size / 2
  const y = e.clientY - rect.top - size / 2

  ripple.style.width = ripple.style.height = `${size}px`
  ripple.style.left = `${x}px`
  ripple.style.top = `${y}px`
  ripple.classList.add('is-active')

  setTimeout(() => {
    ripple.classList.remove('is-active')
  }, 600)
}

function onMouseEnter() {
  if (canvasRef.value) {
    const canvas = canvasRef.value
    const ctx = canvas.getContext('2d')
    for (let i = 0; i < 5; i++) {
      particles.push(createParticle(canvas.width, canvas.height))
    }
  }
}

function onMouseLeave() {
  // Particles will naturally fade out
}
</script>

<style scoped>
.particle-button {
  position: relative;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 12px 24px;
  border: none;
  border-radius: 8px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  overflow: hidden;
  transition: all 0.3s ease;
  color: white;
}

.particle-button--primary {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

.particle-button--secondary {
  background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
}

.particle-button--danger {
  background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
}

.particle-button--success {
  background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
}

.particle-button:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
}

.particle-button:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.particle-button__text {
  position: relative;
  z-index: 2;
}

.particle-button__ripple {
  position: absolute;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.3);
  transform: scale(0);
  transition: transform 0.6s ease-out;
  pointer-events: none;
}

.particle-button__ripple.is-active {
  transform: scale(4);
  transition: transform 0s;
}

.particle-button__canvas {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  z-index: 1;
}

.is-loading {
  position: relative;
}

.is-loading::after {
  content: '';
  position: absolute;
  width: 16px;
  height: 16px;
  border: 2px solid rgba(255, 255, 255, 0.3);
  border-top-color: white;
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
  right: 12px;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}
</style>
