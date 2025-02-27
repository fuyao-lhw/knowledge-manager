import { ref, onMounted, reactive } from 'vue'
import axios from 'axios'

export default function () {
    const loginApi = "/api/login"
    const registerApi = "/api/register"
    async function postLogin(data) {
        const response = await axios.post(loginApi, data)
        return response.data
    }

    async function postRegister(data) {
        const response = await axios.post(registerApi, data)
        return response.data
    }

    // 挂载钩子
    onMounted(() => {
        postLogin();
        postRegister();
    })

    return {postLogin, postRegister}
}
