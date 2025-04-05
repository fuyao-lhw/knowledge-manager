<!-- 结构,主体 -->
<template>
  <el-card>
    <el-table :data="document_list">
        <el-table-column fixed prop="name" label="文章标题" width="300">
            <template #default="{row}">
                <el-link class="link" :underline="false" :href="'/document/'+row.document_id">{{ row.name }}</el-link>
            </template>
        </el-table-column>
        <el-table-column prop="upload_time" label="发布时间" width="180" />
        <el-table-column prop="document_id" label="文章id" width="180" />
    </el-table>
    <!-- <p v-for="(document, index) in document_list" :key="index">
      <el-link class="link" :underline="false" :href="'/document/'+document.document_id">{{ document.name.split('.')[0] }}</el-link>
    </p> -->
    <RouterView></RouterView>
  </el-card>
</template>

<!-- 交互,脚本语言 -->
<script setup lang="ts" name="List">
import axios from "axios";
import { onMounted, ref } from "vue";

// 文档列表
let document_list = ref(<any>[]);
// 获取文档列表
async function get_document_list() {
  const response = await axios.get("/api/documents?form=all");
  console.log("文档列表:", response.data);
  if (response.data.status == 200) {
    document_list.value = response.data.data;
  } else {
    console.log("获取文档列表失败");
  }
}

onMounted(() => {
  get_document_list();
});
</script>

<!-- 样式 -->
<style scoped>
.crumb {
  font-size: 18px;
}
.header {
    font-size: 20px;
}

.link {
  color: black;
  text-decoration: none;
  font-size: 20px;
}
</style>