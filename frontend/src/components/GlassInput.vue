<template>
  <div class="glass-input" :class="{ 'is-focused': isFocused, 'has-value': modelValue }">
    <input
      :type="type"
      :value="modelValue"
      :placeholder="placeholder"
      :disabled="disabled"
      @input="onInput"
      @focus="onFocus"
      @blur="onBlur"
    />
    <label v-if="label" class="glass-input__label">{{ label }}</label>
    <div class="glass-input__line"></div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const props = defineProps({
  modelValue: {
    type: String,
    default: ''
  },
  type: {
    type: String,
    default: 'text'
  },
  placeholder: {
    type: String,
    default: ''
  },
  label: {
    type: String,
    default: ''
  },
  disabled: {
    type: Boolean,
    default: false
  }
})

const emit = defineEmits(['update:modelValue', 'focus', 'blur'])

const isFocused = ref(false)

function onInput(e) {
  emit('update:modelValue', e.target.value)
}

function onFocus() {
  isFocused.value = true
  emit('focus')
}

function onBlur() {
  isFocused.value = false
  emit('blur')
}
</script>

<style scoped>
.glass-input {
  position: relative;
  display: flex;
  flex-direction: column;
}

.glass-input input {
  width: 100%;
  padding: 16px 0;
  border: none;
  background: transparent;
  font-size: 16px;
  color: #1f2937;
  outline: none;
}

.glass-input input::placeholder {
  color: transparent;
}

.glass-input__label {
  position: absolute;
  left: 0;
  top: 16px;
  font-size: 16px;
  color: #9ca3af;
  pointer-events: none;
  transition: all 0.3s ease;
}

.glass-input.is-focused .glass-input__label,
.glass-input.has-value .glass-input__label {
  top: -8px;
  font-size: 12px;
  color: #667eea;
}

.glass-input__line {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 2px;
  background: #e5e7eb;
  border-radius: 1px;
  overflow: hidden;
}

.glass-input__line::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, #667eea, #764ba2);
  transform: scaleX(0);
  transform-origin: left;
  transition: transform 0.3s ease;
}

.glass-input.is-focused .glass-input__line::after {
  transform: scaleX(1);
}
</style>
