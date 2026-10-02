<template>
  <div class="login-page">
    <LiquidGlass variant="card" class="login-card">
      <div class="login-content">
        <div class="login-header">
          <h1 class="login-title">欢迎回来</h1>
          <p class="login-subtitle">登录你的 Gossip Hub 账号</p>
        </div>

        <form class="login-form" @submit.prevent="onLogin">
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
              placeholder="输入密码"
              label="密码"
            />
          </div>

          <div class="form-options">
            <label class="remember-me">
              <input type="checkbox" v-model="rememberMe" />
              <span>记住我</span>
            </label>
            <a href="#" class="forgot-password">忘记密码？</a>
          </div>

          <GlassButton
            type="submit"
            variant="primary"
            :loading="loading"
            class="login-button"
          >
            登录
          </GlassButton>
        </form>

        <div class="login-footer">
          <p>还没有账号？</p>
          <router-link to="/register" class="register-link">立即注册</router-link>
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

const email = ref('')
const password = ref('')
const rememberMe = ref(false)
const loading = ref(false)

async function onLogin() {
  if (!email.value || !password.value) {
    alert('请输入邮箱和密码')
    return
  }

  loading.value = true

  try {
    // TODO: 调用登录 API
    await new Promise(resolve => setTimeout(resolve, 1000))
    router.push('/')
  } catch (error) {
    alert('登录失败，请检查邮箱和密码')
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.login-page {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px;
}

.login-card {
  width: 100%;
  max-width: 400px;
}

.login-content {
  padding: 40px;
}

.login-header {
  text-align: center;
  margin-bottom: 32px;
}

.login-title {
  font-size: 28px;
  font-weight: 800;
  color: #1f2937;
  margin-bottom: 8px;
}

.login-subtitle {
  font-size: 14px;
  color: #6b7280;
}

.login-form {
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

.form-options {
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 14px;
}

.remember-me {
  display: flex;
  align-items: center;
  gap: 8px;
  color: #6b7280;
  cursor: pointer;
}

.remember-me input {
  width: 16px;
  height: 16px;
  accent-color: #667eea;
}

.forgot-password {
  color: #667eea;
  text-decoration: none;
}

.forgot-password:hover {
  text-decoration: underline;
}

.login-button {
  width: 100%;
  margin-top: 8px;
}

.login-footer {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  margin-top: 24px;
  font-size: 14px;
  color: #6b7280;
}

.register-link {
  color: #667eea;
  text-decoration: none;
  font-weight: 600;
}

.register-link:hover {
  text-decoration: underline;
}
</style>
