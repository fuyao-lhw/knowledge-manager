import { createRouter, createWebHistory, createWebHashHistory } from 'vue-router';
import WelcomePage from '@/pages/WelcomePage.vue';
import LoginPage from '@/pages/LoginPage.vue';
import RegisterPage from '@/pages/RegisterPage.vue';
import IndexPage from '@/pages/IndexPage.vue';
import DocumentInfo from '@/components/Documents/Info.vue';
import DocumentList from '@/components/Documents/List.vue';
import DocumentUpolad from '@/components/Documents/Upload.vue';
import DocumentSetting from '@/components/Documents/Setting.vue';
import DocumentDetail from '@/components/Documents/Detail.vue';
import TagsList from '@/components/Tags/List.vue';
import TagsDetail from '@/components/Tags/Detail.vue';
import TagsSetting from '@/components/Tags/Setting.vue';
import SearchResult from '@/components/Search/Result.vue';
import KnowledgeGraph from '@/components/Knowledge/Graph.vue';





const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/',
            redirect: '/welcome'
        },
        {
            path: '/welcome',
            component: WelcomePage
        },
        {
            path: '/login',
            component: LoginPage
        },
        {
            path: '/register',
            component: RegisterPage
        },
        {
            path: '/index',
            component: IndexPage,
            redirect: '/documents/info',
            children: [
                {
                    path: '/documents/info',
                    component: DocumentInfo
                },
                {
                    path: '/documents/list',
                    component: DocumentList
                },
                {
                    path: '/documents/upload',
                    component: DocumentUpolad
                },
                {
                    path: '/documents/setting',
                    component: DocumentSetting
                },
                {
                    path: '/document/:document_id',
                    component: DocumentDetail
                },
                {
                    path: '/tags/list',
                    component: TagsList
                },
                {
                    path: '/tags/:tag_id',
                    component: TagsDetail
                },
                {
                    path: '/tags/setting',
                    component: TagsSetting
                },
                {
                    path: '/search/result',
                    component: SearchResult
                },
                {
                    path: '/knowledge/graph',
                    component: KnowledgeGraph
                },
            ]
        },
        {
            path: '/personal',
            component: () => import('@/pages/PersonalCenterPage.vue')
        },
        {
            path: '/tags',
            children: [

            ]
        },
        
    ]
})
export default router