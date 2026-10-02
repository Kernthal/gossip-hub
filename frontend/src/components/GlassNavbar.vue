<template>
  <nav class="glass-navbar" :class="{ 'is-scrolled': isScrolled }">
    <div class="navbar-container">
      <router-link to="/" class="navbar-logo">
        <span class="logo-text">Gossip Hub</span>
      </router-link>
      <div class="navbar-links">
        <router-link to="/" class="nav-link">首页</router-link>
        <router-link to="/timeline" class="nav-link">时间线</router-link>
        <router-link to="/ranking" class="nav-link">排行</router-link>
        <router-link to="/graph" class="nav-link">关系图谱</router-link>
        <router-link to="/profile" class="nav-link">我的</router-link>
      </div>
      <div class="navbar-actions">
        <GlassButton variant="primary" size="small" @click="$router.push('/post')">
          发布
        </GlassButton>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import GlassButton from './GlassButton.vue'

const isScrolled = ref(false)

function handleScroll() {
  isScrolled.value = window.scrollY > 50
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll)
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})
</script>

<style scoped>
.glass-navbar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 100;
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border-bottom: 1px solid rgba(255, 255, 255, 0.2);
  transition: all 0.3s ease;
}

.glass-navbar.is-scrolled {
  background: rgba(255, 255, 255, 0.15);
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
}

.navbar-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 16px 24px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.navbar-logo {
  text-decoration: none;
}

.logo-text {
  font-size: 24px;
  font-weight: 800;
  color: white;
  text-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
}

.navbar-links {
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

.navbar-actions {
  display: flex;
  gap: 12px;
}

@media (max-width: 768px) {
  .navbar-links {
    display: none;
  }
}
</style>
