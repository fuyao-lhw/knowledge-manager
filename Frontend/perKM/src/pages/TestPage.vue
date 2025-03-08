<!-- 结构,主体 -->
<template>
  <canvas id="canva"></canvas>
</template>

<!-- 交互,脚本语言 -->
<script lang="ts" setup name="TestPage">
import { onMounted } from "vue";
const cvs = document.getElementById("canvas");
function init() {
  cvs.width = window.innerWidth;
  cvs.height = window.innerHeight;
}

onMounted(() => {
  init();
});
</script>

<!-- 样式 -->
<style scoped>
#canva {
  color: #fff;
}
</style>