<template>
  <aside class="glass-sidebar">
    <div class="sidebar-header">
      <h3 class="sidebar-title">导航</h3>
    </div>
    <nav class="sidebar-nav">
      <router-link to="/" class="sidebar-link" active-class="is-active">
        <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
          <path d="M10 2L2 8V18H7V12H13V18H18V8L10 2Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
        <span>首页</span>
      </router-link>
      <router-link to="/timeline" class="sidebar-link" active-class="is-active">
        <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
          <circle cx="10" cy="10" r="8" stroke="currentColor" stroke-width="1.5"/>
          <path d="M10 6V10L13 12" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
        </svg>
        <span>时间线</span>
      </router-link>
      <router-link to="/ranking" class="sidebar-link" active-class="is-active">
        <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
          <path d="M10 2L12.5 7.5L18 8.5L14 12.5L15 18L10 15.5L5 18L6 12.5L2 8.5L7.5 7.5L10 2Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
        <span>排行榜</span>
      </router-link>
      <router-link to="/graph" class="sidebar-link" active-class="is-active">
        <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
          <circle cx="5" cy="10" r="3" stroke="currentColor" stroke-width="1.5"/>
          <circle cx="15" cy="5" r="3" stroke="currentColor" stroke-width="1.5"/>
          <circle cx="15" cy="15" r="3" stroke="currentColor" stroke-width="1.5"/>
          <path d="M7.5 8.5L12.5 6.5M7.5 11.5L12.5 13.5" stroke="currentColor" stroke-width="1.5"/>
        </svg>
        <span>关系图谱</span>
      </router-link>
      <router-link to="/membership" class="sidebar-link" active-class="is-active">
        <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
          <path d="M10 1L12 7H18L13 11L15 17L10 13L5 17L7 11L2 7H8L10 1Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
        <span>会员中心</span>
      </router-link>
      <router-link to="/settings" class="sidebar-link" active-class="is-active">
        <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
          <circle cx="10" cy="10" r="3" stroke="currentColor" stroke-width="1.5"/>
          <path d="M10 2V4M10 16V18M2 10H4M16 10H18M4.93 4.93L6.34 6.34M13.66 13.66L15.07 15.07M4.93 15.07L6.34 13.66M13.66 6.34L15.07 4.93" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
        </svg>
        <span>设置</span>
      </router-link>
    </nav>
  </aside>
</template>

<script setup>
</script>

<style scoped>
.glass-sidebar {
  width: 240px;
  background: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  border-right: 1px solid rgba(255, 255, 255, 0.1);
  padding: 20px 0;
  position: fixed;
  top: 72px;
  left: 0;
  bottom: 0;
  overflow-y: auto;
}

.sidebar-header {
  padding: 0 20px 16px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  margin-bottom: 16px;
}

.sidebar-title {
  font-size: 12px;
  font-weight: 600;
  color: rgba(255, 255, 255, 0.5);
  text-transform: uppercase;
  letter-spacing: 1px;
  margin: 0;
}

.sidebar-nav {
  display: flex;
  flex-direction: column;
  gap: 4px;
  padding: 0 12px;
}

.sidebar-link {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 16px;
  border-radius: 12px;
  text-decoration: none;
  color: rgba(255, 255, 255, 0.7);
  font-size: 14px;
  font-weight: 500;
  transition: all 0.2s ease;
}

.sidebar-link:hover {
  background: rgba(255, 255, 255, 0.1);
  color: white;
}

.sidebar-link.is-active {
  background: linear-gradient(135deg, rgba(102, 126, 234, 0.3), rgba(118, 75, 162, 0.3));
  color: white;
}

@media (max-width: 768px) {
  .glass-sidebar {
    display: none;
  }
}
</style>
