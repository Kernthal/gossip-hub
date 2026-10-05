<template>
  <div class="liquid-glass-wrapper">
    <div class="liquid-glass" :class="`liquid-glass--${variant}`">
      <svg class="liquid-glass__filter" xmlns="http://www.w3.org/2000/svg">
        <defs>
          <filter :id="filterId" color-interpolation-filters="sRGB">
            <feGaussianBlur in="SourceGraphic" stdDeviation="3" result="blur" />
            <feColorMatrix in="blur" type="matrix" values="1 0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0 1 0" result="alpha" />
            <feComposite in="SourceGraphic" in2="alpha" operator="in" />
          </filter>
        </defs>
      </svg>
      <div class="liquid-glass__content">
        <slot></slot>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  variant: {
    type: String,
    default: 'default',
    validator: (v) => ['default', 'card', 'button', 'pill', 'nav'].includes(v)
  },
  frost: {
    type: Number,
    default: 0.1
  },
  saturation: {
    type: Number,
    default: 1.2
  }
})

const filterId = computed(() => `glass-filter-${Math.random().toString(36).substr(2, 9)}`)
</script>

<style scoped>
.liquid-glass-wrapper {
  width: 100%;
}

.liquid-glass {
  position: relative;
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px) saturate(1.2);
  -webkit-backdrop-filter: blur(10px) saturate(1.2);
  border-radius: 16px;
  border: 1px solid rgba(255, 255, 255, 0.2);
  box-shadow:
    inset 0 0 2px 1px rgba(255, 255, 255, 0.35),
    inset 0 0 10px 4px rgba(255, 255, 255, 0.15),
    inset 0 4px 16px rgba(17, 17, 26, 0.05),
    inset 0 8px 24px rgba(17, 17, 26, 0.05),
    inset 0 6px 56px rgba(17, 17, 26, 0.05);
  overflow: hidden;
}

.liquid-glass__filter {
  position: absolute;
  width: 0;
  height: 0;
  pointer-events: none;
}

.liquid-glass__content {
  position: relative;
  z-index: 1;
}

.liquid-glass--card {
  padding: 24px;
}

.liquid-glass--button {
  padding: 12px 24px;
  border-radius: 12px;
}

.liquid-glass--pill {
  border-radius: 9999px;
  padding: 12px 32px;
}

.liquid-glass--nav {
  border-radius: 12px;
  padding: 8px 16px;
}
</style>
