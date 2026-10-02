<template>
  <div class="glass-filter">
    <div class="filter-header">
      <h3 class="filter-title">筛选</h3>
      <button class="filter-reset" @click="reset">重置</button>
    </div>
    <div class="filter-groups">
      <div v-for="group in groups" :key="group.key" class="filter-group">
        <h4 class="group-title">{{ group.label }}</h4>
        <div class="group-options">
          <button
            v-for="option in group.options"
            :key="option.value"
            class="filter-option"
            :class="{ 'is-active': isSelected(group.key, option.value) }"
            @click="toggle(group.key, option.value)"
          >
            {{ option.label }}
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'

const props = defineProps({
  groups: {
    type: Array,
    required: true
  },
  modelValue: {
    type: Object,
    default: () => ({})
  }
})

const emit = defineEmits(['update:modelValue'])

const selected = ref({ ...props.modelValue })

watch(selected, (val) => {
  emit('update:modelValue', val)
}, { deep: true })

function isSelected(groupKey, value) {
  return selected.value[groupKey]?.includes(value)
}

function toggle(groupKey, value) {
  if (!selected.value[groupKey]) {
    selected.value[groupKey] = []
  }
  const index = selected.value[groupKey].indexOf(value)
  if (index > -1) {
    selected.value[groupKey].splice(index, 1)
  } else {
    selected.value[groupKey].push(value)
  }
}

function reset() {
  selected.value = {}
}
</script>

<style scoped>
.glass-filter {
  padding: 20px;
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  border-radius: 12px;
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.filter-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 16px;
}

.filter-title {
  font-size: 16px;
  font-weight: 600;
  color: white;
}

.filter-reset {
  background: none;
  border: none;
  color: rgba(255, 255, 255, 0.5);
  font-size: 12px;
  cursor: pointer;
  transition: color 0.2s;
}

.filter-reset:hover {
  color: white;
}

.filter-groups {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.group-title {
  font-size: 14px;
  font-weight: 600;
  color: rgba(255, 255, 255, 0.7);
  margin-bottom: 8px;
}

.group-options {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.filter-option {
  padding: 6px 12px;
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 20px;
  background: transparent;
  color: rgba(255, 255, 255, 0.7);
  font-size: 12px;
  cursor: pointer;
  transition: all 0.2s ease;
}

.filter-option:hover {
  background: rgba(255, 255, 255, 0.1);
  color: white;
}

.filter-option.is-active {
  background: linear-gradient(135deg, #667eea, #764ba2);
  border-color: transparent;
  color: white;
}
</style>
