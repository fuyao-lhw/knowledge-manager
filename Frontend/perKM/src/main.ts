import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import router from '@/router'
import { createApp } from 'vue'
import App from './App.vue'
import {createPinia} from 'pinia'
import '@/assets/css/app.css'  // 引入全局基础css文件

const app = createApp(App);
const pinia = createPinia();

app.use(router);
app.use(ElementPlus);
app.use(pinia);
app.mount('#app');

// createApp(App).mount('#app')

const cvs = document.getElementById('stroke');
function init(){
    cvs.width = window.innerWidth;
    cvs.height = window.innerHeight;
}

init();
