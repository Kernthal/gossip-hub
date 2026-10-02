<template>
  <div id="app">
    <nav class="bg-white shadow-sm border-b">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between h-16">
          <div class="flex items-center">
            <router-link to="/" class="text-xl font-bold text-gray-900">
              Gossip Hub
            </router-link>
          </div>
          <div class="flex items-center space-x-4">
            <router-link to="/" class="text-gray-600 hover:text-gray-900">首页</router-link>
            <router-link to="/timeline" class="text-gray-600 hover:text-gray-900">时间线</router-link>
            <router-link to="/ranking" class="text-gray-600 hover:text-gray-900">排行</router-link>
            <router-link to="/graph" class="text-gray-600 hover:text-gray-900">关系图谱</router-link>
            <router-link to="/profile" class="text-gray-600 hover:text-gray-900">我的</router-link>
          </div>
        </div>
      </div>
    </nav>
    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <router-view />
    </main>
  </div>
</template>

<script setup>
</script>
