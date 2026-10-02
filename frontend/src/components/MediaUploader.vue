<template>
  <div class="media-uploader">
    <div v-if="files.length > 0" class="media-preview">
      <div v-for="(file, index) in files" :key="index" class="media-item">
        <img v-if="file.type === 'image'" :src="file.url" class="media-thumb" />
        <video v-else :src="file.url" class="media-thumb" controls></video>
        <button class="media-remove" @click="removeFile(index)">
          <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
            <path d="M12 4L4 12M4 4L12 12" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
          </svg>
        </button>
        <div v-if="file.compressing" class="media-loading">
          <Loader type="spinner" />
        </div>
      </div>
    </div>
    <label class="upload-area">
      <input type="file" accept="image/*,video/*" multiple @change="onFileChange" hidden />
      <div class="upload-content">
        <svg width="32" height="32" viewBox="0 0 32 32" fill="none">
          <path d="M16 8V24M8 16H24" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
        </svg>
        <span>点击或拖拽上传</span>
        <p class="upload-hint">支持图片和视频，最大 {{ maxSize }}MB</p>
      </div>
    </label>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import Loader from './Loader.vue'

const props = defineProps({
  maxSize: {
    type: Number,
    default: 100
  },
  maxFiles: {
    type: Number,
    default: 9
  }
})

const emit = defineEmits(['update:files'])

const files = ref([])

function onFileChange(e) {
  const selectedFiles = Array.from(e.target.files)
  
  selectedFiles.forEach(file => {
    if (files.value.length >= props.maxFiles) {
      alert(`最多上传 ${props.maxFiles} 个文件`)
      return
    }

    if (file.size > props.maxSize * 1024 * 1024) {
      alert(`文件大小不能超过 ${props.maxSize}MB`)
      return
    }

    const url = URL.createObjectURL(file)
    const fileData = {
      type: file.type.startsWith('video') ? 'video' : 'image',
      url,
      file,
      compressing: false
    }
    files.value.push(fileData)
    emit('update:files', files.value)

    // 压缩文件
    compressFile(fileData)
  })
}

async function compressFile(fileData) {
  fileData.compressing = true

  try {
    if (fileData.type === 'image') {
      // 图片压缩
      const compressed = await compressImage(fileData.file)
      fileData.compressed = compressed
    } else {
      // 视频压缩（需要 FFmpeg.wasm）
      // TODO: 实现视频压缩
    }
  } catch (error) {
    console.error('压缩失败:', error)
  } finally {
    fileData.compressing = false
    emit('update:files', files.value)
  }
}

async function compressImage(file) {
  return new Promise((resolve) => {
    const img = new Image()
    img.onload = () => {
      const canvas = document.createElement('canvas')
      const ctx = canvas.getContext('2d')
      
      let width = img.width
      let height = img.height
      
      // 限制最大尺寸
      const maxSize = 1920
      if (width > maxSize || height > maxSize) {
        if (width > height) {
          height = (height / width) * maxSize
          width = maxSize
        } else {
          width = (width / height) * maxSize
          height = maxSize
        }
      }
      
      canvas.width = width
      canvas.height = height
      ctx.drawImage(img, 0, 0, width, height)
      
      // 压缩质量
      canvas.toBlob((blob) => {
        resolve(blob)
      }, 'image/jpeg', 0.7)
    }
    img.src = URL.createObjectURL(file)
  })
}

function removeFile(index) {
  URL.revokeObjectURL(files.value[index].url)
  files.value.splice(index, 1)
  emit('update:files', files.value)
}
</script>

<style scoped>
.media-uploader {
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
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
}

.media-loading {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.upload-area {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 32px;
  border: 2px dashed #e5e7eb;
  border-radius: 12px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.upload-area:hover {
  border-color: #667eea;
  background: rgba(102, 126, 234, 0.05);
}

.upload-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  color: #9ca3af;
}

.upload-hint {
  font-size: 12px;
  color: #9ca3af;
}
</style>
