<!-- 结构,主体 -->
<template>
    <div class="document-detail">
      <el-card>
        <el-container>
          <el-header>
            <h1 class="headers">{{ document.title }}</h1>
          </el-header>
          <el-main>
            <div
              v-html="document.content"
              class="markdown-body"
              style="font-size: small"
            ></div>
          </el-main>
        </el-container>
      </el-card>
    </div>
  </template>
  
  <!-- 交互,脚本语言 -->
  <script name="Detail" setup lang="ts">
  import { onMounted, ref } from "vue";
  import axios from "axios";
  import { useRoute } from "vue-router";
  import MarkDownIt from "markdown-it";
  
  const document = ref({
    title: "",
    content: "",
  });
  
  const route = useRoute();
  
  async function get_document_detail() {
    const response = await axios.get("/api/document/" + route.params.document_id);
    console.log("文档详细展示", response.data);
    const md = new MarkDownIt();
    if (response.data.status == 200) {
      document.value.content = md.render(response.data.data.content);
      document.value.title = response.data.data.title.split(".")[0];
    }
  }
  
  onMounted(() => {
    get_document_detail();
  });
  </script>
  
  <!-- 样式 -->
  <style scoped>
  header{
      text-align: center;
  }
  .markdown-body {
    box-sizing: border-box;
    min-width: 200px;
    max-width: 980px;
    margin: 0 auto;
    padding: 45px;
  }
  
  @media (max-width: 767px) {
    .markdown-body {
      padding: 15px;
    }
  }
  </style>
  