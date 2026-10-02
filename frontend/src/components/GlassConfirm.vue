<template>
  <Teleport to="body">
    <Transition name="confirm">
      <div v-if="visible" class="glass-confirm-overlay" @click="onOverlayClick">
        <div class="glass-confirm" @click.stop>
          <div class="confirm-header">
            <h3 class="confirm-title">{{ title }}</h3>
          </div>
          <div class="confirm-body">
            <p class="confirm-message">{{ message }}</p>
          </div>
          <div class="confirm-footer">
            <GlassButton variant="ghost" @click="onCancel">
              {{ cancelText }}
            </GlassButton>
            <GlassButton :variant="confirmVariant" @click="onConfirm">
              {{ confirmText }}
            </GlassButton>
          </div>
        </div>
      </div>
    </Transition>
  </Teleport>
</template>

<script setup>
import GlassButton from './GlassButton.vue'

const props = defineProps({
  visible: {
    type: Boolean,
    default: false
  },
  title: {
    type: String,
    default: '确认'
  },
  message: {
    type: String,
    default: ''
  },
  confirmText: {
    type: String,
    default: '确认'
  },
  cancelText: {
    type: String,
    default: '取消'
  },
  confirmVariant: {
    type: String,
    default: 'primary'
  },
  closeOnOverlay: {
    type: Boolean,
    default: true
  }
})

const emit = defineEmits(['confirm', 'cancel'])

function onConfirm() {
  emit('confirm')
}

function onCancel() {
  emit('cancel')
}

function onOverlayClick() {
  if (props.closeOnOverlay) {
    emit('cancel')
  }
}
</script>

<style scoped>
.glass-confirm-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.4);
  backdrop-filter: blur(4px);
  -webkit-backdrop-filter: blur(4px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  padding: 20px;
}

.glass-confirm {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border-radius: 24px;
  border: 1px solid rgba(255, 255, 255, 0.3);
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
  max-width: 400px;
  width: 100%;
  overflow: hidden;
}

.confirm-header {
  padding: 20px 24px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.3);
}

.confirm-title {
  margin: 0;
  font-size: 20px;
  font-weight: 700;
  color: #1f2937;
}

.confirm-body {
  padding: 24px;
}

.confirm-message {
  margin: 0;
  font-size: 14px;
  color: #4b5563;
  line-height: 1.6;
}

.confirm-footer {
  padding: 16px 24px;
  border-top: 1px solid rgba(255, 255, 255, 0.3);
  display: flex;
  justify-content: flex-end;
  gap: 12px;
}

.confirm-enter-active,
.confirm-leave-active {
  transition: opacity 0.3s ease;
}

.confirm-enter-active .glass-confirm,
.confirm-leave-active .glass-confirm {
  transition: all 0.3s ease;
}

.confirm-enter-from,
.confirm-leave-to {
  opacity: 0;
}

.confirm-enter-from .glass-confirm,
.confirm-leave-to .glass-confirm {
  transform: scale(0.9) translateY(20px);
}
</style>
