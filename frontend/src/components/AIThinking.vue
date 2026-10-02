<template>
  <div class="ai-thinking" :class="`ai-thinking--${variant}`">
    <div class="ai-thinking__dots">
      <span class="dot"></span>
      <span class="dot"></span>
      <span class="dot"></span>
    </div>
    <span v-if="text" class="ai-thinking__text">{{ text }}</span>
  </div>
</template>

<script setup>
defineProps({
  variant: {
    type: String,
    default: 'default',
    validator: (v) => ['default', 'bounce', 'wave', 'pulse', 'typing'].includes(v)
  },
  text: {
    type: String,
    default: ''
  }
})
</script>

<style scoped>
.ai-thinking {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 12px 16px;
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(10px);
  border-radius: 12px;
  border: 1px solid rgba(255, 255, 255, 0.3);
}

.ai-thinking__dots {
  display: flex;
  gap: 4px;
}

.ai-thinking__dots .dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #667eea;
}

.ai-thinking--bounce .dot {
  animation: bounce 1.4s ease-in-out infinite;
}

.ai-thinking--bounce .dot:nth-child(1) { animation-delay: 0s; }
.ai-thinking--bounce .dot:nth-child(2) { animation-delay: 0.2s; }
.ai-thinking--bounce .dot:nth-child(3) { animation-delay: 0.4s; }

.ai-thinking--wave .dot {
  animation: wave 1.4s ease-in-out infinite;
}

.ai-thinking--wave .dot:nth-child(1) { animation-delay: 0s; }
.ai-thinking--wave .dot:nth-child(2) { animation-delay: 0.2s; }
.ai-thinking--wave .dot:nth-child(3) { animation-delay: 0.4s; }

.ai-thinking--pulse .dot {
  animation: pulse 1.4s ease-in-out infinite;
}

.ai-thinking--pulse .dot:nth-child(1) { animation-delay: 0s; }
.ai-thinking--pulse .dot:nth-child(2) { animation-delay: 0.2s; }
.ai-thinking--pulse .dot:nth-child(3) { animation-delay: 0.4s; }

.ai-thinking--typing .dot {
  animation: typing 1.4s ease-in-out infinite;
}

.ai-thinking--typing .dot:nth-child(1) { animation-delay: 0s; }
.ai-thinking--typing .dot:nth-child(2) { animation-delay: 0.2s; }
.ai-thinking--typing .dot:nth-child(3) { animation-delay: 0.4s; }

.ai-thinking__text {
  font-size: 14px;
  color: #4b5563;
  font-weight: 500;
}

@keyframes bounce {
  0%, 60%, 100% { transform: translateY(0); }
  30% { transform: translateY(-10px); }
}

@keyframes wave {
  0%, 60%, 100% { transform: scale(1); opacity: 1; }
  30% { transform: scale(1.5); opacity: 0.5; }
}

@keyframes pulse {
  0%, 100% { transform: scale(1); opacity: 1; }
  50% { transform: scale(0.5); opacity: 0.5; }
}

@keyframes typing {
  0%, 60%, 100% { transform: translateY(0); opacity: 0.4; }
  30% { transform: translateY(-4px); opacity: 1; }
}
</style>
