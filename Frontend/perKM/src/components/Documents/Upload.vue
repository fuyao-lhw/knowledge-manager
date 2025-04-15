<!-- 结构,主体 -->
<template>
  <el-card title="上传文件">
    <template #header>上传文件</template>
    <div class="btn-group">
      <el-upload
        accept="md,txt,html"
        action="/api/documents"
        method="post"
        :auto-upload="false"
        :data="uploadData"
        :multiple="true"
        ref="uploadFiles"
        @change="fileHandleChange"
        :show-file-list="false"
        :on-success="removeFiles"
      >
        <template #trigger
          ><el-button type="primary" :icon="Plus" class="btn"
            >选择文档</el-button
          ></template
        >
        <template #default>
          <el-button
            type="success"
            @click="submitFile"
            class="btn"
            :icon="Upload"
            >点击上传</el-button
          >
        </template>

        <template #tip>
          <div class="el-upload__tip">
            暂时只支持.md/.txt/.html文件;大小不超过5mb<br />
            如果点击上传之后,没有填写文件标签,则默认以文件后缀作为文件标签
          </div>
        </template>
      </el-upload>
    </div>
    <div class="data-show">
      <el-table :data="selectedFiles">
        <el-table-column label="文件名" prop="file.name" />
        <el-table-column label="文件大小" prop="file.size" />
        <el-table-column label="文件标签" prop="tags" />
        <el-table-column label="操作">
          <template #default="scope">
            <el-button @click="editTags(scope.$index)">编辑标签</el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>
  </el-card>
  <el-dialog v-model="tagFormDialogBollean">
    <template #title>编辑标签</template>
    <el-form :model="selectedFiles[editingIndex].tags">
      <el-form-item label="输入标签(以英文逗号分割多个标签)">
        <el-input v-model="selectedFiles[editingIndex].tags" />
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="saveTags">保存</el-button>
      </el-form-item>
    </el-form>
  </el-dialog>
</template>

<!-- 交互,脚本语言 -->
<script lang="ts" setup name="Upload">
import { Plus, Upload } from "@element-plus/icons-vue";
import type { UploadInstance, UploadRawFile } from "element-plus";
import { computed, ref } from "vue";
import type { FileWithTags } from "@/interface/FileWithTags";
import { ta } from "element-plus/es/locale";
import axios from "axios";

// 获取用户名
const username = localStorage.getItem("user");
// 获取标签
const tags = ref([]);

// 点击上传的文件-输出文件名
const preview = function (file: File) {
  console.log(file);
};

// 添加isEditing状态
const files = ref<File[]>([]);
const selectedFiles = ref<FileWithTags[]>([]);
const editingIndex = ref(-1);

// 文件改变时
const fileHandleChange = function (file: File) {
  files.value.push(file);
  getSelectedFiles(files.value);
};

// 辅助函数,生成selectedFiles的默认值
const getSelectedFiles = (files: File[]) => {
  selectedFiles.value = files.map((file) => {
    const fileWithTags: FileWithTags = {
      file: file,
      tags: "",
    };
    return fileWithTags;
  });
};

// 表单对话框
const tagFormDialogBollean = ref(false);
// 表单数据

// 编辑标签
const editTags = function (index: number) {
  editingIndex.value = index;
  const fileWithTags = selectedFiles.value[index];
  // tags.value = fileWithTags.tags;
  tagFormDialogBollean.value = true; // 弹出对话框
};

// 保存标签
const saveTags = function () {
  tagFormDialogBollean.value = false;
  console.log(selectedFiles.value);
};

// 提交的文件
const uploadFiles = ref(null);

// 跟随文件发送的数据
// 将 fileInfos 转换为 JSON 字符串
const uploadData = computed(() => ({
  username: localStorage.getItem("user") || "",
  fileInfos: JSON.stringify(
    selectedFiles.value.map((file) => ({
      fileName: file.file.name,
      fileSize: file.file.size,
      tags: file.tags,
    }))
  ),
}));
// 将携带参数规范化
// const formatUploadData = function () {
//   uploadData.value.fileInfos = selectedFiles.value.map(file => ({
//     fileName: file.file.name,
//     fileSize: file.file.size,
//     tags: file.tags // 每个文件的标签
//   }))
// };

// 提交文件
// 新增自定义上传方法
const submitFile = async () => {


  // 1. 收集所有文件
  const filesToUpload = files.value; // 当前选中的所有文件
  console.log("@@@", filesToUpload);

  // 2. 构建包含所有文件和元数据的 FormData
  const formData = new FormData();
  formData.append("username", uploadData.value.username);
  formData.append("fileInfos", uploadData.value.fileInfos); // JSON 字符串

  // 添加文件到 FormData
  filesToUpload.forEach((file) => {
    console.log(file);
    formData.append("files", file.raw);
  });

  // 发送请求
  const response = await axios.post("/api/documents", formData, {
  });
  console.log(response.data);
  
  // uploadFiles.value!.submit();
  // console.log(1);
  
  
};

// 成功之后清除文件列表
const removeFiles = function () {
  files.value = [];
  selectedFiles.value
};
</script>

<!-- 样式 -->
<style scoped>
.btn {
  display: flex;
}
</style>