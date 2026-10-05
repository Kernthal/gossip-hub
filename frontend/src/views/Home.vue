<template>
  <div class="home">
    <section class="hero">
      <div class="hero-content">
        <h1 class="hero-title">Gossip Hub</h1>
        <p class="hero-subtitle">专属于你们的八卦社交平台</p>
        <div class="hero-actions">
          <router-link to="/timeline" class="hero-button primary">
            <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
              <path d="M10 2L12 8H18L13 12L15 18L10 14L5 18L7 12L2 8H8L10 2Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
            <span>浏览时间线</span>
          </router-link>
          <router-link to="/post" class="hero-button secondary">
            <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
              <path d="M10 3V17M3 10H17" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
            </svg>
            <span>发布八卦</span>
          </router-link>
        </div>
      </div>
    </section>

    <section class="features">
      <div class="features-grid">
        <div class="feature-card">
          <div class="feature-icon">
            <svg width="32" height="32" viewBox="0 0 32 32" fill="none">
              <path d="M16 4C9 4 4 9 4 16C4 23 9 28 16 28C23 28 28 23 28 16C28 9 23 4 16 4Z" stroke="currentColor" stroke-width="2"/>
              <path d="M10 14H22M10 18H18" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
            </svg>
          </div>
          <h3 class="feature-title">八卦爆料</h3>
          <p class="feature-desc">匿名分享你知道的小道消息</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon">
            <svg width="32" height="32" viewBox="0 0 32 32" fill="none">
              <path d="M16 26L6 16C3 13 3 8 6 5C9 2 13 2 16 5C19 2 23 2 26 5C29 8 29 13 26 16L16 26Z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </div>
          <h3 class="feature-title">CP配对</h3>
          <p class="feature-desc">你觉得谁和谁最配？发起投票</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon">
            <svg width="32" height="32" viewBox="0 0 32 32" fill="none">
              <circle cx="8" cy="16" r="4" stroke="currentColor" stroke-width="2"/>
              <circle cx="24" cy="8" r="4" stroke="currentColor" stroke-width="2"/>
              <circle cx="24" cy="24" r="4" stroke="currentColor" stroke-width="2"/>
              <path d="M11 14L20 10M11 18L20 22" stroke="currentColor" stroke-width="2"/>
            </svg>
          </div>
          <h3 class="feature-title">关系图谱</h3>
          <p class="feature-desc">可视化展示谁和谁的关系</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon">
            <svg width="32" height="32" viewBox="0 0 32 32" fill="none">
              <path d="M16 4L18 12H26L20 17L22 25L16 20L10 25L12 17L6 12H14L16 4Z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </div>
          <h3 class="feature-title">八卦预测</h3>
          <p class="feature-desc">预测下一步会发生什么</p>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
</script>

<style scoped>
.home {
  max-width: 1200px;
  margin: 0 auto;
  padding: 40px 24px;
}

.hero {
  text-align: center;
  padding: 80px 0;
}

.hero-title {
  font-size: 64px;
  font-weight: 800;
  color: white;
  margin: 0 0 16px 0;
  letter-spacing: -2px;
}

.hero-subtitle {
  font-size: 20px;
  color: rgba(255, 255, 255, 0.7);
  margin: 0 0 40px 0;
}

.hero-actions {
  display: flex;
  gap: 16px;
  justify-content: center;
}

.hero-button {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 14px 28px;
  border-radius: 12px;
  font-size: 16px;
  font-weight: 600;
  text-decoration: none;
  transition: all 0.2s ease;
}

.hero-button.primary {
  background: white;
  color: #667eea;
}

.hero-button.primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
}

.hero-button.secondary {
  background: rgba(255, 255, 255, 0.1);
  color: white;
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.hero-button.secondary:hover {
  background: rgba(255, 255, 255, 0.15);
  transform: translateY(-2px);
}

.features {
  padding: 40px 0;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 24px;
}

.feature-card {
  padding: 32px 24px;
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(20px);
  border-radius: 16px;
  border: 1px solid rgba(255, 255, 255, 0.3);
  text-align: center;
  transition: all 0.3s ease;
}

.feature-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 32px rgba(0, 0, 0, 0.1);
}

.feature-icon {
  width: 64px;
  height: 64px;
  margin: 0 auto 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 16px;
  background: rgba(102, 126, 234, 0.1);
  color: #667eea;
}

.feature-title {
  font-size: 18px;
  font-weight: 700;
  color: #1f2937;
  margin: 0 0 8px 0;
}

.feature-desc {
  font-size: 14px;
  color: #6b7280;
  margin: 0;
  line-height: 1.5;
}

@media (max-width: 768px) {
  .hero-title {
    font-size: 40px;
  }

  .features-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}
</style>
