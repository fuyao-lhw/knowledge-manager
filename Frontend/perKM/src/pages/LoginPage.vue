<!-- 结构,主体 -->
<template>
  <!-- <el-card> -->
    <form class="isLogin">
      <h1>登录</h1>
      <div class="ipt">
        <p>
          <span class="email">邮箱:</span>
          <el-input
            type="text"
            name="email"
            id="email"
            placeholder="请输入邮箱"
            v-model="data.email"
          />
        </p>
        <p>
          <span class="pwd">密码:</span>
          <el-input
            type="password"
            name="pwd"
            id="pwd"
            placeholder="请输入密码"
            v-model="data.password"
          />
        </p>
        <el-button @click="post_login">登录</el-button>
        <el-link class="to_register" href="/register">没有账号?去注册</el-link>
      </div>
    </form>
  <!-- </el-card> -->
</template>

<!-- 交互,脚本语言 -->
<script lang="ts" name="LoginPage" setup>
import identity from "@/hooks/identity.ts";
import { reactive } from "vue";
import router from "@/router/index.ts";

const { postLogin } = identity("login");

const data = reactive({
  email: "",
  password: "",
});

const post_login = async function () {
  console.log(data);
  const response = await postLogin(data);
  console.log(response);
  if (response.status === true) {
    localStorage.setItem("user", data.email);
    router.push("/");
  } else if (response.status === false) {
    alert(response.message);
  }
};
</script>

<!-- 样式 -->
<style scoped>
.isLogin {
  border: 2px solid;
  height: 500px;
  width: 500px;
  /* color: white; */
  background: #fff;
  position: relative;
  left: 25%;
}
.isLogin h1 {
  font-size: 50px;
  text-align: center;
  /* color: white; */
}
.ipt {
  margin-top: 40px;
  display: flex;
  flex-direction: column;
  gap: 30px; /* 输入项间距 */
  align-items: center; /* 水平居中 */
}

.ipt p {
  width: 80%; /* 控制输入行宽度 */
  display: flex;
  align-items: center;
  gap: 50px; /* 标签和输入框间距 */
}

.ipt span {
  font-size: 18px;
  width: 70px; /* 固定标签宽度 */
  text-align: right; /* 文字右对齐 */
}

input {
  background: transparent;
  border: none;
  border-bottom: 2px solid #666; /* 底部边框 */
  padding: 8px 10px;
  flex: 1; /* 输入框自适应剩余空间 */
  font-size: 16px;
  transition: border-color 0.3s;
}

input:focus {
  border-bottom-color: #409eff; /* 聚焦时颜色变化 */
  outline: none;
}

button {
  font-family: 华文楷体;
  font-size: 20px;
  width: 150px;
  height: 50px;
  border-radius: 10px; /* 圆角设置 */
  background: transparent;
  background-color: gray;
  color: rgb(20, 19, 19); /* 文字颜色 */
  border: none; /* 去掉边框 */
  cursor: pointer; /* 鼠标悬停效果 */
  transition: background-color 0.3s; /* 背景颜色过渡效果 */
}
.to_register {
  display: flex;
  left: -180px;
  top: 20px;
  font-size: 15px;
}
</style>