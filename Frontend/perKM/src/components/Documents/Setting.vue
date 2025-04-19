<!-- 结构,主体 -->
<template>
  <el-table :data="documentList" @selection-change="handleSelectionChange">
    <el-table-column type="selection" />
    <el-table-column fixed prop="title" label="文章标题" width="300">
      <template #default="scope">
        <el-input class="link" v-model="scope.row.title" />
      </template>
    </el-table-column>
    <el-table-column prop="file_tag" label="标签" width="180">
      <template #default="scope">
        <el-input class="link" v-model="scope.row.file_tag" />
      </template>
    </el-table-column>
    <el-table-column prop="upload_time" label="发布时间" width="180" />
    <el-table-column prop="id" label="文章id" width="180" />
  </el-table>
  <div class="btn">
    <el-button @click="save" class="save">
      <el-icon><Finished /></el-icon>
      <span>保存修改</span>
    </el-button>
    <el-popconfirm
      confirm-button-text="确定"
      cancel-button-text="取消"
      title="确定删除选定的标签吗？"
      type="warning"
      icon="el-icon-warning"
      class="delete"
      @confirm="delete_documents"
    >
      <template #reference>
        <el-button>
          <el-icon><Delete /></el-icon>
          <span>删除选定的文档</span>
        </el-button>
      </template>
    </el-popconfirm>
    <el-button class="add" @click="add_document">
      <el-icon><CirclePlusFilled /></el-icon>
      <span>新增/更新文档</span>
    </el-button>
    <div class="tips">
      <el-text type="warning">
        1.更新文档的信息或者删除文档之前,需要选择多选框,然后再点击对应的按钮<br>
        2.更新文档内容需要重新选择内容,文档名字需要和之前的保持一致,否则会将其作为新文档
      </el-text>
    </div>
  </div>
</template>

<!-- 交互,脚本语言 -->
<script lang="ts" name="DocumentSetting" setup>
import { ref, onMounted, onBeforeUnmount } from "vue";
import { get_document_list } from "@/hooks/get_documents";
import { useRouter } from "vue-router";
import axios from "axios";
import {Upload} from "@element-plus/icons-vue";

// 多选框选中数据
const selectedRows = ref([]);

// 处理多选框选中的数据
const handleSelectionChange = (val: any) => {
  selectedRows.value = val;
  console.log("多选框选中的数据", selectedRows.value);
};

// 保存修改
const save = async () => {
  const response = await axios
    .put("/api/documents", {
      documentList: selectedRows.value,
    })
    .then((response) => {
      console.log("更新的返回数据", response.data);
    });

  // 刷新页面
  get_document_list(documentList);
};

// 删除文档
const delete_documents = async () => {
  const response = await axios
    .delete("/api/documents", {
      data: {
        documentList: selectedRows.value,
      },
    })
    .then((response) => {
      console.log("删除的返回数据", response.data);
    });
};

// router
const router = useRouter();

// 新增文档-跳转到上传文档
const add_document = () => {
  router.push("/documents/upload");
};



// 文档列表
const documentList = ref<any>([]);

onMounted(() => {
  get_document_list(documentList);
});
</script>

<!-- 样式 -->
<style scoped>
</style>