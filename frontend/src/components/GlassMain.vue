<template>
  <main class="glass-main">
    <div class="main-container">
      <slot></slot>
    </div>
  </main>
</template>

<script setup>
</script>

<style scoped>
.glass-main {
  margin-left: 240px;
  padding: 96px 24px 40px;
  min-height: 100vh;
}

.main-container {
  max-width: 1200px;
  margin: 0 auto;
}

@media (max-width: 768px) {
  .glass-main {
    margin-left: 0;
    padding: 80px 16px 32px;
  }
}
</style>
