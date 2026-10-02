<template>
  <div class="glass-audio">
    <div class="audio-container">
      <audio ref="audioRef" :src="src" @timeupdate="onTimeUpdate" @loadedmetadata="onLoadedMetadata" @ended="onEnded"></audio>
      <div class="audio-info">
        <div class="audio-title">{{ title }}</div>
        <div class="audio-artist">{{ artist }}</div>
      </div>
      <div class="audio-controls">
        <button class="control-button" @click="togglePlay">
          <svg v-if="!isPlaying" width="24" height="24" viewBox="0 0 24 24" fill="none">
            <path d="M8 5V19L19 12L8 5Z" fill="currentColor"/>
          </svg>
          <svg v-else width="24" height="24" viewBox="0 0 24 24" fill="none">
            <path d="M6 4H10V20H6V4ZM14 4H18V20H14V4Z" fill="currentColor"/>
          </svg>
        </button>
        <div class="progress-bar" @click="seek">
          <div class="progress-fill" :style="{ width: progress + '%' }"></div>
        </div>
        <span class="time-display">{{ currentTime }} / {{ duration }}</span>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const props = defineProps({
  src: {
    type: String,
    required: true
  },
  title: {
    type: String,
    default: 'Unknown'
  },
  artist: {
    type: String,
    default: 'Unknown'
  }
})

const emit = defineEmits(['play', 'pause', 'ended', 'timeupdate'])

const audioRef = ref(null)
const isPlaying = ref(false)
const currentTime = ref('0:00')
const duration = ref('0:00')
const progress = ref(0)

onMounted(() => {
  if (audioRef.value) {
    audioRef.value.addEventListener('loadedmetadata', onLoadedMetadata)
  }
})

onUnmounted(() => {
  if (audioRef.value) {
    audioRef.value.removeEventListener('loadedmetadata', onLoadedMetadata)
  }
})

function onLoadedMetadata() {
  if (audioRef.value) {
    duration.value = formatTime(audioRef.value.duration)
  }
}

function togglePlay() {
  if (isPlaying.value) {
    audioRef.value?.pause()
  } else {
    audioRef.value?.play()
  }
}

function onTimeUpdate() {
  if (audioRef.value) {
    currentTime.value = formatTime(audioRef.value.currentTime)
    progress.value = (audioRef.value.currentTime / audioRef.value.duration) * 100
    emit('timeupdate', audioRef.value.currentTime)
  }
}

function onEnded() {
  isPlaying.value = false
  emit('ended')
}

function seek(e) {
  if (!audioRef.value) return
  const rect = e.currentTarget.getBoundingClientRect()
  const percent = (e.clientX - rect.left) / rect.width
  audioRef.value.currentTime = percent * audioRef.value.duration
}

function formatTime(seconds) {
  const mins = Math.floor(seconds / 60)
  const secs = Math.floor(seconds % 60)
  return `${mins}:${secs.toString().padStart(2, '0')}`
}
</script>

<style scoped>
.glass-audio {
  padding: 16px;
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  border-radius: 12px;
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.audio-container {
  display: flex;
  align-items: center;
  gap: 16px;
}

.audio-info {
  flex: 1;
  min-width: 0;
}

.audio-title {
  font-size: 14px;
  font-weight: 600;
  color: white;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.audio-artist {
  font-size: 12px;
  color: rgba(255, 255, 255, 0.5);
}

.audio-controls {
  display: flex;
  align-items: center;
  gap: 12px;
}

.control-button {
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  border: none;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.1);
  color: white;
  cursor: pointer;
  transition: all 0.2s ease;
}

.control-button:hover {
  background: rgba(255, 255, 255, 0.2);
}

.progress-bar {
  width: 100px;
  height: 4px;
  background: rgba(255, 255, 255, 0.3);
  border-radius: 2px;
  cursor: pointer;
  position: relative;
}

.progress-fill {
  height: 100%;
  background: linear-gradient(90deg, #667eea, #764ba2);
  border-radius: 2px;
  transition: width 0.1s ease;
}

.time-display {
  font-size: 12px;
  color: rgba(255, 255, 255, 0.7);
  white-space: nowrap;
}
</style>
