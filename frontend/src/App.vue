<template>
  <div id="app">
    <ParticleBackground />
    <GlassHeader />
    <GlassSidebar />
    <GlassMain>
      <router-view v-slot="{ Component }">
        <transition name="page" mode="out-in">
          <component :is="Component" />
        </transition>
      </router-view>
    </GlassMain>
    <GlassFooter />
  </div>
</template>

<script setup>
import ParticleBackground from './components/ParticleBackground.vue'
import GlassHeader from './components/GlassHeader.vue'
import GlassSidebar from './components/GlassSidebar.vue'
import GlassMain from './components/GlassMain.vue'
import GlassFooter from './components/GlassFooter.vue'
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  min-height: 100vh;
}

#app {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

/* Page transitions */
.page-enter-active,
.page-leave-active {
  transition: all 0.3s ease;
}

.page-enter-from {
  opacity: 0;
  transform: translateY(20px);
}

.page-leave-to {
  opacity: 0;
  transform: translateY(-20px);
}
</style>
