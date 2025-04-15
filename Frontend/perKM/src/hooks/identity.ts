import { onMounted } from 'vue'
import axios from 'axios'

export default function () {
    const loginApi = "/api/login"
    const registerApi = "/api/register"
    async function postLogin(data: unknown) {
        const response = await axios.post(loginApi, data)
        return response.data
    }

    async function postRegister(data: unknown) {
        const response = await axios.post(registerApi, data)
        return response.data
    }

    // 挂载钩子
    onMounted((data: unknown) => {
        postLogin(data);
        postRegister(data);
    })

    return {postLogin, postRegister}
}
