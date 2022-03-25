<template>
  <div class="button-container">
    <el-upload
      ref="upload"
      class="upload-demo"
      action="http://localhost:5000/uploader"
      method = "POST" 
      :limit="1"
      :on-exceed="handleExceed"
      :on-success="uploadSuccess"
      :auto-upload="true"
      :show-file-list="false">
      <template #trigger>
        <el-button type="primary">Upload CSV</el-button>
      </template>
    </el-upload>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
const upload = ref()
const emit = defineEmits(['uploadSuccess'])

const handleExceed = (files) => {
  upload.value.clearFiles()
  upload.value.handleStart(files[0])
}

const uploadSuccess = (res) => {
  emit('uploadSuccess', res)
}
</script>

<style>
  .button-container { 
    display: flex; 
    align-content: center;
    padding-left: 20px;
  }
</style>