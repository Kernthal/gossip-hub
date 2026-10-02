<template>
  <div class="floating-cards">
    <div
      v-for="(card, index) in cards"
      :key="index"
      class="floating-card"
      :style="{
        '--delay': `${index * 0.2}s`,
        '--x': `${card.x}%`,
        '--y': `${card.y}%`,
        '--rotation': `${card.rotation}deg`
      }"
    >
      <div class="floating-card-content">
        <h3>{{ card.title }}</h3>
        <p>{{ card.description }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { gsap } from 'gsap'

const cards = ref([
  { title: '八卦爆料', description: '匿名分享你知道的小道消息', x: 10, y: 20, rotation: -5 },
  { title: 'CP配对', description: '你觉得谁和谁最配？', x: 70, y: 15, rotation: 3 },
  { title: '关系图谱', description: '可视化展示谁和谁的关系', x: 15, y: 60, rotation: 2 },
  { title: '八卦预测', description: '预测下一步会发生什么', x: 75, y: 55, rotation: -3 },
  { title: '热度排行', description: '看看谁是最热的瓜', x: 40, y: 40, rotation: 0 },
])

onMounted(() => {
  const floatingCards = document.querySelectorAll('.floating-card')
  floatingCards.forEach((card, index) => {
    gsap.to(card, {
      y: 'random(-20, 20)',
      x: 'random(-10, 10)',
      rotation: 'random(-5, 5)',
      duration: 'random(2, 4)',
      repeat: -1,
      yoyo: true,
      ease: 'sine.inOut',
      delay: index * 0.2
    })
  })
})
</script>

<style scoped>
.floating-cards {
  position: relative;
  width: 100%;
  height: 100%;
  min-height: 400px;
}

.floating-card {
  position: absolute;
  left: var(--x);
  top: var(--y);
  transform: rotate(var(--rotation));
  animation: float 6s ease-in-out infinite;
  animation-delay: var(--delay);
}

.floating-card-content {
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(10px);
  border-radius: 16px;
  padding: 20px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.3);
  min-width: 150px;
  text-align: center;
  transition: all 0.3s ease;
}

.floating-card-content:hover {
  transform: scale(1.05);
  box-shadow: 0 15px 40px rgba(0, 0, 0, 0.15);
}

.floating-card-content h3 {
  margin: 0 0 8px 0;
  font-size: 18px;
  font-weight: 700;
  color: #1f2937;
}

.floating-card-content p {
  margin: 0;
  font-size: 14px;
  color: #6b7280;
}

@keyframes float {
  0%, 100% {
    transform: translateY(0) rotate(var(--rotation));
  }
  50% {
    transform: translateY(-20px) rotate(var(--rotation));
  }
}
</style>
