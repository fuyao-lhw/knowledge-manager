<!-- 结构,主体 -->
<template>
  <div class="content">
    <h1 class="title">欢迎来到扶摇知识管理系统</h1>
    <p class="subtitle">
      {{
        welcomeWord != null
          ? welcomeWord
          : "让每一条信息都找到归处，让每一次思考都有迹可循"
      }}
    </p>
    <button class="explore-btn" @click="startJourney">开始探索</button>
  </div>
</template>

<!-- 交互,脚本语言 -->
<script lang="ts" setup name="WelcomePage">
import router from "@/router";
import { useWelcomeWordsStore } from "@/store/WelcomeWords.ts";
import { ref, onMounted, onBeforeUnmount } from "vue";
const startJourney = () => {
  // 这里添加导航逻辑
  console.log("开始旅程");
  // 实际项目中使用路由跳转：
  // router.push('/home')
  router.push("/index");
};

const welcomeWord = ref("");
const intervalId = ref();

onMounted(() => {
  intervalId.value = setInterval(() => {
    const list = useWelcomeWordsStore().welcomeWords;
    if (list.length > 0) {
      const randomIndex = Math.floor(Math.random() * list.length);
      welcomeWord.value = list[randomIndex];
    }
  }, 3000);
});

onBeforeUnmount(() => {
  clearInterval(intervalId.value);
});
</script>

<!-- 样式 -->
<style scoped>
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

.title {
  font-size: 3.5rem;
  margin-bottom: 1rem;
  text-shadow: 0 0 15px rgba(255, 255, 255, 0.5);
  animation: title-float 3s ease-in-out infinite;
}

.subtitle {
  font-size: 1.5rem;
  margin-bottom: 3rem;
  opacity: 0.9;
  letter-spacing: 2px;
}

.explore-btn {
  padding: 1rem 3rem;
  font-size: 1.2rem;
  background: transparent;
  border: 2px solid white;
  color: white;
  border-radius: 30px;
  cursor: pointer;
  transition: all 0.3s ease;
  backdrop-filter: blur(5px);
}

.explore-btn:hover {
  background: rgba(255, 255, 255, 0.1);
  transform: scale(1.05);
  box-shadow: 0 0 20px rgba(255, 255, 255, 0.3);
}

/* 标题浮动动画 */
@keyframes title-float {
  0%,
  100% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-10px);
  }
}

/* 响应式设计 */
@media (max-width: 768px) {
  .title {
    font-size: 2.5rem;
  }

  .subtitle {
    font-size: 1.2rem;
  }
}
</style>