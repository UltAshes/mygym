import { reqGetCode,reUserRegister,reqUserLogin} from "@/api";
const state = {
    code : "",
    token: ''
};
const mutations = {
    GETCODE(state,code){
        state.code = code;
    },
    USERLOGIN(state,token){
        state.token=token;
    }
};
const actions = {
    async getCode({commit},phone){
        let result = await reqGetCode(phone);
        if (result.code == 200){
            commit("GETCODE",result.data);
            return 'ok'
        }else{
            return Promise.reject(new Error('faile'))
        }
    },
    async userRegister({commit},user){
        let result = await reUserRegister(user)
        if(result.code==200){
            return'ok';
        }else{
            return Promise.reject(new Error('faile'))
        }
    },
    async userLogin({commit},data){
        let result = await reqUserLogin(data);
        if(result.code==200){
            commit("USERLOGIN",result.data.token);
            return "ok"
        }else{
            return Promise.reject(new Error("faile"));
        }
    }
};
const getters = {};
export default{
    state,
    mutations,
    actions,
    getters
}   