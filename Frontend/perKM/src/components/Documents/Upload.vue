<!-- 结构,主体 -->
<template>
    <el-card title="上传文件">
      <template #header>上传文件</template>
      <p class="one">
        <el-upload
          accept="md,txt,html"
          action="/api/documents"
          method="post"
          :auto-upload="true"
          :data="uploadData"
        >
          <template #tip>
            <div class="el-upload__tip">
              暂时只支持.md/.txt/.html文件;大小不超过5mb
            </div>
          </template>
          <el-button type="primary" :icon="Plus">上传知识文件</el-button>
        </el-upload>
      </p>
    </el-card>
</template>

<!-- 交互,脚本语言 -->
<script lang="ts" setup name="Upload">
import { Plus } from "@element-plus/icons-vue";
import { ref } from "vue";

const username = localStorage.getItem("user");

const uploadData = ref({
  username: localStorage.getItem('user') || '',
});

</script>

<!-- 样式 -->
<style scoped>

</style>