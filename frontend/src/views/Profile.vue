<template>
  <div class="profile">
    <h1 class="profile-title">我的</h1>

    <LiquidGlass variant="card">
      <div class="profile-card">
        <div class="profile-header">
          <div class="profile-avatar">
            <SVGMorph shape="blob" :size="80" color1="#667eea" color2="#764ba2" />
          </div>
          <div class="profile-info">
            <h2 class="profile-name">{{ user.name }}</h2>
            <p class="profile-email">{{ user.email }}</p>
          </div>
        </div>

        <div class="profile-stats">
          <div class="stat-item">
            <div class="stat-value">{{ user.anonymous_quota }}</div>
            <div class="stat-label">匿名额度</div>
          </div>
          <div class="stat-item">
            <div class="stat-value">{{ user.coins }}</div>
            <div class="stat-label">虚拟货币</div>
          </div>
        </div>

        <div class="profile-actions">
          <GlassButton variant="primary" @click="showMembership = true">
            会员中心
          </GlassButton>
          <GlassButton variant="ghost" @click="$router.push('/my-posts')">
            我的发布
          </GlassButton>
          <GlassButton variant="ghost" @click="$router.push('/settings')">
            设置
          </GlassButton>
        </div>
      </div>
    </LiquidGlass>

    <GlassModal v-model="showMembership" title="会员中心">
      <div class="membership-content">
        <div class="membership-tiers">
          <div
            v-for="tier in tiers"
            :key="tier.name"
            class="tier-card"
            :class="{ 'is-current': user.membership_tier === tier.name }"
          >
            <h4 class="tier-name">{{ tier.label }}</h4>
            <p class="tier-price">{{ tier.price }}</p>
            <ul class="tier-features">
              <li v-for="feature in tier.features" :key="feature">{{ feature }}</li>
            </ul>
            <GlassButton
              :variant="user.membership_tier === tier.name ? 'success' : 'primary'"
              @click="selectTier(tier)"
            >
              {{ user.membership_tier === tier.name ? '当前等级' : '升级' }}
            </GlassButton>
          </div>
        </div>
      </div>
    </GlassModal>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import LiquidGlass from '../components/LiquidGlass.vue'
import SVGMorph from '../components/SVGMorph.vue'
import GlassButton from '../components/GlassButton.vue'
import GlassModal from '../components/GlassModal.vue'

const user = ref({
  name: '未登录',
  email: '',
  membership_tier: 'free',
  anonymous_quota: 0,
  coins: 0
})

const showMembership = ref(false)

const tiers = [
  {
    name: 'vip',
    label: 'VIP',
    price: '¥9.9/月',
    features: ['更多匿名额度', '专属标识', '优先审核']
  },
  {
    name: 'svip',
    label: 'SVIP',
    price: '¥19.9/月',
    features: ['更多匿名额度', '专属标识', '优先审核', '特殊功能']
  },
  {
    name: 'star',
    label: '星钻VIP',
    price: '¥39.9/月',
    features: ['无限匿名额度', '专属标识', '优先审核', '特殊功能', '去广告']
  },
  {
    name: 'diamond',
    label: '黑钻VIP',
    price: '¥69.9/月',
    features: ['无限匿名额度', '专属标识', '优先审核', '特殊功能', '去广告', '专属客服']
  },
  {
    name: 'yellow',
    label: '黄钻VIP',
    price: '¥99.9/月',
    features: ['无限匿名额度', '专属标识', '优先审核', '特殊功能', '去广告', '专属客服', '定制功能']
  }
]

function selectTier(tier) {
  // TODO: 实现会员升级逻辑
}

onMounted(async () => {
  // TODO: 从 API 获取用户信息
})
</script>

<style scoped>
.profile {
  max-width: 600px;
  margin: 0 auto;
  padding: 40px 24px;
}

.profile-title {
  font-size: 36px;
  font-weight: 800;
  color: white;
  text-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
  margin-bottom: 32px;
}

.profile-card {
  padding: 32px;
}

.profile-header {
  display: flex;
  align-items: center;
  gap: 20px;
  margin-bottom: 32px;
}

.profile-avatar {
  width: 80px;
  height: 80px;
}

.profile-name {
  font-size: 24px;
  font-weight: 700;
  color: #1f2937;
  margin-bottom: 4px;
}

.profile-email {
  font-size: 14px;
  color: #6b7280;
}

.profile-stats {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
  margin-bottom: 32px;
}

.stat-item {
  text-align: center;
  padding: 20px;
  background: rgba(102, 126, 234, 0.05);
  border-radius: 12px;
}

.stat-value {
  font-size: 32px;
  font-weight: 800;
  color: #667eea;
  margin-bottom: 4px;
}

.stat-label {
  font-size: 14px;
  color: #6b7280;
}

.profile-actions {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.membership-content {
  padding: 20px;
}

.membership-tiers {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 16px;
}

.tier-card {
  padding: 20px;
  border-radius: 12px;
  background: rgba(102, 126, 234, 0.05);
  text-align: center;
}

.tier-card.is-current {
  background: rgba(102, 126, 234, 0.1);
  border: 2px solid #667eea;
}

.tier-name {
  font-size: 18px;
  font-weight: 700;
  color: #1f2937;
  margin-bottom: 8px;
}

.tier-price {
  font-size: 24px;
  font-weight: 800;
  color: #667eea;
  margin-bottom: 16px;
}

.tier-features {
  list-style: none;
  padding: 0;
  margin: 0 0 16px 0;
  text-align: left;
}

.tier-features li {
  font-size: 12px;
  color: #6b7280;
  padding: 4px 0;
}
</style>
