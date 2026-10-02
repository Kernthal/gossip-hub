<template>
  <div class="glass-layout">
    <GlassHeader />
    <div class="layout-body">
      <GlassSidebar />
      <GlassMain>
        <slot></slot>
      </GlassMain>
    </div>
    <GlassFooter />
  </div>
</template>

<script setup>
import GlassHeader from './GlassHeader.vue'
import GlassSidebar from './GlassSidebar.vue'
import GlassMain from './GlassMain.vue'
import GlassFooter from './GlassFooter.vue'
</script>

<style scoped>
.glass-layout {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.layout-body {
  display: flex;
  flex: 1;
}
</style>
