<template>
  <footer class="glass-footer">
    <div class="footer-container">
      <div class="footer-content">
        <div class="footer-brand">
          <h3 class="footer-logo">Gossip Hub</h3>
          <p class="footer-desc">专属于你们的八卦社交平台</p>
        </div>
        <div class="footer-links">
          <div class="footer-column">
            <h4 class="footer-title">产品</h4>
            <router-link to="/timeline" class="footer-link">时间线</router-link>
            <router-link to="/ranking" class="footer-link">排行榜</router-link>
            <router-link to="/graph" class="footer-link">关系图谱</router-link>
          </div>
          <div class="footer-column">
            <h4 class="footer-title">支持</h4>
            <a href="#" class="footer-link">帮助中心</a>
            <a href="#" class="footer-link">联系我们</a>
            <a href="#" class="footer-link">隐私政策</a>
          </div>
          <div class="footer-column">
            <h4 class="footer-title">关于</h4>
            <a href="#" class="footer-link">关于我们</a>
            <a href="#" class="footer-link">加入我们</a>
            <a href="#" class="footer-link">媒体报道</a>
          </div>
        </div>
      </div>
      <div class="footer-bottom">
        <p class="footer-copyright">&copy; 2024 Gossip Hub. All rights reserved.</p>
      </div>
    </div>
  </footer>
</template>

<script setup>
</script>

<style scoped>
.glass-footer {
  margin-top: auto;
  background: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  padding: 40px 0 20px;
}

.footer-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 24px;
}

.footer-content {
  display: grid;
  grid-template-columns: 1fr 2fr;
  gap: 40px;
  margin-bottom: 32px;
}

.footer-logo {
  font-size: 24px;
  font-weight: 800;
  color: white;
  margin: 0 0 8px 0;
}

.footer-desc {
  font-size: 14px;
  color: rgba(255, 255, 255, 0.5);
  margin: 0;
}

.footer-links {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
}

.footer-title {
  font-size: 14px;
  font-weight: 600;
  color: white;
  margin: 0 0 12px 0;
}

.footer-link {
  display: block;
  font-size: 14px;
  color: rgba(255, 255, 255, 0.5);
  text-decoration: none;
  margin-bottom: 8px;
  transition: color 0.2s ease;
}

.footer-link:hover {
  color: white;
}

.footer-bottom {
  padding-top: 20px;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  text-align: center;
}

.footer-copyright {
  font-size: 12px;
  color: rgba(255, 255, 255, 0.3);
  margin: 0;
}

@media (max-width: 768px) {
  .footer-content {
    grid-template-columns: 1fr;
  }

  .footer-links {
    grid-template-columns: repeat(2, 1fr);
  }
}
</style>
