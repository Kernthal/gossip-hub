<template>
  <div class="glass-timeline">
    <div v-for="(item, index) in items" :key="item.id" class="timeline-item">
      <div class="timeline-marker">
        <div class="marker-dot"></div>
        <div v-if="index < items.length - 1" class="marker-line"></div>
      </div>
      <div class="timeline-content">
        <div class="content-card">
          <div class="content-header">
            <span class="content-time">{{ item.time }}</span>
            <span class="content-badge" :class="`badge-${item.type}`">{{ item.type }}</span>
          </div>
          <p class="content-text">{{ item.content }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  items: {
    type: Array,
    required: true
  }
})
</script>

<style scoped>
.glass-timeline {
  position: relative;
  padding-left: 24px;
}

.timeline-item {
  position: relative;
  padding-bottom: 24px;
}

.timeline-marker {
  position: absolute;
  left: -24px;
  top: 0;
  bottom: 0;
  width: 24px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.marker-dot {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: linear-gradient(135deg, #667eea, #764ba2);
  border: 2px solid white;
  box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.3);
  flex-shrink: 0;
}

.marker-line {
  flex: 1;
  width: 2px;
  background: linear-gradient(180deg, rgba(102, 126, 234, 0.5), rgba(118, 75, 162, 0.5));
  margin-top: 4px;
}

.timeline-content {
  margin-left: 16px;
}

.content-card {
  padding: 16px;
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  border-radius: 12px;
  border: 1px solid rgba(255, 255, 255, 0.2);
  transition: all 0.3s ease;
}

.content-card:hover {
  background: rgba(255, 255, 255, 0.15);
  transform: translateX(4px);
}

.content-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 8px;
}

.content-time {
  font-size: 12px;
  color: rgba(255, 255, 255, 0.5);
}

.content-badge {
  padding: 2px 8px;
  border-radius: 4px;
  font-size: 10px;
  font-weight: 600;
  text-transform: uppercase;
}

.badge-gossip {
  background: rgba(102, 126, 234, 0.2);
  color: #667eea;
}

.badge-cp {
  background: rgba(240, 147, 251, 0.2);
  color: #f093fb;
}

.badge-prediction {
  background: rgba(79, 172, 254, 0.2);
  color: #4facfe;
}

.content-text {
  font-size: 14px;
  color: rgba(255, 255, 255, 0.8);
  line-height: 1.6;
}
</style>
