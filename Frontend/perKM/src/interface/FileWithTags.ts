import { ref } from 'vue';

interface FileWithTags {
    file: File;
    tags: string; // 标签字段
  }
  
  const selectedFiles = ref<FileWithTags[]>([]);

  export { selectedFiles };