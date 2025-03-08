<template>
    <div class="user-info">
      <el-dropdown trigger="click" v-if="username !== null">
        <div class="user-container">
          <el-avatar
            :size="32"
            :src="user.avatar || 'https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png'"
          />
          <span class="username" >{{ username.replace("@qq.com", "") }}</span>
          <el-icon class="arrow"><CaretBottom /></el-icon>
        </div>
        <template #dropdown>
          <el-dropdown-menu>
            <el-dropdown-item @click="handleProfile">
              <el-icon><User /></el-icon>个人中心
            </el-dropdown-item>
            <el-dropdown-item divided @click="handleLogout">
              <el-icon><SwitchButton /></el-icon>退出登录
            </el-dropdown-item>
          </el-dropdown-menu>
        </template>
      </el-dropdown>
      <el-dropdown trigger="click" v-else>
        <div class="user-container">
          <el-avatar
            :size="32"
            :src="user.avatar || 'https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png'"
          />
          <span class="username" >未登录</span>
          <el-icon class="arrow"><CaretBottom /></el-icon>
        </div>
        <template #dropdown>
          <el-dropdown-menu>
            <el-dropdown-item  @click="handleLogout">
              <el-icon><SwitchButton /></el-icon>去登录
            </el-dropdown-item>
          </el-dropdown-menu>
        </template>
      </el-dropdown>
    </div>
  </template>
  
  <script lang="ts" setup>
  import { ref } from 'vue'
  import { useRouter } from 'vue-router'
  import {
    CaretBottom,
    User,
    SwitchButton
  } from '@element-plus/icons-vue'
  
  const router = useRouter()
  
  // 用户信息（可替换为真实数据）
  const user = ref({
    name: '管理员',
    avatar: '',
    role: '系统管理员'
  })

  // 获取用户信息
  const username = localStorage.getItem('user')

  
  const handleProfile = () => {
    router.push('/personal')
  }
  
  const handleLogout = () => {
    // 实际项目中应调用退出接口
    localStorage.removeItem('user')
    router.push('/login')
  }
  </script>
  
  <style scoped>
  .user-container {
    display: flex;
    align-items: center;
    padding: 0 10px;
    cursor: pointer;
    transition: all 0.3s;
    
    &:hover {
      background: rgba(255, 255, 255, 0.08);
    }
  }
  
  .username {
    margin: 0 8px;
    color: #fff;
    font-size: 14px;
  }
  
  .arrow {
    color: #fff;
    font-size: 12px;
    margin-left: 2px;
  }
  
  .el-dropdown-menu__item {
    display: flex;
    align-items: center;
    
    .el-icon {
      margin-right: 8px;
    }
  }
  </style>