import Vue from 'vue'
import VueRouter from 'vue-router'
Vue.use(VueRouter);
import Home from '@/pages/Home'
import Search from '@/pages/Search'
import Register from '@/pages/Register'
import Login from '@/pages/Login'
import ShopCart from '@/pages/ShopCart'
import Center from '@/pages/Center'
import pay from '@/pages/Pay'
import paysuccess from '@/pages/PaySuccess'
export default new VueRouter({
    routes:[
        {
            path:"/home",
            component:Home,
            meta:{show:true}
        }
        ,
        {
            path:"/search/:keyword?",
            component:Search,
            meta:{show:true},
            name:"search"
        }
        ,
        {
            path:"/login",
            component:Login,
            meta:{show:false}
        }
        ,
        {
            path:"/register",
            component:Register,
            meta:{show:false}
        }
        ,
        {
            path:"/shopcart",
            component:ShopCart,
            meta:{show:false}
        }
        ,
        {
            path:"/Center",
            component:Center,
            meta:{show:false}
        }
        ,
        {
            path:"/pay",
            component:pay,
            meta:{show:false}
        }
        ,
        {
            path:"/paysuccess",
            component:paysuccess,
            meta:{show:false}
        }
        ,
        {
            path:'*',
            redirect:'/home'
        }

    ]
})