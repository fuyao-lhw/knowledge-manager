<template>
  <div class="index-page">
    <el-container class="main-container">
      <!-- 侧边导航 -->
      <el-aside class="navigator">
        <el-menu
          active-text-color="#409EFF"
          background-color="#1a1a1a"
          text-color="#fff"
        >
          <el-menu-item index="/dashboard">
            <template #title>
              <el-icon><House /></el-icon>
              <span>知识概览</span>
            </template>
          </el-menu-item>
          <el-sub-menu index="2">
            <template #title>
              <el-icon><Files /></el-icon>
              <span>知识库管理</span>
            </template>
            <el-menu-item index="/knowledge/list">所有知识库</el-menu-item>
            <!-- <el-menu-item index="/knowledge/new">新建知识库</el-menu-item> -->
          </el-sub-menu>
          <el-menu-item index="/recent">
            <template #title>
              <el-icon><Clock /></el-icon>
              <span>所有文档</span>
            </template>
          </el-menu-item>
        </el-menu>
      </el-aside>

      <!-- 主内容区 -->
      <el-main class="main-content">
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
              {{ update.title }}
            </el-timeline-item>
          </el-timeline>
        </el-card>

        <!-- <el-button @click="get_document_list">请求文档</el-button> -->
      </el-main>
    </el-container>
  </div>
</template>

<script lang="ts" setup>
import { onMounted, ref } from "vue";
import { House, Files, Clock } from "@element-plus/icons-vue";
import "@/components/User/UserInfo.vue";
import axios from "axios";

const navVisible = ref(false);

const toggleNav = () => {
  navVisible.value = !navVisible.value;
  document.querySelector(".navigator").classList.toggle("active");
};
const searchKey = ref("");




// Python,HTML,CSS,JacaScript,Java,Vue,C#,开发
const statsData = ref([]);

async function get_stats() {
  const response = await axios.get("/api/stats");
  console.log("数据展示", response.data)
  statsData.value = response.data.data;
}

const updates = ref([]);

async function get_document_list() {
  const response = await axios.get("/api/documents?form=latest");
  console.log("最近更新" ,response.data);
  for (let i=0; i<response.data.data.length; i++){
    updates.value.push({
      title: response.data.data[i].name.split(".")[0],
      time: response.data.data[i].upload_time,
    });
  }
}

onMounted(()=>{
  get_stats();
  get_document_list();
})

</script>

<style scoped>
/* 基础布局优化 */
.index-page {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.header-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  padding: 0 2%;
}

/* 新增搜索容器 */
.search-container {
  flex: 1;
  max-width: 600px;
  margin: 0 20px;
  position: relative;
  top: -20px;
}

/* 调整搜索框样式 */
.search-input {
  width: 100%;
  transition: all 0.3s;
}

/* 用户信息容器 */
.header-right {
  display: flex;
  align-items: center;
  margin-left: auto; /* 确保靠右对齐 */
  position: relative;
  top: -20px;
}

/* 响应式调整 */
@media (max-width: 992px) {
  .system-name {
    font-size: 24px;
  }

  .search-container {
    max-width: 400px;
    margin: 0 10px;
  }
}

@media (max-width: 768px) {
  .system-name {
    font-size: 20px;
  }

  .search-container {
    max-width: 200px;
  }

  .search-input ::v-deep .el-input__inner {
    padding-left: 30px;
  }
}

@media (max-width: 480px) {
  .system-name {
    display: none;
  }

  .search-container {
    max-width: 180px;
    margin-left: 10px;
  }
}

.system-name {
  font-size: 30px;
  line-height: 60px; /* 新增行高设置 */
  display: inline-flex; /* 确保垂直对齐生效 */
  align-items: center; /* 二次保障对齐 */
  height: 100%; /* 继承父级高度 */
  position: relative;
  top: -20px;
}

/* 侧边导航 */
.main-container {
  flex: 1;
  min-height: 0; /* 修复flex布局滚动问题 */
}

.navigator {
  width: 200px;
  background: #1a1a1a;
  overflow-y: auto;
}

/* 主内容区 */
.main-container {
  flex: 1;
  min-height: 0; /* 修复flex布局滚动问题 */
}
.main-content {
  padding: 20px 2%;
  background: #f0f2f5;
  overflow-y: auto;
  /* 移除原来的 height: calc(100vh - 60px) */
}

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

/* 快捷操作按钮 */
.quick-actions .el-space {
  flex-wrap: wrap;
  gap: 12px !important;
}

/* 时间线优化 */
.recent-updates .el-timeline {
  max-width: 800px;
  margin: 0 auto;
}

/* 页脚样式 */
.system-footer {
  flex-shrink: 0;
  background: #1a1a1a;
  color: #fff;
  padding: 20px;
  text-align: center;
  height: 100px;
  box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.1);
}

.footer-content {
  max-width: 1200px;
  margin: 0 auto;
}

.footer-section {
  padding: 10px;
  text-align: left;
  position: relative;
  top: -50px;
}

.footer-section h4 {
  color: #409eff;
  margin-bottom: 12px;
}

.footer-section p {
  margin: 6px 0;
  font-size: 14px;
}

.el-link {
  display: block;
  margin: 6px 0;
}
</style>