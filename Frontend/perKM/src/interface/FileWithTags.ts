import { ref } from 'vue';

export interface FileWithTags {
    file: File;
    tags: string; // 标签字段
  }
  
  const selectedFiles = ref<FileWithTags[]>([]);

export default {selectedFiles};