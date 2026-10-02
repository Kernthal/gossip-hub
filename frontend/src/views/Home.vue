<template>
  <div class="space-y-6">
    <div class="bg-white rounded-lg shadow p-6">
      <h1 class="text-2xl font-bold text-gray-900 mb-4">欢迎来到 Gossip Hub</h1>
      <p class="text-gray-600 mb-6">这是一个专属于你们的八卦社交平台。匿名分享、CP配对、关系图谱、八卦预测，应有尽有。</p>
      <div class="flex space-x-4">
        <router-link to="/timeline" class="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700">
          浏览时间线
        </router-link>
        <router-link to="/post" class="bg-green-600 text-white px-4 py-2 rounded-lg hover:bg-green-700">
          发布八卦
        </router-link>
      </div>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
      <div class="bg-white rounded-lg shadow p-6">
        <h3 class="text-lg font-semibold text-gray-900 mb-2">八卦爆料</h3>
        <p class="text-gray-600 text-sm">匿名分享你知道的小道消息，看看谁和谁在一起了。</p>
      </div>
      <div class="bg-white rounded-lg shadow p-6">
        <h3 class="text-lg font-semibold text-gray-900 mb-2">CP配对</h3>
        <p class="text-gray-600 text-sm">你觉得谁和谁最配？发起投票，看看大家怎么说。</p>
      </div>
      <div class="bg-white rounded-lg shadow p-6">
        <h3 class="text-lg font-semibold text-gray-900 mb-2">关系图谱</h3>
        <p class="text-gray-600 text-sm">可视化展示谁和谁的关系，一目了然。</p>
      </div>
    </div>
  </div>
</template>

<script setup>
</script>
