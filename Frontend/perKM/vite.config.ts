import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    vueDevTools(),
  ],
  build: {
    rollupOptions: {
      output: {
        // 自定义 chunk 分割规则（例如按文件类型分离）
        manualChunks: {
          vue: ['vue', 'vue-router'],
          // utils: ['@/utils'],
        },
        // 静态资源输出到子目录
        assetFileNames: (assetInfo) => {
          const name = assetInfo.name || ''
          if (name.endsWith('.css')) return 'css/[name].[hash].[ext]'
          if (name.endsWith('.png')) return 'images/[name].[hash].[ext]'
          return 'js/[name].[hash].[ext]'
        },
      },
    },
  },
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    },
  },
  server: {
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:5000',
        changeOrigin: true,
        // 这一步是将api给替换掉,后端接口跨域不带api,但是前端接口必须要带
        // rewrite: (path) => path.replace(/^\/api/, '')
      }
    },
    // fs: {
    //   allow: [
    //     'D:/code/All_Learning/MarkdownNotes/images'
    //   ],
    // },
  }
})
