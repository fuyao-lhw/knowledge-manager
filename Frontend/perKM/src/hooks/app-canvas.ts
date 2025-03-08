import { ref, onMounted, onBeforeUnmount } from 'vue'

const canvasRef = ref<HTMLCanvasElement>()

// Canvas初始化
const initCanvas = () => {
    const canvas = canvasRef.value!
    const ctx = canvas.getContext('2d')!

    // 设置画布尺寸
    const resize = () => {
        canvas.width = window.innerWidth
        canvas.height = window.innerHeight
    }

    // 绘制示例（星空效果）
    const draw = () => {
        ctx.fillStyle = '#000'
        ctx.fillRect(0, 0, canvas.width, canvas.height)

        // 添加星星示例
        for (let i = 0; i < 200; i++) {
            ctx.beginPath()
            ctx.arc(
                Math.random() * canvas.width,
                Math.random() * canvas.height,
                Math.random() * 2,
                0,
                Math.PI * 2
            )
            ctx.fillStyle = '#fff'
            ctx.fill()
        }
    }
}

export default function () {
    function run() {
        resize()
        draw()
        window.addEventListener('resize', resize)

        // 清理
        onBeforeUnmount(() => {
            window.removeEventListener('resize', resize)
        })
        onMounted(initCanvas)
    }

  return {canvasRef, initCanvas, run}  
}

