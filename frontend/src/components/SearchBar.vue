<template>
  <div class="search-bar" :class="{ 'is-focused': isFocused }">
    <div class="search-bar__icon">
      <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
        <path d="M9 0C4.03 0 0 4.03 0 9C0 13.97 4.03 18 9 18C13.97 18 18 13.97 18 9C18 4.03 13.97 0 9 0ZM9 16C5.14 16 2 12.86 2 9C2 5.14 5.14 2 9 2C12.86 2 16 5.14 16 9C16 12.86 12.86 16 9 16Z" fill="currentColor"/>
        <path d="M19.71 18.29L16.31 14.89C16.11 14.69 15.72 14.69 15.52 14.89C15.32 15.09 15.32 15.48 15.52 15.68L18.92 19.08C19.12 19.28 19.51 19.28 19.71 19.08C19.91 18.88 19.91 18.49 19.71 18.29Z" fill="currentColor"/>
      </svg>
    </div>
    <input
      ref="inputRef"
      type="text"
      class="search-bar__input"
      :placeholder="placeholder"
      :value="modelValue"
      @input="onInput"
      @focus="onFocus"
      @blur="onBlur"
      @keyup.enter="onSearch"
    />
    <button v-if="modelValue" class="search-bar__clear" @click="onClear">
      <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
        <path d="M12 4L4 12M4 4L12 12" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
      </svg>
    </button>
    <button class="search-bar__button" @click="onSearch">
      搜索
    </button>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const props = defineProps({
  modelValue: {
    type: String,
    default: ''
  },
  placeholder: {
    type: String,
    default: '搜索...'
  }
})

const emit = defineEmits(['update:modelValue', 'search', 'clear'])

const inputRef = ref(null)
const isFocused = ref(false)

function onInput(e) {
  emit('update:modelValue', e.target.value)
}

function onFocus() {
  isFocused.value = true
}

function onBlur() {
  isFocused.value = false
}

function onSearch() {
  emit('search', props.modelValue)
}

function onClear() {
  emit('update:modelValue', '')
  emit('clear')
  inputRef.value?.focus()
}
</script>

<style scoped>
.search-bar {
  display: flex;
  align-items: center;
  background: white;
  border: 2px solid #e5e7eb;
  border-radius: 12px;
  padding: 4px;
  transition: all 0.3s ease;
}

.search-bar.is-focused {
  border-color: #667eea;
  box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
}

.search-bar__icon {
  padding: 8px 12px;
  color: #9ca3af;
}

.search-bar__input {
  flex: 1;
  border: none;
  outline: none;
  font-size: 16px;
  padding: 8px 0;
  background: transparent;
}

.search-bar__input::placeholder {
  color: #9ca3af;
}

.search-bar__clear {
  background: none;
  border: none;
  cursor: pointer;
  padding: 8px;
  color: #9ca3af;
  transition: color 0.2s;
}

.search-bar__clear:hover {
  color: #4b5563;
}

.search-bar__button {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border: none;
  border-radius: 8px;
  padding: 10px 20px;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.search-bar__button:hover {
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
}
</style>
