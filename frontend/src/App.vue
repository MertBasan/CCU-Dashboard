
<template>
  <div class="container">
    <div class="nav">
      <el-input class="input" v-model="search" placeholder="Search by EncounterID..." />
      <top-bar class="btn" @uploadSuccess="handleData" />
      <download class="btn" />
    </div>
    <el-row>
      <el-col :span="24">
        <data-table :table-data="tableData" :search="search" />
      </el-col>
    </el-row>
  </div>
</template>

<script setup lang="ts">
  import { ref } from 'vue'

  const hasUploaded = ref(false)
  const needsReferral = ref(0)
  const tableData = ref([])

  const search = ref('')

  function handleData (res, file) {
    hasUploaded.value = true
    tableData.value = res 
  }
</script>

<style>
@import './assets/base.css';

body {
  background: #1D1A2A;
}

.container {
  padding: 100px 400px;
}

.el-input {
  --el-input-text-color: #DBDBDB;
}

.el-input__inner {
  background-color: #483F75;
  padding: 12px;
  text-align: left;
  box-shadow: none;
}

.el-button {
    background-color: #7254EF;
    border: none;
}

.nav {
  display: flex;
  width: 100%;
}

.nav .btn {
  justify-self: end;
  margin-left: 12px;
}

.nav .input {
  padding-right: 550px;
}
</style>
