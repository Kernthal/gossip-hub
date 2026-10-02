<template>
  <Teleport to="body">
    <Transition name="glass-modal">
      <div v-if="modelValue" class="glass-modal-overlay" @click="onOverlayClick">
        <div class="glass-modal" @click.stop>
          <div class="glass-modal__header">
            <h3 class="glass-modal__title">{{ title }}</h3>
            <button class="glass-modal__close" @click="onClose">
              <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
                <path d="M15 5L5 15M5 5L15 15" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
              </svg>
            </button>
          </div>
          <div class="glass-modal__body">
            <slot></slot>
          </div>
          <div v-if="$slots.footer" class="glass-modal__footer">
            <slot name="footer"></slot>
          </div>
        </div>
      </div>
    </Transition>
  </Teleport>
</template>

<script setup>
import { watch } from 'vue'

const props = defineProps({
  modelValue: {
    type: Boolean,
    default: false
  },
  title: {
    type: String,
    default: ''
  },
  closeOnOverlay: {
    type: Boolean,
    default: true
  }
})

const emit = defineEmits(['update:modelValue', 'close'])

function onClose() {
  emit('update:modelValue', false)
  emit('close')
}

function onOverlayClick() {
  if (props.closeOnOverlay) {
    onClose()
  }
}

watch(() => props.modelValue, (val) => {
  if (val) {
    document.body.style.overflow = 'hidden'
  } else {
    document.body.style.overflow = ''
  }
})
</script>

<style scoped>
.glass-modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.4);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  padding: 20px;
}

.glass-modal {
  background: rgba(255, 255, 255, 0.85);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border-radius: 24px;
  border: 1px solid rgba(255, 255, 255, 0.3);
  box-shadow: inset 0 0 2px 1px rgba(255, 255, 255, 0.5), inset 0 0 10px 4px rgba(255, 255, 255, 0.2), inset 0 4px 16px rgba(17, 17, 26, 0.05), inset 0 8px 24px rgba(17, 17, 26, 0.05), inset 0 6px 56px rgba(17, 17, 26, 0.05), 0 25px 50px -12px rgba(0, 0, 0, 0.25);
  max-height: 90vh;
  display: flex;
  flex-direction: column;
  overflow: hidden;
  width: 100%;
  max-width: 500px;
}

.glass-modal__header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 20px 24px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.3);
}

.glass-modal__title {
  margin: 0;
  font-size: 20px;
  font-weight: 700;
  color: #1f2937;
}

.glass-modal__close {
  background: none;
  border: none;
  cursor: pointer;
  padding: 4px;
  color: #9ca3af;
  transition: color 0.2s;
}

.glass-modal__close:hover {
  color: #4b5563;
}

.glass-modal__body {
  padding: 24px;
  overflow-y: auto;
  flex: 1;
}

.glass-modal__footer {
  padding: 16px 24px;
  border-top: 1px solid rgba(255, 255, 255, 0.3);
  display: flex;
  justify-content: flex-end;
  gap: 12px;
}

/* Transitions */
.glass-modal-enter-active,
.glass-modal-leave-active {
  transition: opacity 0.3s ease;
}

.glass-modal-enter-active .glass-modal,
.glass-modal-leave-active .glass-modal {
  transition: all 0.3s ease;
}

.glass-modal-enter-from,
.glass-modal-leave-to {
  opacity: 0;
}

.glass-modal-enter-from .glass-modal,
.glass-modal-leave-to .glass-modal {
  transform: scale(0.9) translateY(20px);
}
</style>
