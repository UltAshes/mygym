import Vue from 'vue'
import App from './App.vue'
//三级联动组件注册为全局组件
import TypeNav from '@/components/TypeNav';
Vue.component(TypeNav.name,TypeNav)
//引入路由
import router from '@/router'
Vue.config.productionTip = false
import store from '@/store'
new Vue({
  render: h => h(App),
  router,
  store
}).$mount('#app')
