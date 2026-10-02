<template>
  <div class="glass-rating">
    <div class="rating-stars">
      <button
        v-for="star in maxStars"
        :key="star"
        class="star-button"
        :class="{ 'is-active': star <= displayValue }"
        @mouseenter="hoverValue = star"
        @mouseleave="hoverValue = 0"
        @click="setRating(star)"
      >
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
          <path
            d="M12 2L15.09 8.26L22 9.27L17 14.14L18.18 21.02L12 17.77L5.82 21.02L7 14.14L2 9.27L8.91 8.26L12 2Z"
            :fill="star <= displayValue ? '#ffd700' : 'rgba(255,255,255,0.2)'"
            :stroke="star <= displayValue ? '#ffd700' : 'rgba(255,255,255,0.3)'"
            stroke-width="1"
          />
        </svg>
      </button>
    </div>
    <span v-if="showValue" class="rating-value">{{ displayValue }} / {{ maxStars }}</span>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const props = defineProps({
  modelValue: {
    type: Number,
    default: 0
  },
  maxStars: {
    type: Number,
    default: 5
  },
  readonly: {
    type: Boolean,
    default: false
  },
  showValue: {
    type: Boolean,
    default: true
  }
})

const emit = defineEmits(['update:modelValue'])

const hoverValue = ref(0)

const displayValue = computed(() => {
  return hoverValue.value || props.modelValue
})

function setRating(value) {
  if (!props.readonly) {
    emit('update:modelValue', value)
  }
}
</script>

<style scoped>
.glass-rating {
  display: flex;
  align-items: center;
  gap: 12px;
}

.rating-stars {
  display: flex;
  gap: 4px;
}

.star-button {
  background: none;
  border: none;
  cursor: pointer;
  padding: 4px;
  transition: transform 0.2s ease;
}

.star-button:hover {
  transform: scale(1.2);
}

.star-button.is-active {
  animation: star-pop 0.3s ease;
}

.rating-value {
  font-size: 14px;
  font-weight: 600;
  color: rgba(255, 255, 255, 0.7);
}

@keyframes star-pop {
  0% { transform: scale(1); }
  50% { transform: scale(1.3); }
  100% { transform: scale(1); }
}
</style>
