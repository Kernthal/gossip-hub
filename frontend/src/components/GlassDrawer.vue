<template>
  <Teleport to="body">
    <Transition name="drawer">
      <div v-if="modelValue" class="glass-drawer-overlay" @click="onOverlayClick">
        <Transition name="drawer-content">
          <div v-if="modelValue" class="glass-drawer" :class="`glass-drawer--${position}`" @click.stop>
            <div class="drawer-header">
              <h3 class="drawer-title">{{ title }}</h3>
              <button class="drawer-close" @click="onClose">
                <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
                  <path d="M15 5L5 15M5 5L15 15" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
                </svg>
              </button>
            </div>
            <div class="drawer-body">
              <slot></slot>
            </div>
            <div v-if="$slots.footer" class="drawer-footer">
              <slot name="footer"></slot>
            </div>
          </div>
        </Transition>
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
  position: {
    type: String,
    default: 'right',
    validator: (v) => ['left', 'right', 'top', 'bottom'].includes(v)
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
.glass-drawer-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.4);
  backdrop-filter: blur(4px);
  -webkit-backdrop-filter: blur(4px);
  z-index: 1000;
}

.glass-drawer {
  position: absolute;
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.glass-drawer--right {
  top: 0;
  right: 0;
  width: 400px;
  height: 100%;
}

.glass-drawer--left {
  top: 0;
  left: 0;
  width: 400px;
  height: 100%;
}

.glass-drawer--top {
  top: 0;
  left: 0;
  right: 0;
  height: 300px;
}

.glass-drawer--bottom {
  bottom: 0;
  left: 0;
  right: 0;
  height: 300px;
}

.drawer-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 20px 24px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.3);
}

.drawer-title {
  margin: 0;
  font-size: 20px;
  font-weight: 700;
  color: #1f2937;
}

.drawer-close {
  background: none;
  border: none;
  cursor: pointer;
  padding: 4px;
  color: #9ca3af;
  transition: color 0.2s;
}

.drawer-close:hover {
  color: #4b5563;
}

.drawer-body {
  flex: 1;
  padding: 24px;
  overflow-y: auto;
}

.drawer-footer {
  padding: 16px 24px;
  border-top: 1px solid rgba(255, 255, 255, 0.3);
  display: flex;
  justify-content: flex-end;
  gap: 12px;
}

/* Transitions */
.drawer-enter-active,
.drawer-leave-active {
  transition: opacity 0.3s ease;
}

.drawer-enter-active .glass-drawer,
.drawer-leave-active .glass-drawer {
  transition: all 0.3s ease;
}

.drawer-enter-from,
.drawer-leave-to {
  opacity: 0;
}

.drawer-enter-from .glass-drawer--right,
.drawer-leave-to .glass-drawer--right {
  transform: translateX(100%);
}

.drawer-enter-from .glass-drawer--left,
.drawer-leave-to .glass-drawer--left {
  transform: translateX(-100%);
}

.drawer-enter-from .glass-drawer--top,
.drawer-leave-to .glass-drawer--top {
  transform: translateY(-100%);
}

.drawer-enter-from .glass-drawer--bottom,
.drawer-leave-to .glass-drawer--bottom {
  transform: translateY(100%);
}
</style>
