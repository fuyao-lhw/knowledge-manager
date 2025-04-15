import { ref, onMounted, onBeforeUnmount } from 'vue'

const canvasRef = ref<HTMLCanvasElement>()
let canvas: HTMLCanvasElement | null = null
let ctx: CanvasRenderingContext2D | null = null

// 提升到外部作用域
const resize = () => {
  if (canvas) {
    canvas.width = window.innerWidth
    canvas.height = window.innerHeight
  }
}

const draw = () => {
  if (ctx && canvas) {
    ctx.fillStyle = '#000'
    ctx.fillRect(0, 0, canvas.width, canvas.height)

    // 星星示例
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

const initCanvas = () => {
  canvas = canvasRef.value!
  ctx = canvas.getContext('2d')!
}

export default function () {
  function run() {
    // 确保初始化后再调用
    if (!canvas || !ctx) initCanvas()
    resize()
    draw()
    window.addEventListener('resize', resize)

    // 清理
    onBeforeUnmount(() => {
      window.removeEventListener('resize', resize)
    })
    onMounted(initCanvas)
  }

  return { canvasRef, initCanvas, run }
}