import axios from "axios";
import { ref } from "vue";

// 初始化数据
// const tags_data = ref([]);
const get_tags = async (tagsData: any) => {
    const response = await axios.get("/api/tags");
    console.log(response.data);
    tagsData.value = response.data.data;
    return response.data.data;
  };

export { get_tags };