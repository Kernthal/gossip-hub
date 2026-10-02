<template>
  <div class="register-page">
    <LiquidGlass variant="card" class="register-card">
      <div class="register-content">
        <div class="register-header">
          <h1 class="register-title">创建账号</h1>
          <p class="register-subtitle">加入 Gossip Hub，开始你的八卦之旅</p>
        </div>

        <form class="register-form" @submit.prevent="onRegister">
          <div class="form-group">
            <label class="form-label">用户名</label>
            <GlassInput
              v-model="username"
              type="text"
              placeholder="你的用户名"
              label="用户名"
            />
          </div>

          <div class="form-group">
            <label class="form-label">邮箱</label>
            <GlassInput
              v-model="email"
              type="email"
              placeholder="your@email.com"
              label="邮箱"
            />
          </div>

          <div class="form-group">
            <label class="form-label">密码</label>
            <GlassInput
              v-model="password"
              type="password"
              placeholder="设置密码"
              label="密码"
            />
          </div>

          <div class="form-group">
            <label class="form-label">确认密码</label>
            <GlassInput
              v-model="confirmPassword"
              type="password"
              placeholder="确认密码"
              label="确认密码"
            />
          </div>

          <div class="form-group">
            <label class="form-label">班级</label>
            <select v-model="classId" class="form-select">
              <option value="">选择班级</option>
              <option v-for="cls in classes" :key="cls.id" :value="cls.id">
                {{ cls.name }}
              </option>
            </select>
          </div>

          <GlassButton
            type="submit"
            variant="primary"
            :loading="loading"
            class="register-button"
          >
            注册
          </GlassButton>
        </form>

        <div class="register-footer">
          <p>已有账号？</p>
          <router-link to="/login" class="login-link">立即登录</router-link>
        </div>
      </div>
    </LiquidGlass>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import LiquidGlass from '../components/LiquidGlass.vue'
import GlassInput from '../components/GlassInput.vue'
import GlassButton from '../components/GlassButton.vue'

const router = useRouter()

const username = ref('')
const email = ref('')
const password = ref('')
const confirmPassword = ref('')
const classId = ref('')
const loading = ref(false)

const classes = [
  { id: '1', name: '初一1班' },
  { id: '2', name: '初一2班' },
  { id: '3', name: '初二1班' },
  { id: '4', name: '初二2班' },
  { id: '5', name: '初三1班' },
  { id: '6', name: '初三2班' }
]

async function onRegister() {
  if (!username.value || !email.value || !password.value) {
    alert('请填写所有必填项')
    return
  }

  if (password.value !== confirmPassword.value) {
    alert('两次输入的密码不一致')
    return
  }

  loading.value = true

  try {
    // TODO: 调用注册 API
    await new Promise(resolve => setTimeout(resolve, 1000))
    router.push('/login')
  } catch (error) {
    alert('注册失败，请重试')
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.register-page {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px;
}

.register-card {
  width: 100%;
  max-width: 400px;
}

.register-content {
  padding: 40px;
}

.register-header {
  text-align: center;
  margin-bottom: 32px;
}

.register-title {
  font-size: 28px;
  font-weight: 800;
  color: #1f2937;
  margin-bottom: 8px;
}

.register-subtitle {
  font-size: 14px;
  color: #6b7280;
}

.register-form {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.form-label {
  font-size: 14px;
  font-weight: 600;
  color: #374151;
}

.form-select {
  width: 100%;
  padding: 16px 0;
  border: none;
  background: transparent;
  font-size: 16px;
  color: #1f2937;
  outline: none;
  border-bottom: 2px solid #e5e7eb;
}

.form-select:focus {
  border-bottom-color: #667eea;
}

.register-button {
  width: 100%;
  margin-top: 8px;
}

.register-footer {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  margin-top: 24px;
  font-size: 14px;
  color: #6b7280;
}

.login-link {
  color: #667eea;
  text-decoration: none;
  font-weight: 600;
}

.login-link:hover {
  text-decoration: underline;
}
</style>
