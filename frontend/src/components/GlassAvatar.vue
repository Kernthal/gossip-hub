<template>
  <div class="glass-avatar" :class="`glass-avatar--${size}`">
    <div class="avatar-ring">
      <img v-if="src" :src="src" :alt="alt" class="avatar-image" />
      <div v-else class="avatar-placeholder">
        <slot>
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
            <path d="M12 12C14.21 12 16 10.21 16 8C16 5.79 14.21 4 12 4C9.79 4 8 5.79 8 8C8 10.21 9.79 12 12 12Z" stroke="currentColor" stroke-width="2"/>
            <path d="M12 14C7.58 14 4 16.24 4 19V20H20V19C20 16.24 16.42 14 12 14Z" stroke="currentColor" stroke-width="2"/>
          </svg>
        </slot>
      </div>
    </div>
    <span v-if="status" class="avatar-status" :class="`status--${status}`"></span>
  </div>
</template>

<script setup>
defineProps({
  src: {
    type: String,
    default: ''
  },
  alt: {
    type: String,
    default: ''
  },
  size: {
    type: String,
    default: 'medium',
    validator: (v) => ['small', 'medium', 'large'].includes(v)
  },
  status: {
    type: String,
    default: '',
    validator: (v) => ['', 'online', 'offline', 'busy', 'away'].includes(v)
  }
})
</script>

<style scoped>
.glass-avatar {
  position: relative;
  display: inline-flex;
}

.avatar-ring {
  border-radius: 50%;
  padding: 3px;
  background: linear-gradient(135deg, #667eea, #764ba2);
}

.glass-avatar--small .avatar-ring {
  width: 32px;
  height: 32px;
}

.glass-avatar--medium .avatar-ring {
  width: 48px;
  height: 48px;
}

.glass-avatar--large .avatar-ring {
  width: 64px;
  height: 64px;
}

.avatar-image {
  width: 100%;
  height: 100%;
  border-radius: 50%;
  object-fit: cover;
  border: 2px solid white;
}

.avatar-placeholder {
  width: 100%;
  height: 100%;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.2);
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  border: 2px solid white;
}

.avatar-status {
  position: absolute;
  bottom: 0;
  right: 0;
  width: 12px;
  height: 12px;
  border-radius: 50%;
  border: 2px solid white;
}

.status--online {
  background: #10b981;
}

.status--offline {
  background: #9ca3af;
}

.status--busy {
  background: #ef4444;
}

.status--away {
  background: #f59e0b;
}
</style>
