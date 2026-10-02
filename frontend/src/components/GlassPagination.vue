<template>
  <div class="glass-pagination">
    <button
      class="pagination-button"
      :disabled="currentPage <= 1"
      @click="goToPage(currentPage - 1)"
    >
      <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
        <path d="M10 12L6 8L10 4" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
    </button>
    <div class="pagination-pages">
      <button
        v-for="page in visiblePages"
        :key="page"
        class="pagination-page"
        :class="{ 'is-active': page === currentPage }"
        @click="goToPage(page)"
      >
        {{ page }}
      </button>
    </div>
    <button
      class="pagination-button"
      :disabled="currentPage >= totalPages"
      @click="goToPage(currentPage + 1)"
    >
      <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
        <path d="M6 4L10 8L6 12" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
    </button>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  currentPage: {
    type: Number,
    default: 1
  },
  totalPages: {
    type: Number,
    default: 1
  },
  maxVisible: {
    type: Number,
    default: 5
  }
})

const emit = defineEmits(['update:page'])

const visiblePages = computed(() => {
  const pages = []
  let start = Math.max(1, props.currentPage - Math.floor(props.maxVisible / 2))
  let end = Math.min(props.totalPages, start + props.maxVisible - 1)
  
  if (end - start < props.maxVisible - 1) {
    start = Math.max(1, end - props.maxVisible + 1)
  }
  
  for (let i = start; i <= end; i++) {
    pages.push(i)
  }
  
  return pages
})

function goToPage(page) {
  if (page >= 1 && page <= props.totalPages && page !== props.currentPage) {
    emit('update:page', page)
  }
}
</script>

<style scoped>
.glass-pagination {
  display: flex;
  align-items: center;
  gap: 8px;
  justify-content: center;
  padding: 16px;
}

.pagination-button {
  width: 36px;
  height: 36px;
  display: flex;
  align-items: center;
  justify-content: center;
  border: none;
  border-radius: 8px;
  background: rgba(255, 255, 255, 0.1);
  color: white;
  cursor: pointer;
  transition: all 0.2s ease;
}

.pagination-button:hover:not(:disabled) {
  background: rgba(255, 255, 255, 0.2);
}

.pagination-button:disabled {
  opacity: 0.3;
  cursor: not-allowed;
}

.pagination-pages {
  display: flex;
  gap: 4px;
}

.pagination-page {
  width: 36px;
  height: 36px;
  display: flex;
  align-items: center;
  justify-content: center;
  border: none;
  border-radius: 8px;
  background: transparent;
  color: rgba(255, 255, 255, 0.7);
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
}

.pagination-page:hover {
  background: rgba(255, 255, 255, 0.1);
  color: white;
}

.pagination-page.is-active {
  background: rgba(255, 255, 255, 0.2);
  color: white;
}
</style>
