<template>
  <div class="glass-textarea" :class="{ 'is-focused': isFocused }">
    <textarea
      :value="modelValue"
      :placeholder="placeholder"
      :rows="rows"
      :disabled="disabled"
      @input="onInput"
      @focus="onFocus"
      @blur="onBlur"
    ></textarea>
    <label v-if="label" class="glass-textarea__label">{{ label }}</label>
    <div class="glass-textarea__line"></div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const props = defineProps({
  modelValue: {
    type: String,
    default: ''
  },
  placeholder: {
    type: String,
    default: ''
  },
  label: {
    type: String,
    default: ''
  },
  rows: {
    type: Number,
    default: 4
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
.glass-textarea {
  position: relative;
  display: flex;
  flex-direction: column;
}

.glass-textarea textarea {
  width: 100%;
  padding: 16px;
  border: 2px solid rgba(255, 255, 255, 0.2);
  border-radius: 12px;
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  font-size: 14px;
  font-family: inherit;
  color: white;
  resize: vertical;
  transition: all 0.3s ease;
}

.glass-textarea textarea::placeholder {
  color: rgba(255, 255, 255, 0.5);
}

.glass-textarea textarea:focus {
  outline: none;
  border-color: rgba(255, 255, 255, 0.4);
  background: rgba(255, 255, 255, 0.15);
}

.glass-textarea__label {
  position: absolute;
  top: -8px;
  left: 12px;
  padding: 0 8px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  font-size: 12px;
  font-weight: 600;
  color: white;
  border-radius: 4px;
}

.glass-textarea__line {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 2px;
  background: linear-gradient(90deg, #667eea, #764ba2);
  border-radius: 1px;
  transform: scaleX(0);
  transition: transform 0.3s ease;
}

.glass-textarea.is-focused .glass-textarea__line {
  transform: scaleX(1);
}
</style>
