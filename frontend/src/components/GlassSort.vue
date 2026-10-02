<template>
  <div class="glass-sort">
    <span class="sort-label">排序：</span>
    <div class="sort-options">
      <button
        v-for="option in options"
        :key="option.value"
        class="sort-option"
        :class="{ 'is-active': modelValue === option.value }"
        @click="select(option.value)"
      >
        {{ option.label }}
        <svg v-if="modelValue === option.value" width="12" height="12" viewBox="0 0 12 12" fill="none">
          <path v-if="sortOrder === 'asc'" d="M6 2L10 8H2L6 2Z" fill="currentColor"/>
          <path v-else d="M6 10L2 4H10L6 10Z" fill="currentColor"/>
        </svg>
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'

const props = defineProps({
  options: {
    type: Array,
    required: true
  },
  modelValue: {
    type: String,
    default: ''
  },
  defaultOrder: {
    type: String,
    default: 'desc',
    validator: (v) => ['asc', 'desc'].includes(v)
  }
})

const emit = defineEmits(['update:modelValue', 'update:order'])

const sortOrder = ref(props.defaultOrder)

watch(sortOrder, (val) => {
  emit('update:order', val)
})

function select(value) {
  if (props.modelValue === value) {
    sortOrder.value = sortOrder.value === 'asc' ? 'desc' : 'asc'
  } else {
    emit('update:modelValue', value)
    sortOrder.value = props.defaultOrder
  }
}
</script>

<style scoped>
.glass-sort {
  display: flex;
  align-items: center;
  gap: 12px;
}

.sort-label {
  font-size: 14px;
  color: rgba(255, 255, 255, 0.7);
}

.sort-options {
  display: flex;
  gap: 8px;
}

.sort-option {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 6px 12px;
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 8px;
  background: transparent;
  color: rgba(255, 255, 255, 0.7);
  font-size: 12px;
  cursor: pointer;
  transition: all 0.2s ease;
}

.sort-option:hover {
  background: rgba(255, 255, 255, 0.1);
  color: white;
}

.sort-option.is-active {
  background: linear-gradient(135deg, #667eea, #764ba2);
  border-color: transparent;
  color: white;
}
</style>
