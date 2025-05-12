import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import router from '@/router'
import { createApp } from 'vue'
import App from './App.vue'
import { createPinia } from 'pinia'
import '@/assets/css/app.css'  // 引入全局基础css文件
import 'github-markdown-css';
import * as ElementPlusIconsVue from '@element-plus/icons-vue'

const app = createApp(App);
const pinia = createPinia();

app.use(router);
app.use(ElementPlus);
app.use(pinia);
app.mount('#app');

for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
  app.component(key, component)
}

const cvs = document.getElementById('stroke') as HTMLCanvasElement;
function init() {
  cvs.width = window.innerWidth;
  cvs.height = window.innerHeight;
}

init();



createApp(App).mount('#app')