<template>
  <div class="loader" :class="`loader--${type}`">
    <div v-if="type === 'spinner'" class="loader__spinner"></div>
    <div v-else-if="type === 'dots'" class="loader__dots">
      <span></span><span></span><span></span>
    </div>
    <div v-else-if="type === 'bars'" class="loader__bars">
      <span></span><span></span><span></span><span></span><span></span>
    </div>
    <div v-else-if="type === 'ring'" class="loader__ring"></div>
    <div v-else-if="type === 'ripple'" class="loader__ripple">
      <div></div><div></div>
    </div>
    <div v-else-if="type === 'skeleton'" class="loader__skeleton">
      <div class="skeleton-line"></div>
      <div class="skeleton-line"></div>
      <div class="skeleton-line short"></div>
    </div>
    <div v-else-if="type === 'progress'" class="loader__progress">
      <div class="progress-bar"></div>
    </div>
    <div v-else-if="type === 'glow'" class="loader__glow"></div>
    <div v-else-if="type === 'morph'" class="loader__morph"></div>
    <div v-else-if="type === 'orbit'" class="loader__orbit">
      <div class="orbit-ring"></div>
      <div class="orbit-ring"></div>
      <div class="orbit-ring"></div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  type: {
    type: String,
    default: 'spinner',
    validator: (v) => ['spinner', 'dots', 'bars', 'ring', 'ripple', 'skeleton', 'progress', 'glow', 'morph', 'orbit'].includes(v)
  }
})
</script>

<style scoped>
.loader {
  display: inline-flex;
  align-items: center;
  justify-content: center;
}

/* Spinner */
.loader__spinner {
  width: 40px;
  height: 40px;
  border: 3px solid rgba(102, 126, 234, 0.2);
  border-top-color: #667eea;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

/* Dots */
.loader__dots {
  display: flex;
  gap: 8px;
}

.loader__dots span {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: #667eea;
  animation: dot-bounce 1.4s ease-in-out infinite;
}

.loader__dots span:nth-child(2) { animation-delay: 0.2s; }
.loader__dots span:nth-child(3) { animation-delay: 0.4s; }

/* Bars */
.loader__bars {
  display: flex;
  gap: 4px;
  align-items: flex-end;
  height: 40px;
}

.loader__bars span {
  width: 4px;
  background: #667eea;
  border-radius: 2px;
  animation: bar-scale 1.4s ease-in-out infinite;
}

.loader__bars span:nth-child(1) { height: 60%; animation-delay: 0s; }
.loader__bars span:nth-child(2) { height: 100%; animation-delay: 0.1s; }
.loader__bars span:nth-child(3) { height: 80%; animation-delay: 0.2s; }
.loader__bars span:nth-child(4) { height: 100%; animation-delay: 0.3s; }
.loader__bars span:nth-child(5) { height: 60%; animation-delay: 0.4s; }

/* Ring */
.loader__ring {
  width: 40px;
  height: 40px;
  border: 3px solid transparent;
  border-top-color: #667eea;
  border-right-color: #764ba2;
  border-radius: 50%;
  animation: spin 1.5s linear infinite;
}

/* Ripple */
.loader__ripple {
  position: relative;
  width: 40px;
  height: 40px;
}

.loader__ripple div {
  position: absolute;
  width: 100%;
  height: 100%;
  border: 2px solid #667eea;
  border-radius: 50%;
  animation: ripple 1.5s ease-out infinite;
}

.loader__ripple div:nth-child(2) { animation-delay: 0.5s; }

/* Skeleton */
.loader__skeleton {
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.skeleton-line {
  height: 16px;
  background: linear-gradient(90deg, #e5e7eb 25%, #f3f4f6 50%, #e5e7eb 75%);
  background-size: 200% 100%;
  border-radius: 4px;
  animation: skeleton-loading 1.5s infinite;
}

.skeleton-line.short {
  width: 60%;
}

/* Progress */
.loader__progress {
  width: 200px;
  height: 4px;
  background: #e5e7eb;
  border-radius: 2px;
  overflow: hidden;
}

.progress-bar {
  height: 100%;
  background: linear-gradient(90deg, #667eea, #764ba2);
  border-radius: 2px;
  animation: progress 2s ease-in-out infinite;
}

/* Glow */
.loader__glow {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: #667eea;
  animation: glow 1.5s ease-in-out infinite;
}

/* Morph */
.loader__morph {
  width: 40px;
  height: 40px;
  background: linear-gradient(135deg, #667eea, #764ba2);
  animation: morph 2s ease-in-out infinite;
}

/* Orbit */
.loader__orbit {
  position: relative;
  width: 60px;
  height: 60px;
}

.orbit-ring {
  position: absolute;
  border: 2px solid transparent;
  border-radius: 50%;
  animation: orbit 2s linear infinite;
}

.orbit-ring:nth-child(1) {
  width: 100%;
  height: 100%;
  border-top-color: #667eea;
  animation-duration: 2s;
}

.orbit-ring:nth-child(2) {
  width: 70%;
  height: 70%;
  top: 15%;
  left: 15%;
  border-right-color: #764ba2;
  animation-duration: 1.5s;
  animation-direction: reverse;
}

.orbit-ring:nth-child(3) {
  width: 40%;
  height: 40%;
  top: 30%;
  left: 30%;
  border-bottom-color: #f093fb;
  animation-duration: 1s;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

@keyframes dot-bounce {
  0%, 60%, 100% { transform: translateY(0); }
  30% { transform: translateY(-10px); }
}

@keyframes bar-scale {
  0%, 100% { transform: scaleY(0.5); }
  50% { transform: scaleY(1); }
}

@keyframes ripple {
  0% { transform: scale(0); opacity: 1; }
  100% { transform: scale(1.5); opacity: 0; }
}

@keyframes skeleton-loading {
  0% { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}

@keyframes progress {
  0% { width: 0%; margin-left: 0; }
  50% { width: 100%; margin-left: 0; }
  100% { width: 0%; margin-left: 100%; }
}

@keyframes glow {
  0%, 100% { box-shadow: 0 0 20px rgba(102, 126, 234, 0.5); transform: scale(1); }
  50% { box-shadow: 0 0 40px rgba(102, 126, 234, 0.8); transform: scale(1.1); }
}

@keyframes morph {
  0%, 100% { border-radius: 50%; transform: rotate(0deg); }
  25% { border-radius: 10%; transform: rotate(90deg); }
  50% { border-radius: 50%; transform: rotate(180deg); }
  75% { border-radius: 10%; transform: rotate(270deg); }
}

@keyframes orbit {
  to { transform: rotate(360deg); }
}
</style>
