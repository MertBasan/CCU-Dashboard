<template>
<div class="tableContainer">
  <el-table :data="pagedData" row-key="encounterId" height="500" style="width: 100%" :row-class-name="tableRowClassName">
    <el-table-column type="expand">
      <template #default="{ row }">
        <p v-for="(item, index) in row" :key="index">
          {{ index.replaceAll('_', ' ') }}: {{ item }}
        </p>
      </template>
    </el-table-column>
    <el-table-column label="Encounter ID" prop="encounterId" /> 
    <el-table-column label="BMI" prop="bmi" />

    <el-table-column
      prop="referral"
      label="Referal Status"
      width="200"
      :filters="[
          { text: 'Referred', value: '1.0' },
          { text: 'Unreferred', value: '0.0' },
        ]"
      :filter-method="filterTag"
      filter-placement="bottom-end"
    >
      <template #default="scope">
        <el-tag   
          :type="scope.row.referral === '1.0' ? '' : 'success'"
          disable-transitions
          >{{ scope.row.referral === '1.0' ? 'Referred' : 'Unreferred' }}
        </el-tag>
      </template>
    </el-table-column>
  </el-table>

  <el-pagination class="text-center" layout="prev, pager, next" :total="tableData.length" :page-size="pageSize"  @current-change="setPage" />
</div>
</template>

<script setup>
import { ref, computed, defineProps } from 'vue'

const curPage = ref(1)
const pageSize = 248

const tableProps = defineProps({
  tableData: Array,
  search: String
})

const tableRowClassName = ({ row }) => {
  if (row.flag === 1) {  
    return 'warning-row'; 
  } else if (row.flag === 2) {
    return 'urgent-row';
  }
  return '';
}

const setPage = (page) => {
  curPage.value = page
}

const pagedData = computed(() =>
  tableProps.tableData
    .filter(
      (data) =>
        !tableProps.search ||
        data.encounterId.includes(tableProps.search)
    )
    .slice(pageSize * curPage.value - pageSize, pageSize * curPage.value)
)

const filterTag = (value, row) => {
  return row.referral === value
}
</script>

<style>
p {
  margin-left: 55px;
}

.tableContainer{
  margin-top: 30px;
}

.el-table .warning-row {
  --el-table-tr-bg-color: #b87a48;
}

.el-table .urgent-row {
  --el-table-tr-bg-color: #8d3838;
}

.el-table   {
  --el-table-bg-color: #2B2740;
  --el-table-header-bg-color: #3A3554;
  --el-table-header-text-color: #F2E9E4;
  --el-table-tr-bg-color: #494365;
  --el-table-expanded-cell-bg-color: #494365;
  --el-table-row-hover-bg-color: #5a5379;
  --el-table-border-color: none;
  color: #DBDBDB;

  --el-table-border: 3px solid #2B2740;

}

.el-pagination {
  padding-top: 15px;
  --el-pagination-text-color: #DBDBDB;
  justify-content: center;
  --el-pagination-bg-color: #2B2740;
  --el-pagination-button-bg-color: #2B2740;
  --el-pagination-button-disabled-bg-color: #2B2740;
  --el-pagination-button-color: #DBDBDB;
  --el-pagination-hover-color: #b87a48;
}

.el-table__expand-icon {
  color: #DBDBDB;
}

</style>
