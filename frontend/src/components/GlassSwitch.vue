<template>
  <label class="glass-switch" :class="{ 'is-checked': modelValue }">
    <input
      type="checkbox"
      :checked="modelValue"
      :disabled="disabled"
      @change="onChange"
    />
    <span class="switch-slider"></span>
  </label>
</template>

<script setup>
defineProps({
  modelValue: {
    type: Boolean,
    default: false
  },
  disabled: {
    type: Boolean,
    default: false
  }
})

const emit = defineEmits(['update:modelValue'])

function onChange(e) {
  emit('update:modelValue', e.target.checked)
}
</script>

<style scoped>
.glass-switch {
  position: relative;
  display: inline-block;
  width: 50px;
  height: 28px;
}

.glass-switch input {
  position: absolute;
  opacity: 0;
  width: 0;
  height: 0;
}

.switch-slider {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 14px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.switch-slider::before {
  content: '';
  position: absolute;
  top: 3px;
  left: 3px;
  width: 22px;
  height: 22px;
  border-radius: 50%;
  background: white;
  transition: all 0.3s ease;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}

.glass-switch.is-checked .switch-slider {
  background: linear-gradient(135deg, #667eea, #764ba2);
}

.glass-switch.is-checked .switch-slider::before {
  transform: translateX(22px);
}

.glass-switch:hover .switch-slider {
  background: rgba(255, 255, 255, 0.3);
}

.glass-switch.is-checked:hover .switch-slider {
  background: linear-gradient(135deg, #5a6fd6, #6a4190);
}
</style>
