<!-- 结构,主体 -->
<template>
  <div class="personal">
    <el-card title="个人信息" class="personal-info">
      <template #header>个人信息</template>
      <p>
        <span>用户名:</span>
        <span>{{ username }}</span>
      </p>
      <p>
        <el-button round>修改密码</el-button>
      </p>
      <!-- <p class="avatar">
      <span>头像:</span>
      <el-image
        src="https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png"
        fit="contain"
      />
    </p> -->
    </el-card>
    <el-card title="上传文件">
      <template #header>上传文件</template>
      <p class="one">
        <el-upload
        accept="md,txt,html"
        action="/api/documents"
        method="POST"
        :auto-upload="false"
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
  </div>
</template>

<!-- 交互,脚本语言 -->
<script lang="ts" setup name="PersonalCenterPage">
import { ref } from "vue";
import { Plus } from "@element-plus/icons-vue";

const username = localStorage.getItem("user");
</script>

<!-- 样式 -->
<style scoped>
.personal {
  display: flex;
  flex-direction: column; /* 垂直排列 */
  gap: 30px; /* 设置元素之间的间隙 */
  border: 1px solid #000;
  padding: 10px;
}

.avatar {
  padding: 30px 0;
  text-align: center;
  border-right: solid 1px var(--el-border-color);
  display: inline-block;
  width: 20%;
  box-sizing: border-box;
  vertical-align: top;
}
.avatar:last-child {
  border-right: none;
}
</style>