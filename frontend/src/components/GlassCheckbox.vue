<template>
  <label class="glass-checkbox" :class="{ 'is-checked': modelValue }">
    <input
      type="checkbox"
      :checked="modelValue"
      :disabled="disabled"
      @change="onChange"
    />
    <span class="checkbox-box">
      <svg v-if="modelValue" width="12" height="12" viewBox="0 0 12 12" fill="none">
        <path d="M2 6L5 9L10 3" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
    </span>
    <span class="checkbox-label">
      <slot></slot>
    </span>
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
.glass-checkbox {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  cursor: pointer;
  user-select: none;
}

.glass-checkbox input {
  position: absolute;
  opacity: 0;
  width: 0;
  height: 0;
}

.checkbox-box {
  width: 20px;
  height: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 2px solid rgba(255, 255, 255, 0.3);
  border-radius: 6px;
  background: rgba(255, 255, 255, 0.1);
  transition: all 0.2s ease;
}

.glass-checkbox.is-checked .checkbox-box {
  background: linear-gradient(135deg, #667eea, #764ba2);
  border-color: transparent;
}

.glass-checkbox:hover .checkbox-box {
  border-color: rgba(255, 255, 255, 0.5);
}

.checkbox-label {
  font-size: 14px;
  color: rgba(255, 255, 255, 0.8);
}
</style>
