<template>
  <div class="glass-video">
    <div class="video-container">
      <video
        ref="videoRef"
        :src="src"
        :poster="poster"
        :autoplay="autoplay"
        :loop="loop"
        :muted="muted"
        @play="onPlay"
        @pause="onPause"
        @ended="onEnded"
        @timeupdate="onTimeUpdate"
      ></video>
      <div v-if="!isPlaying" class="video-overlay" @click="play">
        <div class="play-button">
          <svg width="48" height="48" viewBox="0 0 48 48" fill="none">
            <circle cx="24" cy="24" r="24" fill="rgba(0,0,0,0.5)"/>
            <path d="M18 14L36 24L18 34V14Z" fill="white"/>
          </svg>
        </div>
      </div>
      <div class="video-controls">
        <button class="control-button" @click="togglePlay">
          <svg v-if="!isPlaying" width="20" height="20" viewBox="0 0 20 20" fill="none">
            <path d="M5 3L15 10L5 17V3Z" fill="currentColor"/>
          </svg>
          <svg v-else width="20" height="20" viewBox="0 0 20 20" fill="none">
            <path d="M5 3H8V17H5V3ZM12 3H15V17H12V3Z" fill="currentColor"/>
          </svg>
        </button>
        <div class="progress-bar" @click="seek">
          <div class="progress-fill" :style="{ width: progress + '%' }"></div>
        </div>
        <span class="time-display">{{ currentTime }} / {{ duration }}</span>
        <button class="control-button" @click="toggleMute">
          <svg v-if="!muted" width="20" height="20" viewBox="0 0 20 20" fill="none">
            <path d="M10 3L5 7H2V13H5L10 17V3Z" fill="currentColor"/>
            <path d="M13 7C14.5 8.5 14.5 11.5 13 13" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
          </svg>
          <svg v-else width="20" height="20" viewBox="0 0 20 20" fill="none">
            <path d="M10 3L5 7H2V13H5L10 17V3Z" fill="currentColor"/>
            <path d="M13 7L17 13M17 7L13 13" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
          </svg>
        </button>
        <button class="control-button" @click="toggleFullscreen">
          <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
            <path d="M3 7V3H7M13 3H17V7M17 13V17H13M7 17H3V13" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </button>
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
  poster: {
    type: String,
    default: ''
  },
  autoplay: {
    type: Boolean,
    default: false
  },
  loop: {
    type: Boolean,
    default: false
  },
  muted: {
    type: Boolean,
    default: false
  }
})

const emit = defineEmits(['play', 'pause', 'ended', 'timeupdate'])

const videoRef = ref(null)
const isPlaying = ref(false)
const currentTime = ref('0:00')
const duration = ref('0:00')
const progress = ref(0)

onMounted(() => {
  if (videoRef.value) {
    videoRef.value.addEventListener('loadedmetadata', onLoadedMetadata)
  }
})

onUnmounted(() => {
  if (videoRef.value) {
    videoRef.value.removeEventListener('loadedmetadata', onLoadedMetadata)
  }
})

function onLoadedMetadata() {
  if (videoRef.value) {
    duration.value = formatTime(videoRef.value.duration)
  }
}

function play() {
  videoRef.value?.play()
}

function pause() {
  videoRef.value?.pause()
}

function togglePlay() {
  if (isPlaying.value) {
    pause()
  } else {
    play()
  }
}

function onPlay() {
  isPlaying.value = true
  emit('play')
}

function onPause() {
  isPlaying.value = false
  emit('pause')
}

function onEnded() {
  isPlaying.value = false
  emit('ended')
}

function onTimeUpdate() {
  if (videoRef.value) {
    currentTime.value = formatTime(videoRef.value.currentTime)
    progress.value = (videoRef.value.currentTime / videoRef.value.duration) * 100
    emit('timeupdate', videoRef.value.currentTime)
  }
}

function seek(e) {
  if (!videoRef.value) return
  const rect = e.currentTarget.getBoundingClientRect()
  const percent = (e.clientX - rect.left) / rect.width
  videoRef.value.currentTime = percent * videoRef.value.duration
}

function toggleMute() {
  if (videoRef.value) {
    videoRef.value.muted = !videoRef.value.muted
  }
}

function toggleFullscreen() {
  if (videoRef.value) {
    if (document.fullscreenElement) {
      document.exitFullscreen()
    } else {
      videoRef.value.requestFullscreen()
    }
  }
}

function formatTime(seconds) {
  const mins = Math.floor(seconds / 60)
  const secs = Math.floor(seconds % 60)
  return `${mins}:${secs.toString().padStart(2, '0')}`
}
</script>

<style scoped>
.glass-video {
  position: relative;
  border-radius: 12px;
  overflow: hidden;
  background: black;
}

.video-container {
  position: relative;
  width: 100%;
  padding-top: 56.25%;
}

.video-container video {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.video-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(0, 0, 0, 0.3);
  cursor: pointer;
}

.play-button {
  transition: transform 0.2s ease;
}

.video-overlay:hover .play-button {
  transform: scale(1.1);
}

.video-controls {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 16px;
  background: linear-gradient(transparent, rgba(0, 0, 0, 0.7));
}

.control-button {
  width: 36px;
  height: 36px;
  display: flex;
  align-items: center;
  justify-content: center;
  border: none;
  border-radius: 8px;
  background: transparent;
  color: white;
  cursor: pointer;
  transition: all 0.2s ease;
}

.control-button:hover {
  background: rgba(255, 255, 255, 0.2);
}

.progress-bar {
  flex: 1;
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
  color: white;
  white-space: nowrap;
}
</style>
