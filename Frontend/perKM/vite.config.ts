import { fileURLToPath, URL } from 'node:url'
import legacy from '@vitejs/plugin-legacy';
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    vueDevTools(),
    legacy({
      targets: ['defaults', 'not IE 11'],
      additionalLegacyPolyfills: ["regenerator-runtime/runtime"],
    }),
  ],
  base: "",  // 配置文件的根目录为相对路径
  assetsInclude: ['**/*.md'],

  build: {
    assetsDir: 'assets',  // 配置静态资源目录


    rollupOptions: {
      output: {
        manualChunks: {
          // 手动拆分代码块（优化分包）
          vue: ['vue', 'vue-router'],
          lodash: ['lodash'],
        },
        // 配置静态资源打包
        chunkFileNames: 'js/[name]-[hash].ts',
        entryFileNames: 'js/[name]-[hash].ts',

        // 配置CSS静态资源打包
        assetFileNames: (assetInfo) => {
          if (assetInfo.name === 'style.css') {
            return 'css/[name]-[hash].css';
          }
          return 'css/[name]-[hash].[ext]';
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
