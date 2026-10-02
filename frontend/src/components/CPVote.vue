<template>
  <div class="cp-vote">
    <div class="cp-header">
      <h3 class="cp-title">CP投票</h3>
      <p class="cp-subtitle">你觉得他们配不配？</p>
    </div>

    <div class="cp-candidates">
      <div class="candidate">
        <div class="candidate-avatar">
          <SVGMorph shape="blob" :size="60" :color1="color1" :color2="color2" />
        </div>
        <span class="candidate-name">{{ personA }}</span>
      </div>
      <div class="cp-heart">
        <svg width="32" height="32" viewBox="0 0 24 24" fill="none">
          <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5C2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3C19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z" fill="#f093fb"/>
        </svg>
      </div>
      <div class="candidate">
        <div class="candidate-avatar">
          <SVGMorph shape="blob" :size="60" :color1="color2" :color2="color1" />
        </div>
        <span class="candidate-name">{{ personB }}</span>
      </div>
    </div>

    <div class="cp-actions">
      <GlassButton
        variant="primary"
        :disabled="hasVoted"
        @click="vote('yes')"
      >
        配 ({{ yesPercent }}%)
      </GlassButton>
      <GlassButton
        variant="ghost"
        :disabled="hasVoted"
        @click="vote('no')"
      >
        不配 ({{ noPercent }}%)
      </GlassButton>
    </div>

    <div v-if="hasVoted" class="cp-result">
      <p>感谢参与！结果将在投票结束后公布</p>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import GlassButton from './GlassButton.vue'
import SVGMorph from './SVGMorph.vue'

const props = defineProps({
  personA: {
    type: String,
    required: true
  },
  personB: {
    type: String,
    required: true
  },
  yesVotes: {
    type: Number,
    default: 0
  },
  noVotes: {
    type: Number,
    default: 0
  },
  color1: {
    type: String,
    default: '#f093fb'
  },
  color2: {
    type: String,
    default: '#f5576c'
  }
})

const emit = defineEmits(['vote'])

const hasVoted = ref(false)
const userVote = ref(null)

const totalVotes = computed(() => props.yesVotes + props.noVotes)
const yesPercent = computed(() => {
  if (totalVotes.value === 0) return 50
  return Math.round((props.yesVotes / totalVotes.value) * 100)
})
const noPercent = computed(() => {
  if (totalVotes.value === 0) return 50
  return Math.round((props.noVotes / totalVotes.value) * 100)
})

function vote(type) {
  hasVoted.value = true
  userVote.value = type
  emit('vote', type)
}
</script>

<style scoped>
.cp-vote {
  padding: 24px;
}

.cp-header {
  text-align: center;
  margin-bottom: 24px;
}

.cp-title {
  font-size: 20px;
  font-weight: 700;
  color: #1f2937;
  margin-bottom: 4px;
}

.cp-subtitle {
  font-size: 14px;
  color: #6b7280;
}

.cp-candidates {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 24px;
  margin-bottom: 24px;
}

.candidate {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
}

.candidate-avatar {
  width: 60px;
  height: 60px;
}

.candidate-name {
  font-size: 14px;
  font-weight: 600;
  color: #374151;
}

.cp-heart {
  animation: pulse 1.5s ease-in-out infinite;
}

.cp-actions {
  display: flex;
  gap: 12px;
  justify-content: center;
}

.cp-result {
  text-align: center;
  margin-top: 16px;
  padding: 12px;
  background: rgba(102, 126, 234, 0.1);
  border-radius: 8px;
}

.cp-result p {
  font-size: 14px;
  color: #667eea;
}

@keyframes pulse {
  0%, 100% { transform: scale(1); }
  50% { transform: scale(1.1); }
}
</style>
