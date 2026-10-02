<template>
  <div class="anonymous-qa">
    <div class="qa-header">
      <h3 class="qa-title">匿名提问箱</h3>
      <p class="qa-subtitle">匿名提问，保护隐私</p>
    </div>

    <div class="qa-form">
      <textarea
        v-model="question"
        class="qa-textarea"
        placeholder="输入你的问题..."
        rows="3"
      ></textarea>
      <GlassButton
        variant="primary"
        :loading="submitting"
        @click="submit"
      >
        提交问题
      </GlassButton>
    </div>

    <div class="qa-list">
      <div v-if="questions.length === 0" class="qa-empty">
        <EmptyState title="暂无问题" description="成为第一个提问的人吧" />
      </div>
      <div v-else class="qa-items">
        <LiquidGlass v-for="item in questions" :key="item.id" variant="card">
          <div class="qa-item">
            <div class="qa-question">
              <p class="qa-text">{{ item.question }}</p>
              <span class="qa-time">{{ item.created_at }}</span>
            </div>
            <div v-if="item.answers && item.answers.length > 0" class="qa-answers">
              <div v-for="answer in item.answers" :key="answer.id" class="qa-answer">
                <p class="answer-text">{{ answer.content }}</p>
                <span class="answer-time">{{ answer.created_at }}</span>
              </div>
            </div>
            <div class="qa-actions">
              <button class="action-button" @click="showAnswerForm = item.id">
                回答
              </button>
            </div>
            <div v-if="showAnswerForm === item.id" class="answer-form">
              <textarea
                v-model="answerText"
                class="answer-textarea"
                placeholder="输入你的回答..."
                rows="2"
              ></textarea>
              <GlassButton
                variant="primary"
                size="small"
                @click="submitAnswer(item.id)"
              >
                提交回答
              </GlassButton>
            </div>
          </div>
        </LiquidGlass>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import LiquidGlass from './LiquidGlass.vue'
import GlassButton from './GlassButton.vue'
import EmptyState from './EmptyState.vue'

const questions = ref([])
const question = ref('')
const answerText = ref('')
const submitting = ref(false)
const showAnswerForm = ref(null)

function submit() {
  if (!question.value.trim()) {
    alert('请输入问题')
    return
  }

  submitting.value = true

  // TODO: 调用 API 提交问题
  setTimeout(() => {
    questions.value.unshift({
      id: Date.now(),
      question: question.value,
      created_at: new Date().toLocaleString(),
      answers: []
    })
    question.value = ''
    submitting.value = false
  }, 500)
}

function submitAnswer(questionId) {
  if (!answerText.value.trim()) {
    alert('请输入回答')
    return
  }

  const item = questions.value.find(q => q.id === questionId)
  if (item) {
    if (!item.answers) item.answers = []
    item.answers.push({
      id: Date.now(),
      content: answerText.value,
      created_at: new Date().toLocaleString()
    })
  }
  answerText.value = ''
  showAnswerForm.value = null
}
</script>

<style scoped>
.anonymous-qa {
  padding: 24px;
}

.qa-header {
  text-align: center;
  margin-bottom: 24px;
}

.qa-title {
  font-size: 20px;
  font-weight: 700;
  color: #1f2937;
  margin-bottom: 4px;
}

.qa-subtitle {
  font-size: 14px;
  color: #6b7280;
}

.qa-form {
  margin-bottom: 24px;
}

.qa-textarea {
  width: 100%;
  padding: 16px;
  border: 2px solid #e5e7eb;
  border-radius: 12px;
  font-size: 14px;
  font-family: inherit;
  resize: vertical;
  margin-bottom: 12px;
  transition: all 0.3s ease;
}

.qa-textarea:focus {
  outline: none;
  border-color: #667eea;
  box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
}

.qa-empty {
  padding: 40px;
}

.qa-items {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.qa-item {
  padding: 16px;
}

.qa-question {
  margin-bottom: 12px;
}

.qa-text {
  font-size: 14px;
  color: #374151;
  line-height: 1.6;
  margin-bottom: 8px;
}

.qa-time {
  font-size: 12px;
  color: #9ca3af;
}

.qa-answers {
  margin-bottom: 12px;
  padding-left: 16px;
  border-left: 2px solid #e5e7eb;
}

.qa-answer {
  margin-bottom: 8px;
}

.answer-text {
  font-size: 14px;
  color: #4b5563;
  line-height: 1.6;
  margin-bottom: 4px;
}

.answer-time {
  font-size: 12px;
  color: #9ca3af;
}

.qa-actions {
  display: flex;
  gap: 12px;
}

.action-button {
  padding: 6px 12px;
  border: none;
  border-radius: 6px;
  background: transparent;
  color: #667eea;
  font-size: 14px;
  cursor: pointer;
  transition: all 0.2s ease;
}

.action-button:hover {
  background: rgba(102, 126, 234, 0.1);
}

.answer-form {
  margin-top: 12px;
}

.answer-textarea {
  width: 100%;
  padding: 12px;
  border: 2px solid #e5e7eb;
  border-radius: 8px;
  font-size: 14px;
  font-family: inherit;
  resize: vertical;
  margin-bottom: 8px;
}

.answer-textarea:focus {
  outline: none;
  border-color: #667eea;
}
</style>
