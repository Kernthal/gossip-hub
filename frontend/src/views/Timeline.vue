<template>
  <div class="space-y-6">
    <div class="flex justify-between items-center">
      <h1 class="text-2xl font-bold text-gray-900">时间线</h1>
      <router-link to="/post" class="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700">
        发布八卦
      </router-link>
    </div>

    <div class="flex space-x-4 border-b">
      <button
        v-for="tab in tabs"
        :key="tab.key"
        @click="activeTab = tab.key"
        :class="[
          'pb-2 px-4 font-medium text-sm',
          activeTab === tab.key
            ? 'border-b-2 border-blue-600 text-blue-600'
            : 'text-gray-500 hover:text-gray-700'
        ]"
      >
        {{ tab.label }}
      </button>
    </div>

    <div class="space-y-4">
      <div v-if="loading" class="text-center py-8">
        <p class="text-gray-500">加载中...</p>
      </div>
      <div v-else-if="posts.length === 0" class="text-center py-8">
        <p class="text-gray-500">暂无内容</p>
      </div>
      <div
        v-for="post in posts"
        :key="post.id"
        class="bg-white rounded-lg shadow p-6"
      >
        <div class="flex items-center justify-between mb-4">
          <div class="flex items-center space-x-2">
            <span class="text-sm text-gray-500">{{ post.author }}</span>
            <span class="text-xs text-gray-400">{{ post.created_at }}</span>
          </div>
          <span :class="['text-xs px-2 py-1 rounded-full', post.type_class]">
            {{ post.type }}
          </span>
        </div>
        <p class="text-gray-800 mb-4">{{ post.content }}</p>
        <div class="flex items-center space-x-6 text-sm text-gray-500">
          <span>浏览 {{ post.views }}</span>
          <span>点赞 {{ post.likes }}</span>
          <span>评论 {{ post.comments }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const tabs = [
  { key: 'latest', label: '最新' },
  { key: 'hot', label: '热点' },
  { key: 'most_viewed', label: '浏览最多' }
]

const activeTab = ref('latest')
const posts = ref([])
const loading = ref(true)

onMounted(async () => {
  // TODO: 从 API 获取数据
  loading.value = false
  posts.value = []
})
</script>
