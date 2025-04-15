<!-- 结构,主体 -->
<template>
  <div class="stats-container">
    <el-row :gutter="20">
      <el-col :span="6" v-for="(stat, index) in statsData" :key="index">
        <el-card shadow="hover">
          <el-statistic
            :title="stat.title"
            :value="stat.value"
            :precision="stat.precision || 0"
          />
        </el-card>
      </el-col>
    </el-row>
  </div>

  <!-- 最近更新 -->
  <el-card class="recent-updates">
    <template #header>
      <div class="card-header">
        <span>最近更新</span>
      </div>
    </template>
    <el-timeline>
      <el-timeline-item
        v-for="(update, index) in updates"
        :key="index"
        :timestamp="update.time"
      >
        <el-link :underline="false" :href="'/document/' + update.document_id">{{
          update.title
        }}</el-link>
      </el-timeline-item>
    </el-timeline>
  </el-card>
</template>

<!-- 交互,脚本语言 -->
<script setup lang="ts" name="Info">
import axios from "axios";
import { onMounted, ref } from "vue";

// const navVisible = ref(false);

// const toggleNav = () => {
//   navVisible.value = !navVisible.value;
//   document.querySelector(".navigator").classList.toggle("active");
// };
// 搜索的关键字
const searchKey = ref("");

// Python,HTML,CSS,JacaScript,Java,Vue,C#,开发
// 新增类型定义
interface StatItem {
  title: string;
  value: number | string;
  precision?: number;
}

const statsData = ref<StatItem[]>([]); // 指定泛型类型

// async function get_stats() {
//   const response = await axios.get("/api/stats");
//   // 数据转换确保类型正确
//   statsData.value = response.data.data.map(item => ({
//     title: item.title,
//     value: item.value,
//     precision: item.precision
//   }));
// }

// 获取统计数据
async function get_stats() {
  const response = await axios.get("/api/stats");
  console.log("数据展示", response.data);
  statsData.value = response.data.data;
}

// 在<script setup>中新增接口定义
interface UpdateItem {
  title: string;
  time: string;
  document_id: number | string; // 根据实际类型调整
}

// 修改updates定义
const updates = ref<UpdateItem[]>([]); // 显式指定泛型类型

// 获取最近更新
async function get_document_list() {
  const response = await axios.get("/api/documents?form=latest");
  console.log("最近更新", response.data);
  for (let i = 0; i < response.data.data.length; i++) {
    updates.value.push({
      title: response.data.data[i].name.split(".")[0],
      time: response.data.data[i].upload_time,
      document_id: response.data.data[i].document_id,
    });
  }
}

onMounted(() => {
  get_stats();
  get_document_list();
});
</script>

<!-- 样式 -->
<style scoped>
/* 统计卡片容器 */
.stats-container .el-row {
  justify-content: space-around;
}

.stats-container .el-col {
  flex: 1;
  min-width: 240px;
  max-width: 280px;
  margin: 10px;
}
</style>