<template>
  <div class="glass-accordion">
    <div v-for="(item, index) in items" :key="index" class="accordion-item">
      <button
        class="accordion-header"
        :class="{ 'is-open': openItems.includes(index) }"
        @click="toggle(index)"
      >
        <span class="accordion-title">{{ item.title }}</span>
        <svg class="accordion-icon" width="16" height="16" viewBox="0 0 16 16" fill="none">
          <path d="M4 6L8 10L12 6" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
      </button>
      <Transition name="accordion">
        <div v-if="openItems.includes(index)" class="accordion-content">
          <div class="accordion-body">
            <slot :item="item" :index="index"></slot>
          </div>
        </div>
      </Transition>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const props = defineProps({
  items: {
    type: Array,
    required: true
  },
  multiple: {
    type: Boolean,
    default: false
  }
})

const openItems = ref([])

function toggle(index) {
  if (props.multiple) {
    const itemIndex = openItems.value.indexOf(index)
    if (itemIndex > -1) {
      openItems.value.splice(itemIndex, 1)
    } else {
      openItems.value.push(index)
    }
  } else {
    openItems.value = openItems.value.includes(index) ? [] : [index]
  }
}
</script>

<style scoped>
.glass-accordion {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.accordion-item {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  border-radius: 12px;
  border: 1px solid rgba(255, 255, 255, 0.2);
  overflow: hidden;
}

.accordion-header {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 16px 20px;
  border: none;
  background: transparent;
  color: white;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
}

.accordion-header:hover {
  background: rgba(255, 255, 255, 0.05);
}

.accordion-header.is-open {
  background: rgba(255, 255, 255, 0.1);
}

.accordion-icon {
  transition: transform 0.3s ease;
}

.accordion-header.is-open .accordion-icon {
  transform: rotate(180deg);
}

.accordion-content {
  overflow: hidden;
}

.accordion-body {
  padding: 16px 20px;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
}

.accordion-enter-active,
.accordion-leave-active {
  transition: all 0.3s ease;
}

.accordion-enter-from,
.accordion-leave-to {
  opacity: 0;
  max-height: 0;
}
</style>
