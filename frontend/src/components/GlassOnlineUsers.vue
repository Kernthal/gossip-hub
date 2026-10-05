<template>
  <div class="glass-online-users">
    <div class="online-header">
      <h3 class="online-title">在线用户</h3>
      <span class="online-count">{{ users.length }}</span>
    </div>
    <div class="online-list">
      <div v-for="user in users" :key="user.id" class="online-item">
        <GlassAvatar :src="user.avatar" size="small" :status="user.status" />
        <span class="online-name">{{ user.name }}</span>
      </div>
    </div>
  </div>
</template>

<script setup>
import GlassAvatar from './GlassAvatar.vue'

defineProps({
  users: {
    type: Array,
    default: () => []
  }
})
</script>

<style scoped>
.glass-online-users {
  padding: 24px;
}

.online-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 16px;
}

.online-title {
  font-size: 18px;
  font-weight: 700;
  color: white;
  margin: 0;
}

.online-count {
  padding: 2px 8px;
  background: rgba(16, 185, 129, 0.2);
  color: #10b981;
  font-size: 12px;
  font-weight: 600;
  border-radius: 10px;
}

.online-list {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.online-item {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 8px;
  border-radius: 8px;
  transition: all 0.2s ease;
}

.online-item:hover {
  background: rgba(255, 255, 255, 0.05);
}

.online-name {
  font-size: 14px;
  color: rgba(255, 255, 255, 0.8);
}
</style>
