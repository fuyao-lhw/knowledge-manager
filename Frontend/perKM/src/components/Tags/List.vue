<!-- 结构,主体 -->
<template>
  <div class="tag-list">
    <el-table :data="tagsData">
      <el-table-column label="标签id" prop="tag_id">
        <template #default="scope">
          <span class="tag-id">{{ scope.row.tag_id }}</span>
        </template>
      </el-table-column>
      <el-table-column label="标签名" prop="tag_name">
        <template #default="scope">
          <RouterLink class="tag-link" :to="'/tags/' + scope.row.tag_id">
            {{ scope.row.tag_name }}
          </RouterLink>
          <!-- <el-link class="tag-link" >
                {{ scope.row.tag_name }}
            </el-link> -->
        </template>
      </el-table-column>
    </el-table>
  </div>
  <!-- <RouterView></RouterView> -->
</template>

<!-- 交互,脚本语言 -->
<script lang="ts" setup name="TagList">
import { get_tags } from "@/hooks/get_tags";
import { onMounted, ref } from "vue";

const tagsData = ref([]);

onMounted(() => {
  get_tags(tagsData);
});
</script>

<!-- 样式 -->
<style scoped>

.tag-link{
  color: black;
  text-decoration: none;
  font-size: 20px;
}
</style>