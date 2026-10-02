<template>
  <div class="space-y-6">
    <h1 class="text-2xl font-bold text-gray-900">我的</h1>

    <div class="bg-white rounded-lg shadow p-6">
      <div class="flex items-center space-x-4 mb-6">
        <div class="w-16 h-16 bg-gray-200 rounded-full"></div>
        <div>
          <h2 class="text-xl font-semibold text-gray-900">{{ user.name }}</h2>
          <p class="text-gray-500">{{ user.email }}</p>
        </div>
      </div>

      <div class="grid grid-cols-2 gap-4 mb-6">
        <div class="bg-gray-50 rounded-lg p-4">
          <p class="text-sm text-gray-500">匿名额度</p>
          <p class="text-2xl font-bold text-gray-900">{{ user.anonymous_quota }}</p>
        </div>
        <div class="bg-gray-50 rounded-lg p-4">
          <p class="text-sm text-gray-500">虚拟货币</p>
          <p class="text-2xl font-bold text-gray-900">{{ user.coins }}</p>
        </div>
      </div>

      <div class="space-y-3">
        <button class="w-full text-left px-4 py-3 bg-gray-50 rounded-lg hover:bg-gray-100">
          <span class="font-medium text-gray-900">会员中心</span>
          <span class="text-sm text-gray-500 float-right">升级会员享更多权益</span>
        </button>
        <button class="w-full text-left px-4 py-3 bg-gray-50 rounded-lg hover:bg-gray-100">
          <span class="font-medium text-gray-900">我的发布</span>
          <span class="text-sm text-gray-500 float-right">查看历史发布</span>
        </button>
        <button class="w-full text-left px-4 py-3 bg-gray-50 rounded-lg hover:bg-gray-100">
          <span class="font-medium text-gray-900">设置</span>
          <span class="text-sm text-gray-500 float-right">账号设置</span>
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const user = ref({
  name: '未登录',
  email: '',
  anonymous_quota: 0,
  coins: 0
})

onMounted(async () => {
  // TODO: 从 API 获取用户信息
})
</script>
