
<template>
  <main>
    <h3>商品列表</h3>

    <el-button @click="dialogFormVisible = true">添加商品</el-button>

    <el-table :data="tableData" style="width: 100%">
      <el-table-column prop="date" label="Date" width="180" />
      <el-table-column prop="name" label="Name" width="180" />
      <el-table-column prop="address" label="Address" />
    </el-table>

    <el-dialog v-model="dialogFormVisible" title="创建商品" width="600">
      <el-form :model="form">
        <el-form-item label="名称" :label-width="formLabelWidth">
          <el-input v-model="form.name" autocomplete="off" />
        </el-form-item>
        <el-form-item label="图片" :label-width="formLabelWidth">
          <input type="file" @change="updateImagePreview" />
          <img class="img-preview" :src="form.img" v-if="form.img" alt="Image Preview" />
        </el-form-item>
        <el-form-item label="价格" :label-width="formLabelWidth">
          <el-input-number v-model="form.price" autocomplete="off" />
        </el-form-item>
      </el-form>
      <template #footer>
        <div class="dialog-footer">
          <el-button @click="dialogFormVisible = false">取消</el-button>
          <el-button type="primary" @click="dialogFormVisible = false">提交</el-button>
        </div>
      </template>
    </el-dialog>
  </main>
</template>



<script setup>
import { ref, reactive } from 'vue'

const dialogFormVisible = ref(false)
const formLabelWidth = 120

const form = reactive({})

const updateImagePreview = (event) => {
  let reader = new FileReader()
  reader.onload = (e) => {
    form.img = e.target.result
  }
  reader.readAsDataURL(event.target.files[0])
}

const tableData = [
  {
    date: '2016-05-03',
    name: 'Tom',
    address: 'No. 189, Grove St, Los Angeles'
  },
  {
    date: '2016-05-02',
    name: 'Tom',
    address: 'No. 189, Grove St, Los Angeles'
  },
  {
    date: '2016-05-04',
    name: 'Tom',
    address: 'No. 189, Grove St, Los Angeles'
  },
  {
    date: '2016-05-01',
    name: 'Tom',
    address: 'No. 189, Grove St, Los Angeles'
  }
]
</script>

<style lang="less" scoped>
@import '@/assets/GoodView.less';
</style>