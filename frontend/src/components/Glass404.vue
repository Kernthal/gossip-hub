<template>
  <div class="glass-404">
    <div class="error-code">404</div>
    <h2 class="error-title">页面不存在</h2>
    <p class="error-message">你访问的页面不存在或已被删除</p>
    <GlassButton variant="primary" @click="$router.push('/')">
      返回首页
    </GlassButton>
  </div>
</template>

<script setup>
import GlassButton from './GlassButton.vue'
</script>

<style scoped>
.glass-404 {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 60vh;
  text-align: center;
  padding: 40px 20px;
}

.error-code {
  font-size: 120px;
  font-weight: 800;
  color: rgba(255, 255, 255, 0.1);
  line-height: 1;
  margin-bottom: 16px;
  text-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
}

.error-title {
  margin: 0 0 8px 0;
  font-size: 24px;
  font-weight: 700;
  color: white;
}

.error-message {
  margin: 0 0 32px 0;
  font-size: 16px;
  color: rgba(255, 255, 255, 0.6);
}
</style>
