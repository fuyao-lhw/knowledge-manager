// 引入defineStore创建store
import { defineStore } from 'pinia'

// 定义并暴露store
export const useWelcomeWordsStore = defineStore('welcomeWords', {
  state: () => {
    return {
      welcomeWords: [
        '让每一条信息都找到归处，让每一次思考都有迹可循',
        '智慧沉淀之处，创新生长之地',
        '知识需要管理，正如星辰需要轨迹',
        '每一片知识碎片，都是点亮思维的星辰',
        '在知识的银河中，构建属于你的星座图谱',
        '让知识不再沉睡，让经验持续发光',
        '让知识在流动中增值，在共享中创新',
        '脑力跃迁准备就绪，开始构建记忆宫殿',
        '每个灵感的星火，都值得被永久存档'
      ],
    }
  },
  actions: {
    
  },
})