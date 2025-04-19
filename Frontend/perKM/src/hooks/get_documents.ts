import axios from "axios";

async function get_document_list(documentList: any) {
    const response = await axios.get("/api/documents?form=all");
    console.log("文档列表:", response.data);
    if (response.data.status == 200) {
        documentList.value = response.data.data;
    } else {
        console.log("获取文档列表失败");
    }
}

export { get_document_list };