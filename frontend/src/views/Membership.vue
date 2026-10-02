<template>
  <div class="membership-page">
    <h1 class="membership-title">会员中心</h1>

    <div class="membership-current">
      <LiquidGlass variant="card">
        <div class="current-tier">
          <div class="tier-badge">
            <SVGMorph shape="star" :size="60" color1="#ffd700" color2="#ffaa00" />
          </div>
          <div class="tier-info">
            <h3 class="tier-name">{{ currentTier.label }}</h3>
            <p class="tier-expiry">{{ currentTier.expiry }}</p>
          </div>
        </div>
      </LiquidGlass>
    </div>

    <div class="membership-tiers">
      <LiquidGlass v-for="tier in tiers" :key="tier.name" variant="card">
        <div class="tier-card" :class="{ 'is-current': user.membership_tier === tier.name }">
          <div class="tier-header">
            <h4 class="tier-label">{{ tier.label }}</h4>
            <p class="tier-price">{{ tier.price }}</p>
          </div>
          <ul class="tier-features">
            <li v-for="feature in tier.features" :key="feature" class="feature-item">
              <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
                <path d="M13.5 4.5L6 12L2.5 8.5" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
              <span>{{ feature }}</span>
            </li>
          </ul>
          <GlassButton
            :variant="user.membership_tier === tier.name ? 'success' : 'primary'"
            @click="selectTier(tier)"
          >
            {{ user.membership_tier === tier.name ? '当前等级' : '升级' }}
          </GlassButton>
        </div>
      </LiquidGlass>
    </div>

    <div class="membership-benefits">
      <LiquidGlass variant="card">
        <div class="benefits-content">
          <h3 class="benefits-title">会员权益</h3>
          <div class="benefits-grid">
            <div class="benefit-item">
              <div class="benefit-icon">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
                  <path d="M12 2L2 7L12 12L22 7L12 2Z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  <path d="M2 17L12 22L22 17" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  <path d="M2 12L12 17L22 12" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
              </div>
              <h4 class="benefit-title">更多匿名额度</h4>
              <p class="benefit-desc">每月享受更多匿名发帖次数</p>
            </div>
            <div class="benefit-item">
              <div class="benefit-icon">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
                  <path d="M12 2L15.09 8.26L22 9.27L17 14.14L18.18 21.02L12 17.77L5.82 21.02L7 14.14L2 9.27L8.91 8.26L12 2Z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
              </div>
              <h4 class="benefit-title">专属标识</h4>
              <p class="benefit-desc">独特的会员徽章和标识</p>
            </div>
            <div class="benefit-item">
              <div class="benefit-icon">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
                  <path d="M13 2L3 14H12L11 22L21 10H12L13 2Z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
              </div>
              <h4 class="benefit-title">优先审核</h4>
              <p class="benefit-desc">帖子优先审核，更快发布</p>
            </div>
            <div class="benefit-item">
              <div class="benefit-icon">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
                  <path d="M12 22C17.52 22 22 17.52 22 12C22 6.48 17.52 2 12 2C6.48 2 2 6.48 2 12C2 17.52 6.48 22 12 22Z" stroke="currentColor" stroke-width="2"/>
                  <path d="M12 6V12L16 14" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
                </svg>
              </div>
              <h4 class="benefit-title">去广告</h4>
              <p class="benefit-desc">享受无广告的清爽体验</p>
            </div>
          </div>
        </div>
      </LiquidGlass>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import LiquidGlass from '../components/LiquidGlass.vue'
import SVGMorph from '../components/SVGMorph.vue'
import GlassButton from '../components/GlassButton.vue'

const user = ref({
  membership_tier: 'free'
})

const tiers = [
  {
    name: 'vip',
    label: 'VIP',
    price: '¥9.9/月',
    features: ['每月20条匿名额度', 'VIP徽章', '优先审核']
  },
  {
    name: 'svip',
    label: 'SVIP',
    price: '¥19.9/月',
    features: ['每月50条匿名额度', 'SVIP徽章', '优先审核', '特殊功能']
  },
  {
    name: 'star',
    label: '星钻VIP',
    price: '¥39.9/月',
    features: ['无限匿名额度', '星钻徽章', '优先审核', '特殊功能', '去广告']
  },
  {
    name: 'diamond',
    label: '黑钻VIP',
    price: '¥69.9/月',
    features: ['无限匿名额度', '黑钻徽章', '优先审核', '特殊功能', '去广告', '专属客服']
  },
  {
    name: 'yellow',
    label: '黄钻VIP',
    price: '¥99.9/月',
    features: ['无限匿名额度', '黄钻徽章', '优先审核', '特殊功能', '去广告', '专属客服', '定制功能']
  }
]

const currentTier = ref({
  label: '免费用户',
  expiry: '永久'
})

function selectTier(tier) {
  // TODO: 实现会员升级逻辑
  alert(`选择升级到 ${tier.label}`)
}
</script>

<style scoped>
.membership-page {
  max-width: 1000px;
  margin: 0 auto;
  padding: 40px 24px;
}

.membership-title {
  font-size: 36px;
  font-weight: 800;
  color: white;
  text-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
  margin-bottom: 32px;
}

.membership-current {
  margin-bottom: 32px;
}

.current-tier {
  display: flex;
  align-items: center;
  gap: 20px;
  padding: 24px;
}

.tier-badge {
  width: 60px;
  height: 60px;
}

.tier-name {
  font-size: 24px;
  font-weight: 700;
  color: #1f2937;
  margin-bottom: 4px;
}

.tier-expiry {
  font-size: 14px;
  color: #6b7280;
}

.membership-tiers {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
  margin-bottom: 32px;
}

.tier-card {
  padding: 24px;
  text-align: center;
}

.tier-card.is-current {
  border: 2px solid #667eea;
}

.tier-header {
  margin-bottom: 16px;
}

.tier-label {
  font-size: 20px;
  font-weight: 700;
  color: #1f2937;
  margin-bottom: 8px;
}

.tier-price {
  font-size: 28px;
  font-weight: 800;
  color: #667eea;
}

.tier-features {
  list-style: none;
  padding: 0;
  margin: 0 0 20px 0;
  text-align: left;
}

.feature-item {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 0;
  font-size: 14px;
  color: #4b5563;
}

.feature-item svg {
  color: #10b981;
  flex-shrink: 0;
}

.benefits-content {
  padding: 24px;
}

.benefits-title {
  font-size: 20px;
  font-weight: 700;
  color: #1f2937;
  margin-bottom: 20px;
}

.benefits-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
}

.benefit-item {
  text-align: center;
  padding: 20px;
  background: rgba(102, 126, 234, 0.05);
  border-radius: 12px;
}

.benefit-icon {
  width: 48px;
  height: 48px;
  margin: 0 auto 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(102, 126, 234, 0.1);
  border-radius: 12px;
  color: #667eea;
}

.benefit-title {
  font-size: 16px;
  font-weight: 600;
  color: #1f2937;
  margin-bottom: 8px;
}

.benefit-desc {
  font-size: 14px;
  color: #6b7280;
}
</style>
