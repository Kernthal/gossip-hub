<template>
  <div class="glass-activity">
    <div class="activity-header">
      <h3 class="activity-title">最近活动</h3>
    </div>
    <div class="activity-list">
      <div v-for="activity in activities" :key="activity.id" class="activity-item">
        <div class="activity-icon" :class="`icon-${activity.type}`">
          <svg v-if="activity.type === 'post'" width="16" height="16" viewBox="0 0 16 16" fill="none">
            <path d="M8 1C4 1 1 4 1 8C1 9.5 1.5 11 2.5 12L2 15L5 13.5C6 14 7 14 8 14C12 14 15 11 15 8C15 4 12 1 8 1Z" stroke="currentColor" stroke-width="1.5"/>
          </svg>
          <svg v-else-if="activity.type === 'like'" width="16" height="16" viewBox="0 0 16 16" fill="none">
            <path d="M8 14L2 8C0.5 6.5 0.5 4 2 2.5C3.5 1 6 1 7 2.5C7.5 3 8 3.5 8 3.5C8 3.5 8.5 3 9 2.5C10 1 12.5 1 14 2.5C15.5 4 15.5 6.5 14 8L8 14Z" stroke="currentColor" stroke-width="1.5"/>
          </svg>
          <svg v-else-if="activity.type === 'comment'" width="16" height="16" viewBox="0 0 16 16" fill="none">
            <path d="M8 1C4 1 1 4 1 8C1 9.5 1.5 11 2.5 12L2 15L5 13.5C6 14 7 14 8 14C12 14 15 11 15 8C15 4 12 1 8 1Z" stroke="currentColor" stroke-width="1.5"/>
          </svg>
          <svg v-else width="16" height="16" viewBox="0 0 16 16" fill="none">
            <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-width="1.5"/>
          </svg>
        </div>
        <div class="activity-content">
          <p class="activity-text">{{ activity.text }}</p>
          <span class="activity-time">{{ activity.time }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  activities: {
    type: Array,
    required: true
  }
})
</script>

<style scoped>
.glass-activity {
  padding: 24px;
}

.activity-header {
  margin-bottom: 20px;
}

.activity-title {
  font-size: 18px;
  font-weight: 700;
  color: white;
  margin: 0;
}

.activity-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.activity-item {
  display: flex;
  align-items: flex-start;
  gap: 12px;
  padding: 16px;
  background: rgba(255, 255, 255, 0.05);
  border-radius: 12px;
  border: 1px solid rgba(255, 255, 255, 0.1);
  transition: all 0.2s ease;
}

.activity-item:hover {
  background: rgba(255, 255, 255, 0.1);
}

.activity-icon {
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 8px;
  flex-shrink: 0;
}

.icon-post {
  background: rgba(102, 126, 234, 0.2);
  color: #667eea;
}

.icon-like {
  background: rgba(240, 147, 251, 0.2);
  color: #f093fb;
}

.icon-comment {
  background: rgba(79, 172, 254, 0.2);
  color: #4facfe;
}

.activity-content {
  flex: 1;
}

.activity-text {
  font-size: 14px;
  color: rgba(255, 255, 255, 0.8);
  margin: 0 0 4px 0;
  line-height: 1.5;
}

.activity-time {
  font-size: 12px;
  color: rgba(255, 255, 255, 0.4);
}
</style>
