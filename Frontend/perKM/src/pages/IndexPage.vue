<!-- 结构,主体 -->
<template>
<div class="index-page">
    <div class="star-background">
        <div class="star-layer"></div>
        <div class="star-layer"></div>
    </div>

    <div class="content">
        首页
    </div>
</div>
</template>

<!-- 交互,脚本语言 -->
<script lang="ts" setup name="IndexPage">

</script>

<!-- 样式 -->
<style scoped>
.index-page {
    position: relative;
    min-height: 100vh;
}
.content {
    position: relative;
    z-index: 1;
}
</style>