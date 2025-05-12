<template>
  <div class="index-page">
    <!-- canvas层 -->
    <canvas ref="canvasRef" class="background-canvas"></canvas>

    <!-- 顶部导航栏 -->
    <el-header class="header">
      <el-icon class="menu-toggle" @click="toggleNav">
        <Expand v-if="navVisible" />
        <Fold v-else />
      </el-icon>
      <div class="header-content">
        <!-- 左侧系统名称 -->
        <el-link :underline="false" style="color: white;" class="logo" type="primary" href="/index">
          <span class="system-name">
            <el-icon class="system-icon"><Promotion /></el-icon
            >扶摇知识管理系统</span
          >
        </el-link>

        <!-- 中间搜索框 -->
        <div class="search-container">
          <el-input
            v-model="searchKey"
            placeholder="全站搜索"
            class="search-input"
            clearable
          >
            <template #prefix>
              <el-icon><Search /></el-icon>
            </template>
            <template #suffix>
              <el-button type="primary" @click="submitSearch">搜索</el-button>
            </template>
          </el-input>
        </div>
        <!-- 右侧用户信息 -->
        <div class="header-right">
          <user-setting />
        </div>
      </div>
    </el-header>
    <el-main class="main"><RouterView></RouterView></el-main>
    <el-divider></el-divider>
    <el-footer class="system-footer">
      <div class="footer-content">
        <el-row :gutter="20">
          <el-col :md="8" :sm="24">
            <div class="footer-section">
              <h4>关于我们</h4>
              <p>
                扶摇团队<br />
                提倡知识共享<br />
                © 2025 扶摇知识管理系统
              </p>
            </div>
          </el-col>
          <el-col :md="8" :sm="24">
            <div class="footer-section">
              <h4>联系方式</h4>
              <p>
                邮箱：1959415641@qq.com<br />
                电话：***********<br />
                <el-link href="https://gitee.com/luo_hw" :underline="false"
                  >Gitee</el-link
                >
              </p>
            </div>
          </el-col>
          <el-col :md="8" :sm="24">
            <div class="footer-section">
              <h4>快速链接</h4>
              <p>
                <el-link type="info" :underline="false">用户协议</el-link><br />
                <el-link type="info" :underline="false">隐私政策</el-link><br />
                <el-link type="info" :underline="false">帮助中心</el-link>
              </p>
            </div>
          </el-col>
        </el-row>
      </div>
    </el-footer>
  </div>
</template>

<script lang="ts" setup>
import { Search } from "@element-plus/icons-vue";
import { ref, onMounted, onBeforeUnmount } from "vue";
import UserSetting from "./components/User/UserSetting.vue";
import axios from "axios";
import { useRouter } from "vue-router";

const searchKey = ref("");

const router = useRouter();

// 搜索方法
const submitSearch = async () => {
  console.log("搜索内容：", searchKey.value);

  router.push({
    path: "/search/result",
    query: {
      keyword: searchKey.value,
    },
  });
};

const canvasRef = ref<HTMLCanvasElement>();

// 新增导航状态管理
const navVisible = ref(true);

// 新增导航切换方法
const toggleNav = () => {
  navVisible.value = !navVisible.value;
};



// Canvas初始化
const initCanvas = () => {
  const canvas = canvasRef.value!;
  const ctx = canvas.getContext("2d")!;
  // 在initCanvas中添加
  // canvas.style.willChange = 'contents' // 启用GPU加速

  // 设置画布尺寸
  const resize = () => {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    draw();
  };

  // 绘制示例（星空效果）
  const draw = () => {
    // ctx.fillStyle = 'rgba(0, 0, 0, 0.1)' // 添加透明度实现拖尾效果
    // ctx.fillRect(0, 0, canvas.width, canvas.height)
    ctx.fillStyle = "#000";
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    // 添加星星示例
    for (let i = 0; i < 200; i++) {
      ctx.beginPath();
      ctx.arc(
        Math.random() * canvas.width,
        Math.random() * canvas.height,
        Math.random() * 2,
        0,
        Math.PI * 2
      );
      ctx.fillStyle = "#fff";
      ctx.fill();
    }
  };

  resize();
  draw();
  window.addEventListener("resize", resize);

  // 修改后的生命周期管理
  let resizeHandler: () => void;

  onMounted(() => {
    resizeHandler = () => resize();
    window.addEventListener("resize", resizeHandler);
  });

  onBeforeUnmount(() => {
    window.removeEventListener("resize", resizeHandler);
  });
};


onMounted(initCanvas);
</script>

<style scoped>
/* 添加全局样式 */

.background-canvas {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  z-index: 0; /* 确保内容在上层 */
}
/* 基础布局优化 */
.index-page {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  z-index: 1; /* 提升内容层级 */
}

.main {
  z-index: 1;
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

.system-icon {
  font-size: inherit;
}

/* 页脚 */
.system-footer {
  display: block;
  color: #fff;
  height: 100px;
}

/* .el-link{
  display: block;
} */
</style>