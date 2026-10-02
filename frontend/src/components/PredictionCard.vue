<template>
  <div class="prediction-card">
    <div class="prediction-header">
      <div class="prediction-icon">
        <SVGMorph shape="star" :size="40" color1="#fa709a" color2="#fee140" />
      </div>
      <div class="prediction-info">
        <h4 class="prediction-title">{{ title }}</h4>
        <p class="prediction-desc">{{ description }}</p>
      </div>
    </div>

    <div class="prediction-content">
      <p class="prediction-text">{{ content }}</p>
    </div>

    <div class="prediction-meta">
      <div class="meta-item">
        <span class="meta-label">目标日期</span>
        <span class="meta-value">{{ targetDate }}</span>
      </div>
      <div class="meta-item">
        <span class="meta-label">AI置信度</span>
        <span class="meta-value">{{ aiConfidence }}%</span>
      </div>
    </div>

    <div class="prediction-actions">
      <GlassButton
        variant="primary"
        size="small"
        :disabled="hasBet"
        @click="bet('yes')"
      >
        押注发生 ({{ yesBets }})
      </GlassButton>
      <GlassButton
        variant="ghost"
        size="small"
        :disabled="hasBet"
        @click="bet('no')"
      >
        押注不发生 ({{ noBets }})
      </GlassButton>
    </div>

    <div v-if="hasBet" class="prediction-result">
      <p>已押注 {{ userBet === 'yes' ? '发生' : '不发生' }}</p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import GlassButton from './GlassButton.vue'
import SVGMorph from './SVGMorph.vue'

const props = defineProps({
  title: {
    type: String,
    required: true
  },
  description: {
    type: String,
    default: ''
  },
  content: {
    type: String,
    required: true
  },
  targetDate: {
    type: String,
    default: ''
  },
  aiConfidence: {
    type: Number,
    default: 50
  },
  yesBets: {
    type: Number,
    default: 0
  },
  noBets: {
    type: Number,
    default: 0
  }
})

const emit = defineEmits(['bet'])

const hasBet = ref(false)
const userBet = ref(null)

function bet(type) {
  hasBet.value = true
  userBet.value = type
  emit('bet', type)
}
</script>

<style scoped>
.prediction-card {
  padding: 20px;
}

.prediction-header {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 16px;
}

.prediction-icon {
  width: 40px;
  height: 40px;
  flex-shrink: 0;
}

.prediction-title {
  font-size: 16px;
  font-weight: 700;
  color: #1f2937;
  margin-bottom: 4px;
}

.prediction-desc {
  font-size: 12px;
  color: #6b7280;
}

.prediction-content {
  margin-bottom: 16px;
}

.prediction-text {
  font-size: 14px;
  color: #374151;
  line-height: 1.6;
}

.prediction-meta {
  display: flex;
  gap: 16px;
  margin-bottom: 16px;
  padding: 12px;
  background: rgba(102, 126, 234, 0.05);
  border-radius: 8px;
}

.meta-item {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.meta-label {
  font-size: 12px;
  color: #9ca3af;
}

.meta-value {
  font-size: 14px;
  font-weight: 600;
  color: #667eea;
}

.prediction-actions {
  display: flex;
  gap: 12px;
}

.prediction-result {
  text-align: center;
  margin-top: 12px;
  padding: 8px;
  background: rgba(102, 126, 234, 0.1);
  border-radius: 8px;
}

.prediction-result p {
  font-size: 14px;
  color: #667eea;
}
</style>
