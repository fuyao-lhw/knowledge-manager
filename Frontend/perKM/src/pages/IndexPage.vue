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
              <RouterLink to="/documents/info" class="link"
                >系统概览</RouterLink
              >
            </template>
          </el-menu-item>
          <el-sub-menu index="documents">
            <template #title>
              <el-icon><Document /></el-icon>
              <span class="link">文档模块</span>
            </template>
            <el-menu-item index="/documents/list">
              <template #title>
                <el-icon><List /></el-icon>
                <RouterLink to="/documents/list" class="link"
                  >所有文档</RouterLink
                >
              </template>
            </el-menu-item>
            <el-menu-item index="/documents/upload">
              <template #title>
                <el-icon><DocumentAdd /></el-icon>
                <RouterLink to="/documents/upload" class="link"
                  >上传文档</RouterLink
                >
              </template>
            </el-menu-item>
            <el-menu-item index="/documents/setting">
              <template #title>
                <el-icon><Setting /></el-icon>
                <RouterLink to="/documents/setting" class="link"
                  >文档管理</RouterLink
                >
              </template>
            </el-menu-item>
          </el-sub-menu>
          <el-sub-menu index="/tags">
            <template #title>
              <el-icon><Collection /></el-icon>
              <span class="link">标签模块</span>
            </template>
            <el-menu-item index="/tags/list">
              <template #title>
                <el-icon><CollectionTag /></el-icon>
                <RouterLink to="/tags/list" class="link">所有标签</RouterLink>
              </template>
            </el-menu-item>
            <el-menu-item index="/tags/setting">
              <template #title>
                <el-icon><Setting /></el-icon>
                <RouterLink to="/tags/setting" class="link">标签管理</RouterLink>
              </template>
            </el-menu-item>
          </el-sub-menu>
          <el-sub-menu index="/knowledge">
            <template #title>
              <el-icon><Notification /></el-icon>
              <span class="link">知识关联</span>
            </template>
            <el-menu-item index="/knowledge/graph">
              <template #title>
                <el-icon><Notebook /></el-icon>
                <RouterLink :to="'/knowledge/graph'" class="link">知识图谱</RouterLink>
              </template>
            </el-menu-item>
          </el-sub-menu>
        </el-menu>
      </el-aside>

      <!-- 主内容区 -->
      <el-main class="main-content">
        <RouterView></RouterView>
        <!-- <el-button @click="get_document_list">请求文档</el-button> -->
      </el-main>
    </el-container>
  </div>
</template>

<script lang="ts" setup>
// import "@/components/User/UserSetting.vue";
import "@/components/Documents/Info.vue";
import { onMounted, ref } from "vue";
import { RouterLink, RouterView } from "vue-router";

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

.navigator .link {
  color: #fff;
  text-decoration: none;
  font-size: 20px;
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