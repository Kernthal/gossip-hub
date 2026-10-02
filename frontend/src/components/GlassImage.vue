<template>
  <div class="glass-image" :class="{ 'is-loading': loading }">
    <div class="image-container">
      <img
        v-if="!error"
        :src="src"
        :alt="alt"
        :style="{ objectFit: fit }"
        @load="onLoad"
        @error="onError"
      />
      <div v-else class="image-error">
        <svg width="48" height="48" viewBox="0 0 48 48" fill="none">
          <circle cx="24" cy="24" r="22" stroke="rgba(255,255,255,0.2)" stroke-width="2"/>
          <path d="M24 16V24L30 28" stroke="rgba(255,255,255,0.2)" stroke-width="2" stroke-linecap="round"/>
        </svg>
        <p>加载失败</p>
      </div>
      <div v-if="loading" class="image-loading">
        <Loader type="spinner" />
      </div>
      <div v-if="overlay" class="image-overlay">
        <slot name="overlay"></slot>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import Loader from './Loader.vue'

const props = defineProps({
  src: {
    type: String,
    required: true
  },
  alt: {
    type: String,
    default: ''
  },
  fit: {
    type: String,
    default: 'cover',
    validator: (v) => ['cover', 'contain', 'fill', 'none', 'scale-down'].includes(v)
  },
  overlay: {
    type: Boolean,
    default: false
  }
})

const loading = ref(true)
const error = ref(false)

function onLoad() {
  loading.value = false
}

function onError() {
  loading.value = false
  error.value = true
}
</script>

<style scoped>
.glass-image {
  position: relative;
  border-radius: 12px;
  overflow: hidden;
  background: rgba(255, 255, 255, 0.1);
}

.image-container {
  position: relative;
  width: 100%;
  height: 100%;
  min-height: 200px;
}

.image-container img {
  width: 100%;
  height: 100%;
  display: block;
}

.image-error {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  color: rgba(255, 255, 255, 0.5);
  font-size: 14px;
}

.image-loading {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(0, 0, 0, 0.3);
}

.image-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>
