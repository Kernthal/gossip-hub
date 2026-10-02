<template>
  <div class="glass-tabs">
    <div class="tabs-header">
      <button
        v-for="tab in tabs"
        :key="tab.key"
        class="tab-button"
        :class="{ 'is-active': activeTab === tab.key }"
        @click="activeTab = tab.key"
      >
        {{ tab.label }}
      </button>
    </div>
    <div class="tabs-content">
      <slot :name="activeTab"></slot>
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'

const props = defineProps({
  tabs: {
    type: Array,
    required: true
  },
  defaultTab: {
    type: String,
    default: ''
  }
})

const emit = defineEmits(['update:activeTab'])

const activeTab = ref(props.defaultTab || props.tabs[0]?.key || '')

watch(activeTab, (val) => {
  emit('update:activeTab', val)
})
</script>

<style scoped>
.glass-tabs {
  width: 100%;
}

.tabs-header {
  display: flex;
  gap: 4px;
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  padding: 4px;
  border-radius: 12px;
  border: 1px solid rgba(255, 255, 255, 0.2);
  margin-bottom: 16px;
}

.tab-button {
  flex: 1;
  padding: 12px 24px;
  border: none;
  border-radius: 8px;
  background: transparent;
  color: rgba(255, 255, 255, 0.7);
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.tab-button:hover {
  color: white;
}

.tab-button.is-active {
  background: rgba(255, 255, 255, 0.2);
  color: white;
}

.tabs-content {
  min-height: 200px;
}
</style>
