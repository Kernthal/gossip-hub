<template>
  <div class="glass-select" :class="{ 'is-open': isOpen }">
    <button class="select-trigger" @click="isOpen = !isOpen">
      <span class="select-value">{{ selectedLabel || placeholder }}</span>
      <svg width="16" height="16" viewBox="0 0 16 16" fill="none" class="select-arrow">
        <path d="M4 6L8 10L12 6" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
    </button>
    <Transition name="select">
      <div v-if="isOpen" class="select-dropdown">
        <button
          v-for="option in options"
          :key="option.value"
          class="select-option"
          :class="{ 'is-selected': modelValue === option.value }"
          @click="selectOption(option)"
        >
          {{ option.label }}
        </button>
      </div>
    </Transition>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const props = defineProps({
  modelValue: {
    type: [String, Number],
    default: ''
  },
  options: {
    type: Array,
    required: true
  },
  placeholder: {
    type: String,
    default: '请选择'
  }
})

const emit = defineEmits(['update:modelValue'])

const isOpen = ref(false)

const selectedLabel = computed(() => {
  const option = props.options.find(o => o.value === props.modelValue)
  return option ? option.label : ''
})

function selectOption(option) {
  emit('update:modelValue', option.value)
  isOpen.value = false
}
</script>

<style scoped>
.glass-select {
  position: relative;
  width: 100%;
}

.select-trigger {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 12px 16px;
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 12px;
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  color: white;
  font-size: 14px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.select-trigger:hover {
  background: rgba(255, 255, 255, 0.15);
}

.select-arrow {
  transition: transform 0.3s ease;
}

.is-open .select-arrow {
  transform: rotate(180deg);
}

.select-dropdown {
  position: absolute;
  top: 100%;
  left: 0;
  right: 0;
  margin-top: 8px;
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(20px);
  border-radius: 12px;
  border: 1px solid rgba(255, 255, 255, 0.3);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
  overflow: hidden;
  z-index: 100;
}

.select-option {
  width: 100%;
  padding: 12px 16px;
  border: none;
  background: transparent;
  color: #374151;
  font-size: 14px;
  text-align: left;
  cursor: pointer;
  transition: all 0.2s ease;
}

.select-option:hover {
  background: rgba(102, 126, 234, 0.1);
}

.select-option.is-selected {
  background: rgba(102, 126, 234, 0.2);
  color: #667eea;
  font-weight: 600;
}

.select-enter-active,
.select-leave-active {
  transition: all 0.2s ease;
}

.select-enter-from,
.select-leave-to {
  opacity: 0;
  transform: translateY(-10px);
}
</style>
