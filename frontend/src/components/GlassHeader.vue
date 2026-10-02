<template>
  <header class="glass-header">
    <div class="header-container">
      <router-link to="/" class="header-logo">
        <span class="logo-text">Gossip Hub</span>
      </router-link>
      <nav class="header-nav">
        <router-link to="/" class="nav-link">首页</router-link>
        <router-link to="/timeline" class="nav-link">时间线</router-link>
        <router-link to="/ranking" class="nav-link">排行</router-link>
        <router-link to="/graph" class="nav-link">关系图谱</router-link>
      </nav>
      <div class="header-actions">
        <template v-if="isLoggedIn">
          <GlassButton variant="primary" size="small" @click="$router.push('/post')">
            发布
          </GlassButton>
          <GlassAvatar :src="user?.avatar" size="small" @click="$router.push('/profile')" />
        </template>
        <template v-else>
          <GlassButton variant="ghost" size="small" @click="$router.push('/login')">
            登录
          </GlassButton>
          <GlassButton variant="primary" size="small" @click="$router.push('/register')">
            注册
          </GlassButton>
        </template>
      </div>
    </div>
  </header>
</template>

<script setup>
import { computed } from 'vue'
import { useUserStore } from '../stores'
import GlassButton from './GlassButton.vue'
import GlassAvatar from './GlassAvatar.vue'

const userStore = useUserStore()
const isLoggedIn = computed(() => userStore.isLoggedIn)
const user = computed(() => userStore.user)
</script>

<style scoped>
.glass-header {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 100;
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border-bottom: 1px solid rgba(255, 255, 255, 0.2);
}

.header-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 16px 24px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.header-logo {
  text-decoration: none;
}

.logo-text {
  font-size: 24px;
  font-weight: 800;
  color: white;
  text-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
}

.header-nav {
  display: flex;
  gap: 8px;
}

.nav-link {
  padding: 8px 16px;
  border-radius: 12px;
  text-decoration: none;
  color: rgba(255, 255, 255, 0.8);
  font-weight: 500;
  transition: all 0.3s ease;
}

.nav-link:hover {
  background: rgba(255, 255, 255, 0.1);
  color: white;
}

.nav-link.router-link-active {
  background: rgba(255, 255, 255, 0.2);
  color: white;
}

.header-actions {
  display: flex;
  align-items: center;
  gap: 12px;
}

@media (max-width: 768px) {
  .header-nav {
    display: none;
  }
}
</style>
