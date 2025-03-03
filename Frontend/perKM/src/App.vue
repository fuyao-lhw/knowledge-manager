<!-- 结构,主体 -->
<template>
  <div class="main-container">
    <!-- 星空背景层 -->
    <div class="star-background">
      <div class="star-layer"></div>
    </div>

    <!-- 内容层 -->
    <div class="content">
      <RouterView></RouterView>
    </div>
  </div>
</template>

<script setup lang="ts" name="WelcomePage">
</script>

<style scoped>
.main-container {
  position: relative;
  height: 100vh;
  width: 100%;
  min-height: 100vh;
  overflow: hidden;
  background: linear-gradient(to bottom right, #000428 0%, #004e92 100%);
}


/* 内容样式 */
.content {
  position: relative;
  z-index: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100%;
  color: white;
  text-align: center;
  padding: 20px;
}
</style>