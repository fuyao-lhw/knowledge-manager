<!-- 结构,主体 -->
<template>
    <div class="search-result">
        <el-table :data="searchResult">
            <el-table-column prop="id" label="文档ID"></el-table-column>
            <el-table-column prop="title" label="文档标题">
                <template #default="scope">
                    <RouterLink class="link" :to="'/document/' + scope.row.id">
                        {{ scope.row.title }}
                    </RouterLink>
                </template>
            </el-table-column>
            <el-table-column prop="file_tag" label="文档标签"></el-table-column>
        </el-table>
    </div>
</template>

<!-- 交互,脚本语言 -->
<script lang="ts" name="SearchResult" setup>
import { useRoute } from "vue-router";
import { onMounted, ref } from "vue";
import axios from "axios";

const route = useRoute();

// 搜索结果
const searchResult = ref([]);

// 获取搜索结果
const get_search_result = async () => {
    const searchKey = ref(route.query.keyword as string);
    const response = await axios.post("/api/search", {
    keyword: searchKey.value,
  });
  console.log("搜索结果：", response.data);
  searchResult.value = response.data.data;
};

onMounted(() => {
  get_search_result();
});
</script>

<!-- 样式 -->
<style scoped>
.link {
  color: black;
  text-decoration: none;
  font-size: 20px;
}
</style>