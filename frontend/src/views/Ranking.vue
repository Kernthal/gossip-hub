<template>
  <div class="space-y-6">
    <h1 class="text-2xl font-bold text-gray-900">热度排行</h1>

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
      <div v-else-if="rankings.length === 0" class="text-center py-8">
        <p class="text-gray-500">暂无排行数据</p>
      </div>
      <div
        v-for="(item, index) in rankings"
        :key="item.id"
        class="bg-white rounded-lg shadow p-4 flex items-center space-x-4"
      >
        <div :class="['text-2xl font-bold w-8 text-center', index < 3 ? 'text-yellow-500' : 'text-gray-400']">
          {{ index + 1 }}
        </div>
        <div class="flex-1">
          <p class="text-gray-800">{{ item.title }}</p>
          <p class="text-sm text-gray-500">{{ item.views }} 浏览</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const tabs = [
  { key: 'most_viewed', label: '浏览最多' },
  { key: 'hot', label: '热点' },
  { key: 'latest', label: '最新' }
]

const activeTab = ref('most_viewed')
const rankings = ref([])
const loading = ref(true)

onMounted(async () => {
  // TODO: 从 API 获取排行数据
  loading.value = false
  rankings.value = []
})
</script>
