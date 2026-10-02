<template>
  <div class="post-page">
    <h1 class="post-page-title">发布八卦</h1>

    <LiquidGlass variant="card">
      <div class="post-form">
        <div class="form-group">
          <label class="form-label">类型</label>
          <div class="type-selector">
            <button
              v-for="type in types"
              :key="type.key"
              class="type-option"
              :class="{ 'is-selected': selectedType === type.key }"
              @click="selectedType = type.key"
            >
              <SVGMorph :shape="type.shape" :size="40" :color1="type.color1" :color2="type.color2" />
              <span>{{ type.label }}</span>
            </button>
          </div>
        </div>

        <div class="form-group">
          <label class="form-label">内容</label>
          <textarea
            v-model="content"
            class="form-textarea"
            placeholder="分享你知道的小道消息..."
            rows="6"
          ></textarea>
        </div>

        <div class="form-group">
          <label class="form-label">图片/视频</label>
          <div class="media-upload">
            <div v-if="mediaFiles.length > 0" class="media-preview">
              <div v-for="(file, index) in mediaFiles" :key="index" class="media-item">
                <img v-if="file.type === 'image'" :src="file.url" class="media-thumb" />
                <video v-else :src="file.url" class="media-thumb"></video>
                <button class="media-remove" @click="removeMedia(index)">x</button>
              </div>
            </div>
            <label class="upload-button">
              <input type="file" accept="image/*,video/*" multiple @change="onFileChange" hidden />
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
                <path d="M12 5V19M5 12H19" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
              </svg>
              <span>添加图片/视频</span>
            </label>
          </div>
        </div>

        <div class="form-group">
          <label class="form-label">匿名发布</label>
          <div class="anonymous-toggle">
            <button
              class="toggle-button"
              :class="{ 'is-active': isAnonymous }"
              @click="isAnonymous = !isAnonymous"
            >
              <span class="toggle-slider"></span>
            </button>
            <span class="toggle-label">{{ isAnonymous ? '匿名' : '实名' }}</span>
          </div>
        </div>

        <div class="form-actions">
          <GlassButton variant="primary" :loading="submitting" @click="submit">
            发布
          </GlassButton>
          <GlassButton variant="ghost" @click="$router.back()">
            取消
          </GlassButton>
        </div>
      </div>
    </LiquidGlass>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import LiquidGlass from '../components/LiquidGlass.vue'
import SVGMorph from '../components/SVGMorph.vue'
import GlassButton from '../components/GlassButton.vue'

const router = useRouter()

const types = [
  { key: 'gossip', label: '八卦爆料', shape: 'blob', color1: '#667eea', color2: '#764ba2' },
  { key: 'cp', label: 'CP配对', shape: 'heart', color1: '#f093fb', color2: '#f5576c' },
  { key: 'prediction', label: '八卦预测', shape: 'star', color1: '#fa709a', color2: '#fee140' }
]

const selectedType = ref('gossip')
const content = ref('')
const mediaFiles = ref([])
const isAnonymous = ref(true)
const submitting = ref(false)

function onFileChange(e) {
  const files = Array.from(e.target.files)
  files.forEach(file => {
    const url = URL.createObjectURL(file)
    mediaFiles.value.push({
      type: file.type.startsWith('video') ? 'video' : 'image',
      url,
      file
    })
  })
}

function removeMedia(index) {
  URL.revokeObjectURL(mediaFiles.value[index].url)
  mediaFiles.value.splice(index, 1)
}

async function submit() {
  if (!content.value.trim()) {
    alert('请输入内容')
    return
  }

  submitting.value = true

  try {
    // TODO: 调用 API 发布
    await new Promise(resolve => setTimeout(resolve, 1000))
    router.push('/timeline')
  } catch (error) {
    alert('发布失败，请重试')
  } finally {
    submitting.value = false
  }
}
</script>

<style scoped>
.post-page {
  max-width: 600px;
  margin: 0 auto;
  padding: 40px 24px;
}

.post-page-title {
  font-size: 36px;
  font-weight: 800;
  color: white;
  text-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
  margin-bottom: 32px;
}

.post-form {
  padding: 32px;
}

.form-group {
  margin-bottom: 24px;
}

.form-label {
  display: block;
  font-size: 14px;
  font-weight: 600;
  color: #374151;
  margin-bottom: 12px;
}

.type-selector {
  display: flex;
  gap: 12px;
}

.type-option {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  padding: 16px;
  border: 2px solid transparent;
  border-radius: 12px;
  background: rgba(102, 126, 234, 0.05);
  cursor: pointer;
  transition: all 0.3s ease;
}

.type-option:hover {
  background: rgba(102, 126, 234, 0.1);
}

.type-option.is-selected {
  border-color: #667eea;
  background: rgba(102, 126, 234, 0.15);
}

.type-option span {
  font-size: 14px;
  font-weight: 600;
  color: #374151;
}

.form-textarea {
  width: 100%;
  padding: 16px;
  border: 2px solid #e5e7eb;
  border-radius: 12px;
  font-size: 16px;
  font-family: inherit;
  resize: vertical;
  transition: all 0.3s ease;
}

.form-textarea:focus {
  outline: none;
  border-color: #667eea;
  box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
}

.media-upload {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.media-preview {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
}

.media-item {
  position: relative;
  width: 100px;
  height: 100px;
}

.media-thumb {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 8px;
}

.media-remove {
  position: absolute;
  top: -8px;
  right: -8px;
  width: 24px;
  height: 24px;
  border: none;
  border-radius: 50%;
  background: #ef4444;
  color: white;
  font-size: 14px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
}

.upload-button {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  padding: 32px;
  border: 2px dashed #e5e7eb;
  border-radius: 12px;
  cursor: pointer;
  transition: all 0.3s ease;
  color: #9ca3af;
}

.upload-button:hover {
  border-color: #667eea;
  color: #667eea;
}

.anonymous-toggle {
  display: flex;
  align-items: center;
  gap: 12px;
}

.toggle-button {
  position: relative;
  width: 50px;
  height: 28px;
  border: none;
  border-radius: 14px;
  background: #e5e7eb;
  cursor: pointer;
  transition: all 0.3s ease;
}

.toggle-button.is-active {
  background: #667eea;
}

.toggle-slider {
  position: absolute;
  top: 3px;
  left: 3px;
  width: 22px;
  height: 22px;
  border-radius: 50%;
  background: white;
  transition: all 0.3s ease;
}

.toggle-button.is-active .toggle-slider {
  left: 25px;
}

.toggle-label {
  font-size: 14px;
  font-weight: 600;
  color: #374151;
}

.form-actions {
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}
</style>
