<template>
  <div class="settings-page">
    <h1 class="settings-title">设置</h1>

    <div class="settings-sections">
      <LiquidGlass variant="card">
        <div class="settings-section">
          <h3 class="section-title">账号设置</h3>
          <div class="settings-items">
            <div class="settings-item">
              <div class="item-info">
                <h4 class="item-title">修改密码</h4>
                <p class="item-desc">更改你的登录密码</p>
              </div>
              <GlassButton variant="ghost" @click="showChangePassword = true">
                修改
              </GlassButton>
            </div>
            <div class="settings-item">
              <div class="item-info">
                <h4 class="item-title">绑定邮箱</h4>
                <p class="item-desc">{{ user.email || '未绑定' }}</p>
              </div>
              <GlassButton variant="ghost" @click="showChangeEmail = true">
                修改
              </GlassButton>
            </div>
          </div>
        </div>
      </LiquidGlass>

      <LiquidGlass variant="card">
        <div class="settings-section">
          <h3 class="section-title">隐私设置</h3>
          <div class="settings-items">
            <div class="settings-item">
              <div class="item-info">
                <h4 class="item-title">匿名发布</h4>
                <p class="item-desc">默认匿名发布八卦</p>
              </div>
              <button
                class="toggle-button"
                :class="{ 'is-active': settings.anonymousByDefault }"
                @click="settings.anonymousByDefault = !settings.anonymousByDefault"
              >
                <span class="toggle-slider"></span>
              </button>
            </div>
            <div class="settings-item">
              <div class="item-info">
                <h4 class="item-title">公开个人资料</h4>
                <p class="item-desc">允许其他用户查看你的资料</p>
              </div>
              <button
                class="toggle-button"
                :class="{ 'is-active': settings.publicProfile }"
                @click="settings.publicProfile = !settings.publicProfile"
              >
                <span class="toggle-slider"></span>
              </button>
            </div>
          </div>
        </div>
      </LiquidGlass>

      <LiquidGlass variant="card">
        <div class="settings-section">
          <h3 class="section-title">通知设置</h3>
          <div class="settings-items">
            <div class="settings-item">
              <div class="item-info">
                <h4 class="item-title">推送通知</h4>
                <p class="item-desc">接收系统推送通知</p>
              </div>
              <button
                class="toggle-button"
                :class="{ 'is-active': settings.pushNotifications }"
                @click="settings.pushNotifications = !settings.pushNotifications"
              >
                <span class="toggle-slider"></span>
              </button>
            </div>
            <div class="settings-item">
              <div class="item-info">
                <h4 class="item-title">邮件通知</h4>
                <p class="item-desc">接收邮件通知</p>
              </div>
              <button
                class="toggle-button"
                :class="{ 'is-active': settings.emailNotifications }"
                @click="settings.emailNotifications = !settings.emailNotifications"
              >
                <span class="toggle-slider"></span>
              </button>
            </div>
          </div>
        </div>
      </LiquidGlass>

      <LiquidGlass variant="card">
        <div class="settings-section">
          <h3 class="section-title">其他</h3>
          <div class="settings-items">
            <div class="settings-item">
              <div class="item-info">
                <h4 class="item-title">清除缓存</h4>
                <p class="item-desc">清除本地缓存数据</p>
              </div>
              <GlassButton variant="ghost" @click="clearCache">
                清除
              </GlassButton>
            </div>
            <div class="settings-item">
              <div class="item-info">
                <h4 class="item-title">退出登录</h4>
                <p class="item-desc">退出当前账号</p>
              </div>
              <GlassButton variant="danger" @click="logout">
                退出
              </GlassButton>
            </div>
          </div>
        </div>
      </LiquidGlass>
    </div>

    <GlassModal v-model="showChangePassword" title="修改密码">
      <div class="modal-form">
        <div class="form-group">
          <label class="form-label">当前密码</label>
          <GlassInput type="password" placeholder="输入当前密码" label="当前密码" />
        </div>
        <div class="form-group">
          <label class="form-label">新密码</label>
          <GlassInput type="password" placeholder="输入新密码" label="新密码" />
        </div>
        <div class="form-group">
          <label class="form-label">确认新密码</label>
          <GlassInput type="password" placeholder="确认新密码" label="确认新密码" />
        </div>
        <GlassButton variant="primary" @click="changePassword">
          确认修改
        </GlassButton>
      </div>
    </GlassModal>

    <GlassModal v-model="showChangeEmail" title="修改邮箱">
      <div class="modal-form">
        <div class="form-group">
          <label class="form-label">新邮箱</label>
          <GlassInput type="email" placeholder="输入新邮箱" label="新邮箱" />
        </div>
        <div class="form-group">
          <label class="form-label">密码</label>
          <GlassInput type="password" placeholder="输入密码" label="密码" />
        </div>
        <GlassButton variant="primary" @click="changeEmail">
          确认修改
        </GlassButton>
      </div>
    </GlassModal>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import LiquidGlass from '../components/LiquidGlass.vue'
import GlassButton from '../components/GlassButton.vue'
import GlassModal from '../components/GlassModal.vue'
import GlassInput from '../components/GlassInput.vue'

const router = useRouter()

const user = ref({
  email: 'user@example.com'
})

const settings = ref({
  anonymousByDefault: true,
  publicProfile: false,
  pushNotifications: true,
  emailNotifications: false
})

const showChangePassword = ref(false)
const showChangeEmail = ref(false)

function clearCache() {
  if (confirm('确定要清除缓存吗？')) {
    localStorage.clear()
    alert('缓存已清除')
  }
}

function logout() {
  if (confirm('确定要退出登录吗？')) {
    // TODO: 调用登出 API
    router.push('/login')
  }
}

function changePassword() {
  // TODO: 实现修改密码逻辑
  showChangePassword.value = false
  alert('密码修改成功')
}

function changeEmail() {
  // TODO: 实现修改邮箱逻辑
  showChangeEmail.value = false
  alert('邮箱修改成功')
}
</script>

<style scoped>
.settings-page {
  max-width: 600px;
  margin: 0 auto;
  padding: 40px 24px;
}

.settings-title {
  font-size: 36px;
  font-weight: 800;
  color: white;
  text-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
  margin-bottom: 32px;
}

.settings-sections {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.settings-section {
  padding: 24px;
}

.section-title {
  font-size: 18px;
  font-weight: 700;
  color: #1f2937;
  margin-bottom: 16px;
}

.settings-items {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.settings-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 16px;
  background: rgba(102, 126, 234, 0.05);
  border-radius: 12px;
}

.item-title {
  font-size: 16px;
  font-weight: 600;
  color: #1f2937;
  margin-bottom: 4px;
}

.item-desc {
  font-size: 14px;
  color: #6b7280;
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

.modal-form {
  display: flex;
  flex-direction: column;
  gap: 16px;
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
</style>
