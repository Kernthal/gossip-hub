<template>
  <div class="glass-popover" ref="popoverRef">
    <div class="popover-trigger" @click="toggle">
      <slot></slot>
    </div>
    <Transition name="popover">
      <div v-if="visible" class="popover-content" :class="`popover--${position}`">
        <div class="popover-arrow"></div>
        <div class="popover-inner">
          <slot name="content"></slot>
        </div>
      </div>
    </Transition>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const props = defineProps({
  position: {
    type: String,
    default: 'bottom',
    validator: (v) => ['top', 'bottom', 'left', 'right'].includes(v)
  },
  trigger: {
    type: String,
    default: 'click',
    validator: (v) => ['click', 'hover'].includes(v)
  }
})

const visible = ref(false)
const popoverRef = ref(null)

function toggle() {
  visible.value = !visible.value
}

function show() {
  visible.value = true
}

function hide() {
  visible.value = false
}

function onClickOutside(e) {
  if (popoverRef.value && !popoverRef.value.contains(e.target)) {
    visible.value = false
  }
}

onMounted(() => {
  document.addEventListener('click', onClickOutside)
})

onUnmounted(() => {
  document.removeEventListener('click', onClickOutside)
})

defineExpose({ show, hide, toggle })
</script>

<style scoped>
.glass-popover {
  position: relative;
  display: inline-block;
}

.popover-trigger {
  display: inline-block;
}

.popover-content {
  position: absolute;
  z-index: 1000;
  padding: 12px;
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border-radius: 12px;
  border: 1px solid rgba(255, 255, 255, 0.3);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
  min-width: 200px;
}

.popover--top {
  bottom: 100%;
  left: 50%;
  transform: translateX(-50%);
  margin-bottom: 8px;
}

.popover--bottom {
  top: 100%;
  left: 50%;
  transform: translateX(-50%);
  margin-top: 8px;
}

.popover--left {
  right: 100%;
  top: 50%;
  transform: translateY(-50%);
  margin-right: 8px;
}

.popover--right {
  left: 100%;
  top: 50%;
  transform: translateY(-50%);
  margin-left: 8px;
}

.popover-arrow {
  position: absolute;
  width: 0;
  height: 0;
  border: 6px solid transparent;
}

.popover--top .popover-arrow {
  bottom: -12px;
  left: 50%;
  transform: translateX(-50%);
  border-top-color: rgba(255, 255, 255, 0.95);
}

.popover--bottom .popover-arrow {
  top: -12px;
  left: 50%;
  transform: translateX(-50%);
  border-bottom-color: rgba(255, 255, 255, 0.95);
}

.popover--left .popover-arrow {
  right: -12px;
  top: 50%;
  transform: translateY(-50%);
  border-left-color: rgba(255, 255, 255, 0.95);
}

.popover--right .popover-arrow {
  left: -12px;
  top: 50%;
  transform: translateY(-50%);
  border-right-color: rgba(255, 255, 255, 0.95);
}

.popover-inner {
  position: relative;
  z-index: 1;
}

.popover-enter-active,
.popover-leave-active {
  transition: all 0.2s ease;
}

.popover-enter-from,
.popover-leave-to {
  opacity: 0;
  transform: scale(0.9);
}
</style>
