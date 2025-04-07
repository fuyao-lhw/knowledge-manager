<!-- 结构,主体 -->
<template>
  <div class="personal">
    <el-card title="个人信息" class="personal-info">
      <template #header>个人信息</template>
      <p>
        <span>用户名:</span>
        <span>{{ username }}</span>
      </p>
      <p>
        <el-button round @click="transPwd = true">修改密码</el-button>
      </p>

      <el-dialog v-model="transPwd" title="修改密码"> 
        <el-form>
          <el-form-item label="旧密码">
            <el-input v-model="form_pwd.old_pwd" placeholder="旧密码"></el-input>
          </el-form-item>
          <el-form-item label="新密码">
            <el-input v-model="form_pwd.new_pwd" placeholder="新密码"></el-input>
          </el-form-item>
          <el-form-item label="确认密码">
            <el-input v-model="form_pwd.confirm_pwd" placeholder="确认密码"></el-input>
          </el-form-item>
          <el-form-item label="验证码">
            <el-input v-model="form_pwd.verify_code" placeholder="验证码"></el-input>
            <el-button @click="send_code">发送验证码</el-button>
          </el-form-item>
          <el-button @click="transPassword">提交</el-button>
        </el-form>
      </el-dialog>
      <!-- <p class="avatar">
      <span>头像:</span>
      <el-image
        src="https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png"
        fit="contain"
      />
    </p> -->
    </el-card>

  </div>
</template>

<!-- 交互,脚本语言 -->
<script lang="ts" setup name="PersonalCenterPage">
import { reactive, ref } from "vue";
import axios from "axios";

const username = localStorage.getItem("user");

const transPwd = ref(false);

const form_pwd = ref({
  email: username,
  old_pwd: "",
  new_pwd: "",
  confirm_pwd: "",
  verify_code: "",
})

// 提交申请
async function send_code() {
    console.log('发送验证码申请...')
    const response = await axios.post("/api/verify_code", {email: form_pwd.value.email});
    console.log(response.data)
}

async function transPassword() {
  if (form_pwd.value.new_pwd !== form_pwd.value.confirm_pwd){
    alert("两次密码不一致");
  } else if(form_pwd.value.new_pwd === ""){
    alert("密码不能为空");
  } else if (form_pwd.value.verify_code === ""){
    alert("验证码不能为空");
  } else {
    const response = await axios.post("/api/trans_pwd", form_pwd.value);
    console.log(response.data);
  }
}
</script>

<!-- 样式 -->
<style scoped>
.personal {
  display: flex;
  flex-direction: column; /* 垂直排列 */
  gap: 30px; /* 设置元素之间的间隙 */
  border: 1px solid #000;
  padding: 10px;
}

.avatar {
  padding: 30px 0;
  text-align: center;
  border-right: solid 1px var(--el-border-color);
  display: inline-block;
  width: 20%;
  box-sizing: border-box;
  vertical-align: top;
}
.avatar:last-child {
  border-right: none;
}
</style>