<template>
  <label class="glass-radio" :class="{ 'is-checked': modelValue === value }">
    <input
      type="radio"
      :name="name"
      :value="value"
      :checked="modelValue === value"
      :disabled="disabled"
      @change="onChange"
    />
    <span class="radio-circle"></span>
    <span class="radio-label">
      <slot></slot>
    </span>
  </label>
</template>

<script setup>
defineProps({
  modelValue: {
    type: [String, Number],
    default: ''
  },
  value: {
    type: [String, Number],
    required: true
  },
  name: {
    type: String,
    default: ''
  },
  disabled: {
    type: Boolean,
    default: false
  }
})

const emit = defineEmits(['update:modelValue'])

function onChange(e) {
  emit('update:modelValue', e.target.value)
}
</script>

<style scoped>
.glass-radio {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  cursor: pointer;
  user-select: none;
}

.glass-radio input {
  position: absolute;
  opacity: 0;
  width: 0;
  height: 0;
}

.radio-circle {
  width: 20px;
  height: 20px;
  border: 2px solid rgba(255, 255, 255, 0.3);
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.1);
  position: relative;
  transition: all 0.2s ease;
}

.radio-circle::after {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: linear-gradient(135deg, #667eea, #764ba2);
  transform: translate(-50%, -50%) scale(0);
  transition: all 0.2s ease;
}

.glass-radio.is-checked .radio-circle {
  border-color: transparent;
}

.glass-radio.is-checked .radio-circle::after {
  transform: translate(-50%, -50%) scale(1);
}

.glass-radio:hover .radio-circle {
  border-color: rgba(255, 255, 255, 0.5);
}

.radio-label {
  font-size: 14px;
  color: rgba(255, 255, 255, 0.8);
}
</style>
