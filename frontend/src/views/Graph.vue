<template>
  <div class="space-y-6">
    <h1 class="text-2xl font-bold text-gray-900">关系图谱</h1>

    <div class="bg-white rounded-lg shadow p-4">
      <div class="flex space-x-4 mb-4">
        <button
          v-for="tab in tabs"
          :key="tab.key"
          @click="activeTab = tab.key"
          :class="[
            'px-4 py-2 rounded-lg text-sm font-medium',
            activeTab === tab.key
              ? 'bg-blue-600 text-white'
              : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
          ]"
        >
          {{ tab.label }}
        </button>
      </div>

      <div ref="graphContainer" class="w-full h-96 border rounded-lg"></div>
    </div>

    <div class="bg-white rounded-lg shadow p-6">
      <h3 class="text-lg font-semibold text-gray-900 mb-4">关系详情</h3>
      <p class="text-gray-500 text-sm">点击节点查看详细信息</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import * as d3 from 'd3'

const tabs = [
  { key: 'all', label: '全部关系' },
  { key: 'cp', label: 'CP关系' },
  { key: 'friend', label: '朋友关系' },
  { key: 'custom', label: '自定义' }
]

const activeTab = ref('all')
const graphContainer = ref(null)

onMounted(() => {
  // TODO: 初始化 D3.js 关系图谱
})
</script>
