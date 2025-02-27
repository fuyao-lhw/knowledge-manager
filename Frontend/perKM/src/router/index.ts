import { createRouter, createWebHistory } from 'vue-router';
import LoginPage from '@/pages/LoginPage.vue'



const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/',
            redirect: '/welcome'
        },
        {
            path: '/welcome',
            component: () => import('@/pages/WelcomePage.vue')
        },
        {
            path: '/login',
            component: LoginPage
        },
        {
            path: '/register',
            component: () => import('@/pages/RegisterPage.vue')
        },
        {
            path: '/index',
            component: () => import('@/pages/IndexPage.vue')
        },
        {
            path: '/test',
            component: () => import('@/pages/TestPage.vue')
        },
    ]
})

export default router