<template>
  <div class="space-y-6">
    <div v-if="loading" class="text-center py-8">
      <p class="text-gray-500">加载中...</p>
    </div>
    <div v-else-if="post" class="space-y-6">
      <div class="bg-white rounded-lg shadow p-6">
        <div class="flex items-center justify-between mb-4">
          <div class="flex items-center space-x-2">
            <span class="text-sm text-gray-500">{{ post.author }}</span>
            <span class="text-xs text-gray-400">{{ post.created_at }}</span>
          </div>
          <span :class="['text-xs px-2 py-1 rounded-full', post.type_class]">
            {{ post.type }}
          </span>
        </div>
        <p class="text-gray-800 text-lg mb-4">{{ post.content }}</p>
        <div v-if="post.images && post.images.length > 0" class="flex space-x-2 mb-4">
          <img
            v-for="img in post.images"
            :key="img"
            :src="img"
            class="w-32 h-32 object-cover rounded-lg"
          />
        </div>
        <div class="flex items-center space-x-6 text-sm text-gray-500">
          <button @click="like" class="hover:text-red-500">
            点赞 {{ post.likes }}
          </button>
          <span>浏览 {{ post.views }}</span>
          <span>评论 {{ post.comments }}</span>
        </div>
      </div>

      <div class="bg-white rounded-lg shadow p-6">
        <h3 class="text-lg font-semibold text-gray-900 mb-4">评论</h3>
        <div class="space-y-4">
          <div v-if="comments.length === 0" class="text-center py-4">
            <p class="text-gray-500">暂无评论</p>
          </div>
          <div
            v-for="comment in comments"
            :key="comment.id"
            class="border-b pb-4"
          >
            <div class="flex items-center space-x-2 mb-2">
              <span class="text-sm text-gray-500">{{ comment.author }}</span>
              <span class="text-xs text-gray-400">{{ comment.created_at }}</span>
            </div>
            <p class="text-gray-800">{{ comment.content }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const post = ref(null)
const comments = ref([])
const loading = ref(true)

const like = () => {
  // TODO: 点赞逻辑
}

onMounted(async () => {
  // TODO: 从 API 获取帖子详情
  loading.value = false
})
</script>
