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
        :success="removeFiles"
        :before-upload="beforeUpload"
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
      <el-form-item label="输入标签">
        <el-input v-model="selectedFiles[editingIndex].tags" />
        <el-text type="warning">
          输入多个标签,以英文逗号分割<br>
          未创建的标签会自动创建
        </el-text>
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
import { computed, ref } from "vue";
import type { FileWithTags } from "@/interface/FileWithTags";
import axios from "axios";


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

// 限制文件大小为 5MB
const MAX_FILE_SIZE = 5 * 1024 * 1024; 
// 上传文件之前的钩子
const beforeUpload = (file) => {
  if (file.size > MAX_FILE_SIZE) {
    alert(`文件 ${file.name} 大小超过 5MB，无法上传`);
    return false;
  }
  return true;
};


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