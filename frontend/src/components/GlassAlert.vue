<template>
  <Transition name="alert">
    <div v-if="visible" class="glass-alert" :class="`glass-alert--${type}`">
      <div class="alert-icon">
        <svg v-if="type === 'success'" width="20" height="20" viewBox="0 0 20 20" fill="none">
          <path d="M10 0C4.48 0 0 4.48 0 10C0 15.52 4.48 20 10 20C15.52 20 20 15.52 20 10C20 4.48 15.52 0 10 0ZM8 15L3 10L4.41 8.59L8 12.17L15.59 4.58L17 6L8 15Z" fill="currentColor"/>
        </svg>
        <svg v-else-if="type === 'error'" width="20" height="20" viewBox="0 0 20 20" fill="none">
          <path d="M10 0C4.48 0 0 4.48 0 10C0 15.52 4.48 20 10 20C15.52 20 20 15.52 20 10C20 4.48 15.52 0 10 0ZM15 13.59L13.59 15L10 11.41L6.41 15L5 13.59L8.59 10L5 6.41L6.41 5L10 8.59L13.59 5L15 6.41L11.41 10L15 13.59Z" fill="currentColor"/>
        </svg>
        <svg v-else-if="type === 'warning'" width="20" height="20" viewBox="0 0 20 20" fill="none">
          <path d="M10 0C4.48 0 0 4.48 0 10C0 15.52 4.48 20 10 20C15.52 20 20 15.52 20 10C20 4.48 15.52 0 10 0ZM11 15H9V13H11V15ZM11 11H9V5H11V11Z" fill="currentColor"/>
        </svg>
        <svg v-else width="20" height="20" viewBox="0 0 20 20" fill="none">
          <path d="M10 0C4.48 0 0 4.48 0 10C0 15.52 4.48 20 10 20C15.52 20 20 15.52 20 10C20 4.48 15.52 0 10 0ZM11 15H9V9H11V15ZM11 7H9V5H11V7Z" fill="currentColor"/>
        </svg>
      </div>
      <div class="alert-content">
        <p class="alert-message">{{ message }}</p>
      </div>
      <button v-if="closable" class="alert-close" @click="close">
        <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
          <path d="M12 4L4 12M4 4L12 12" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
        </svg>
      </button>
    </div>
  </Transition>
</template>

<script setup>
import { ref, watch } from 'vue'

const props = defineProps({
  type: {
    type: String,
    default: 'info',
    validator: (v) => ['success', 'error', 'warning', 'info'].includes(v)
  },
  message: {
    type: String,
    required: true
  },
  closable: {
    type: Boolean,
    default: true
  },
  duration: {
    type: Number,
    default: 0
  }
})

const emit = defineEmits(['close'])

const visible = ref(true)

watch(() => props.message, () => {
  visible.value = true
})

function close() {
  visible.value = false
  emit('close')
}
</script>

<style scoped>
.glass-alert {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 16px 20px;
  border-radius: 12px;
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.glass-alert--success {
  background: rgba(16, 185, 129, 0.2);
  border-color: rgba(16, 185, 129, 0.3);
}

.glass-alert--error {
  background: rgba(239, 68, 68, 0.2);
  border-color: rgba(239, 68, 68, 0.3);
}

.glass-alert--warning {
  background: rgba(245, 158, 11, 0.2);
  border-color: rgba(245, 158, 11, 0.3);
}

.glass-alert--info {
  background: rgba(59, 130, 246, 0.2);
  border-color: rgba(59, 130, 246, 0.3);
}

.alert-icon {
  flex-shrink: 0;
  color: white;
}

.alert-content {
  flex: 1;
}

.alert-message {
  margin: 0;
  font-size: 14px;
  color: white;
  line-height: 1.5;
}

.alert-close {
  background: none;
  border: none;
  color: rgba(255, 255, 255, 0.7);
  cursor: pointer;
  padding: 4px;
  transition: color 0.2s;
}

.alert-close:hover {
  color: white;
}

.alert-enter-active,
.alert-leave-active {
  transition: all 0.3s ease;
}

.alert-enter-from,
.alert-leave-to {
  opacity: 0;
  transform: translateY(-10px);
}
</style>
