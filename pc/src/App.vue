<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <div class="page-home-layout">
    <header class="page-header">
      <div class="wrapper"></div>
    </header>
    <div class="Main">
      <div class="menu">
        <nav class="nav">
          <RouterLink to="/">首页</RouterLink>
          <RouterLink to="/good">商品</RouterLink>
          <RouterLink to="/order">订单</RouterLink>
        </nav>
      </div>
      <div class="Content">
        <RouterView />
      </div>
    </div>
  </div>
</template>

<style scoped lang="less">
.page-header {
  height: 40px;
  border-bottom: 1px solid rgba(0, 0, 0, 0.17);
}

.menu {
  width: 120px;
  border-right: 1px solid rgba(0, 0, 0, 0.17);
  .nav {
    a {
      display: block;
      text-align: center;
      text-decoration: none;
      margin-top: 10px;
      cursor: pointer;
    }
  }
}

.page-home-layout {
  display: flex;
  flex-direction: column;
  height: 100%;
}

.Main {
  height: 100%;
  display: flex;
}

.Content{
  padding: 20px;
}
</style>
