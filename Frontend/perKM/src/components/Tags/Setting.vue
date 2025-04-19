<!-- 结构,主体 -->
<template>
  <!-- 展示标签数据 -->
  <el-table
    :data="tagsData"
    @selection-change="handleSelectionChange"
  >
    <el-table-column type="selection" />
    <!-- <el-checkbox v-model="selected"></el-checkbox> -->
    <!-- </el-table-column> -->
    <el-table-column label="标签id" prop="tag_id" />
    <el-table-column label="标签名" prop="tag_name">
      <template #default="{ row, column }">
        <el-input v-model="row[column.property]" />
      </template>
    </el-table-column>
  </el-table>
  <!-- 提示 -->
  <div class="tips">
    <el-text type="warning">
      修改:1.选中该标签(可多选);2.输入框里直接修改<br />
      删除:1.选中该标签(可多选)<br />
      点击提交修改/删除即可
    </el-text>
  </div>
  <!-- 提交修改标签的按钮 -->
  <el-button @click="submit_tags">
    <el-icon><Position /></el-icon>
    <span>修改选定的标签</span>
  </el-button>
  <!-- 删除选定的标签的按钮 -->
  <el-popconfirm
    confirm-button-text="确定"
    cancel-button-text="取消"
    title="确定删除选定的标签吗？"
    type="warning"
    icon="el-icon-warning"
    @confirm="delete_tags"
  >
    <template #reference>
      <el-button>
        <el-icon><Delete /></el-icon>
        <span>删除选定的标签</span>
      </el-button>
    </template>
  </el-popconfirm>
  <!-- 新增标签的按钮 -->
  <el-button @click="addTagsBoolean = true">
    <el-icon><CirclePlusFilled /></el-icon>
    <span>新增标签</span>
  </el-button>
  <!-- 新增标签的对话框表单 -->
   <el-dialog v-model="addTagsBoolean">
    <el-form>
      <el-form-item label="标签名">
        <el-input v-model="tagName" />
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="addTags">提交</el-button>
      </el-form-item>
    </el-form>
   </el-dialog>
</template>

<!-- 交互,脚本语言 -->
<script lang="ts" name="TagSetting" setup>
import { ref, onMounted } from "vue";
import axios from "axios";
import { get_tags } from "@/hooks/get_tags.ts"

// 初始化数据
const tagsData = ref([]);

// 多选框选中数据
const selectedRows = ref([]);

// 处理多选框选中数据
const handleSelectionChange = (val: any) => {
  selectedRows.value = val;
  console.log("选中的行", selectedRows.value);
};

// 需要提交的标签数据
const submitTagsData = ref<any>([]);

// 格式化标签数据
const formatTagsData = () => {
  selectedRows.value.forEach((row: any) => {
    submitTagsData.value.push({
      tag_id: row.tag_id,
      tag_name: row.tag_name,
    });
  });
};

// 提交标签数据
const submit_tags = async (id: number, name: string) => {
  formatTagsData(); // 格式化标签数据
  console.log(submitTagsData.value);

  const response = await axios.put("/api/tags", {
    tagsData: submitTagsData.value,
  });
  console.log(response.data);

  get_tags(tagsData);  // 重新获取数据以刷新表格
};

// 删除选定的标签
const delete_tags = async () => {
  formatTagsData(); // 格式化标签数据
  console.log(submitTagsData.value);

  const response = await axios.delete("/api/tags", {
    data: {
      tagsData: submitTagsData.value,
    },
  });
  console.log(response.data);

  get_tags(tagsData);
};

// 新增标签对话框的model
const addTagsBoolean = ref(false);

// 新增标签名
const tagName = ref("");

// 新增标签的方法
const addTags = async () => {
    console.log("标签名", tagName.value);
    
    // 发送请求q
    const response = await axios.post("/api/tags", {
        tag_name: tagName.value,
        username: localStorage.getItem("user"),
    });
    console.log("返回数据", response.data);

    // 刷新组件
    get_tags(tagsData);
    

    // 关闭新增标签的对话框
    addTagsBoolean.value = false;
};

onMounted(() => {
  get_tags(tagsData);
  
});
</script>

<!-- 样式 -->
<style scoped>
</style>