<template>
  <span class="typing-text">
    {{ displayedText }}<span v-if="isTyping" class="cursor">|</span>
  </span>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'

const props = defineProps({
  text: {
    type: String,
    required: true
  },
  speed: {
    type: Number,
    default: 50
  },
  delay: {
    type: Number,
    default: 0
  }
})

const displayedText = ref('')
const isTyping = ref(false)

onMounted(() => {
  setTimeout(() => {
    startTyping()
  }, props.delay)
})

watch(() => props.text, () => {
  startTyping()
})

function startTyping() {
  displayedText.value = ''
  isTyping.value = true
  let index = 0

  const interval = setInterval(() => {
    if (index < props.text.length) {
      displayedText.value += props.text[index]
      index++
    } else {
      isTyping.value = false
      clearInterval(interval)
    }
  }, props.speed)
}
</script>

<style scoped>
.typing-text {
  display: inline-block;
}

.cursor {
  animation: blink 1s infinite;
  font-weight: bold;
}

@keyframes blink {
  0%, 50% { opacity: 1; }
  51%, 100% { opacity: 0; }
}
</style>
