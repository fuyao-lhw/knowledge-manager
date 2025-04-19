<!-- 结构,主体 -->
<template>
  <div class="show-document">
    <el-table :data="documents_by_tag">
      <el-table-column prop="id" label="文档ID"></el-table-column>
      <el-table-column prop="title" label="文档标题">
        <template #default="scope">
          <RouterLink :to="'/document/' + scope.row.id" class="document-link">
            {{ scope.row.title }}
          </RouterLink>
        </template>
      </el-table-column>
      <el-table-column
        prop="update_time"
        label="更新时间"
        width="180"
      ></el-table-column>
    </el-table>
  </div>
</template>

<!-- 交互,脚本语言 -->
<script setup lang="ts" name="TagDetail">
import { onMounted, ref } from "vue";
import { useRoute } from "vue-router";
import axios from "axios";

const route = useRoute();
// 获取路由参数
const tag_id = ref(route.params.tag_id);

// 获取该标签对应的文档列表-数据
const documents_by_tag = ref([]);

// 获取该标签对应的文档列表-方法
const get_documents_by_tag = async () => {
  const response = await axios.get(`/api/tags/${tag_id.value}`);
  console.log("文档列表:", response.data);
  documents_by_tag.value = response.data.data.documents_info;
};

onMounted(() => {
  get_documents_by_tag();
});
</script>

<!-- 样式 -->
<style scoped>
.document-link{
  color: black;
  text-decoration: none;
  font-size: 20px;
}
</style>