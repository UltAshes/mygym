import axios from "axios";


const requests = axios.create({
    //baseURL:'api',
    baseURL: 'http://127.0.0.1:5000',
    timeout: 15000,
    responseType: 'json',
    headers: { 'content-type': 'application/json' },
});
//请求拦截器
requests.interceptors.request.use((config)=>{
  return config;
});
//响应拦截器
requests.interceptors.response.use((res)=>{
  return res.data;
},(error)=>{
  return Promise.reject(new Error('faile'))
}
);
export default requests;