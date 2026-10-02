<template>
  <div class="glass-stepper">
    <div class="stepper-header">
      <div
        v-for="(step, index) in steps"
        :key="index"
        class="step-item"
        :class="{
          'is-active': currentStep === index,
          'is-completed': currentStep > index
        }"
      >
        <div class="step-circle">
          <svg v-if="currentStep > index" width="16" height="16" viewBox="0 0 16 16" fill="none">
            <path d="M3 8L7 12L13 4" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
          <span v-else>{{ index + 1 }}</span>
        </div>
        <span class="step-label">{{ step.label }}</span>
        <div v-if="index < steps.length - 1" class="step-line"></div>
      </div>
    </div>
    <div class="stepper-content">
      <slot :currentStep="currentStep"></slot>
    </div>
    <div class="stepper-actions">
      <GlassButton
        v-if="currentStep > 0"
        variant="ghost"
        @click="prev"
      >
        上一步
      </GlassButton>
      <GlassButton
        v-if="currentStep < steps.length - 1"
        variant="primary"
        @click="next"
      >
        下一步
      </GlassButton>
      <GlassButton
        v-else
        variant="success"
        @click="complete"
      >
        完成
      </GlassButton>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import GlassButton from './GlassButton.vue'

const props = defineProps({
  steps: {
    type: Array,
    required: true
  }
})

const emit = defineEmits(['complete'])

const currentStep = ref(0)

function prev() {
  if (currentStep.value > 0) {
    currentStep.value--
  }
}

function next() {
  if (currentStep.value < props.steps.length - 1) {
    currentStep.value++
  }
}

function complete() {
  emit('complete')
}
</script>

<style scoped>
.glass-stepper {
  padding: 24px;
}

.stepper-header {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 32px;
}

.step-item {
  display: flex;
  align-items: center;
  gap: 12px;
  position: relative;
}

.step-circle {
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.1);
  border: 2px solid rgba(255, 255, 255, 0.2);
  color: rgba(255, 255, 255, 0.5);
  font-weight: 600;
  transition: all 0.3s ease;
}

.step-item.is-active .step-circle {
  background: linear-gradient(135deg, #667eea, #764ba2);
  border-color: transparent;
  color: white;
}

.step-item.is-completed .step-circle {
  background: rgba(16, 185, 129, 0.2);
  border-color: #10b981;
  color: #10b981;
}

.step-label {
  font-size: 14px;
  font-weight: 600;
  color: rgba(255, 255, 255, 0.5);
  white-space: nowrap;
}

.step-item.is-active .step-label {
  color: white;
}

.step-line {
  width: 60px;
  height: 2px;
  background: rgba(255, 255, 255, 0.2);
  margin: 0 12px;
}

.stepper-content {
  min-height: 200px;
  margin-bottom: 24px;
}

.stepper-actions {
  display: flex;
  justify-content: flex-end;
  gap: 12px;
}
</style>
