import requests from "./request";

export const reqCategoryList =()=>requests({url:'/home',method:'get'})
export const reqGetCode =(phone)=>requests({url:`/register/send/${phone}`,method:'get'})
//export const reqGetCode =(phone)=>requests({url:`/user/passport/sendCode/${phone}`,method:'get'})

export const reUserRegister= (data)=>requests({url:"/register/create",data,method:"post"})
export const reqUserLogin= (data)=>requests({url:"/login",data,method:"post"})