<template>
  <nav class="glass-breadcrumb">
    <ol class="breadcrumb-list">
      <li v-for="(item, index) in items" :key="index" class="breadcrumb-item">
        <router-link v-if="item.to && index < items.length - 1" :to="item.to" class="breadcrumb-link">
          {{ item.label }}
        </router-link>
        <span v-else class="breadcrumb-current">
          {{ item.label }}
        </span>
        <span v-if="index < items.length - 1" class="breadcrumb-separator">
          <svg width="12" height="12" viewBox="0 0 12 12" fill="none">
            <path d="M4 2L8 6L4 10" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </span>
      </li>
    </ol>
  </nav>
</template>

<script setup>
defineProps({
  items: {
    type: Array,
    required: true
  }
})
</script>

<style scoped>
.glass-breadcrumb {
  padding: 12px 0;
}

.breadcrumb-list {
  display: flex;
  align-items: center;
  list-style: none;
  margin: 0;
  padding: 0;
  flex-wrap: wrap;
  gap: 8px;
}

.breadcrumb-item {
  display: flex;
  align-items: center;
  gap: 8px;
}

.breadcrumb-link {
  color: rgba(255, 255, 255, 0.7);
  text-decoration: none;
  font-size: 14px;
  transition: color 0.2s ease;
}

.breadcrumb-link:hover {
  color: white;
}

.breadcrumb-current {
  color: white;
  font-size: 14px;
  font-weight: 600;
}

.breadcrumb-separator {
  color: rgba(255, 255, 255, 0.3);
  display: flex;
  align-items: center;
}
</style>
