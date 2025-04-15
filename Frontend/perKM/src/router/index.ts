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
            component: () => import('@/pages/IndexPage.vue'),
            redirect: '/documents/info',
            children: [
                {
                    path: '/documents/info',
                    component: () => import('@/components/Documents/Info.vue')
                },
                {
                    path: '/documents/list',
                    component: () => import('@/components/Documents/List.vue')
                },
                {
                    path: '/documents/upload',
                    component: () => import('@/components/Documents/Upload.vue')
                },
                {
                    path: '/documents/edit',
                    component: () => import('@/components/Documents/Edit.vue')
                },
            ]
        },
        {
            path: '/personal',
            component: () => import('@/pages/PersonalCenterPage.vue')
        },
        {
            path: '/document/:document_id',
            // component: () => import('@/pages/DocumentDetailPage.vue')
            component: () => import('@/components/Documents/Detail.vue')
        },
    ]
})
export default router