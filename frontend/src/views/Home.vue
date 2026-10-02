<template>
  <div class="home">
    <section class="hero">
      <div class="hero-content">
        <h1 class="hero-title">
          <TypingText :text="title" :speed="80" />
        </h1>
        <p class="hero-subtitle">专属于你们的八卦社交平台</p>
        <div class="hero-actions">
          <GlassButton variant="primary" @click="$router.push('/timeline')">
            浏览时间线
          </GlassButton>
          <GlassButton variant="ghost" @click="$router.push('/post')">
            发布八卦
          </GlassButton>
        </div>
      </div>
      <div class="hero-visual">
        <FloatingCards />
      </div>
    </section>

    <section class="features">
      <div class="features-grid">
        <LiquidGlass v-for="feature in features" :key="feature.title" variant="card">
          <div class="feature-card">
            <div class="feature-icon">
              <SVGMorph :shape="feature.shape" :size="60" :color1="feature.color1" :color2="feature.color2" />
            </div>
            <h3 class="feature-title">{{ feature.title }}</h3>
            <p class="feature-desc">{{ feature.description }}</p>
          </div>
        </LiquidGlass>
      </div>
    </section>

    <section class="stats">
      <div class="stats-grid">
        <div class="stat-item">
          <div class="stat-value">1000+</div>
          <div class="stat-label">匿名八卦</div>
        </div>
        <div class="stat-item">
          <div class="stat-value">500+</div>
          <div class="stat-label">CP配对</div>
        </div>
        <div class="stat-item">
          <div class="stat-value">200+</div>
          <div class="stat-label">关系图谱</div>
        </div>
        <div class="stat-item">
          <div class="stat-value">50+</div>
          <div class="stat-label">八卦预测</div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import TypingText from '../components/TypingText.vue'
import GlassButton from '../components/GlassButton.vue'
import LiquidGlass from '../components/LiquidGlass.vue'
import SVGMorph from '../components/SVGMorph.vue'
import FloatingCards from '../components/FloatingCards.vue'

const title = 'Gossip Hub'

const features = [
  {
    title: '八卦爆料',
    description: '匿名分享你知道的小道消息，看看谁和谁在一起了',
    shape: 'blob',
    color1: '#667eea',
    color2: '#764ba2'
  },
  {
    title: 'CP配对',
    description: '你觉得谁和谁最配？发起投票，看看大家怎么说',
    shape: 'heart',
    color1: '#f093fb',
    color2: '#f5576c'
  },
  {
    title: '关系图谱',
    description: '可视化展示谁和谁的关系，一目了然',
    shape: 'hexagon',
    color1: '#4facfe',
    color2: '#00f2fe'
  },
  {
    title: '八卦预测',
    description: '预测下一步会发生什么，押注你的判断',
    shape: 'star',
    color1: '#fa709a',
    color2: '#fee140'
  }
]
</script>

<style scoped>
.home {
  max-width: 1200px;
  margin: 0 auto;
  padding: 40px 24px;
}

.hero {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 60px;
  align-items: center;
  min-height: 70vh;
  margin-bottom: 80px;
}

.hero-title {
  font-size: 64px;
  font-weight: 800;
  color: white;
  margin-bottom: 16px;
  text-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
  min-height: 80px;
}

.hero-subtitle {
  font-size: 24px;
  color: rgba(255, 255, 255, 0.8);
  margin-bottom: 32px;
}

.hero-actions {
  display: flex;
  gap: 16px;
}

.hero-visual {
  height: 400px;
}

.features {
  margin-bottom: 80px;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 24px;
}

.feature-card {
  text-align: center;
  padding: 20px;
}

.feature-icon {
  display: flex;
  justify-content: center;
  margin-bottom: 16px;
}

.feature-title {
  font-size: 20px;
  font-weight: 700;
  color: #1f2937;
  margin-bottom: 8px;
}

.feature-desc {
  font-size: 14px;
  color: #6b7280;
  line-height: 1.6;
}

.stats {
  margin-bottom: 80px;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 24px;
}

.stat-item {
  text-align: center;
  padding: 32px;
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  border-radius: 16px;
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.stat-value {
  font-size: 48px;
  font-weight: 800;
  color: white;
  margin-bottom: 8px;
}

.stat-label {
  font-size: 16px;
  color: rgba(255, 255, 255, 0.7);
}

@media (max-width: 768px) {
  .hero {
    grid-template-columns: 1fr;
    text-align: center;
  }

  .hero-title {
    font-size: 40px;
  }

  .hero-actions {
    justify-content: center;
  }

  .stats-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}
</style>
