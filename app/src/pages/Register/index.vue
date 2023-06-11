<template>
  <div class="register-container">
    <!-- 注册内容 -->
    <div class="register">
      <h3>Register
        <span class="go">I have a Accont, to
          <router-link to="/login" target="_blank">Login</router-link>
        </span>
      </h3>
      <div class="content">
        <label>Phone:</label>
        <input type="text" placeholder="Please Enten Your Phone Number" v-model="phone">
        <span class="error-msg"></span>
      </div>
      <div class="content">
        <label>Code:</label>
        <input type="text" placeholder="Please Enten the Code" v-model="code">
        <button style="width: 100px;height: 38px;" @click="getCode">Get a Code</button>
        <span class="error-msg"></span>
      </div>
      <div class="content">
        <label>Password:</label>
        <input type="password" placeholder="Please Enten Your Password" v-model="password">
        <span class="error-msg"></span>
      </div>
      <div class="content">
        <label>password:</label>
        <input type="password" placeholder="Please Enten Your Password Again" v-model="password1">
        <span class="error-msg"></span>
      </div>
      <div class="controls">
        <input name="m1" type="checkbox" :checked="agree" />
        <span>Agree our consent</span>
        <span class="error-msg"></span>
      </div>
      <div class="btn">
        <button @click="userRegister">Registration complete</button>
      </div>
    </div>

    <!-- 底部 -->
    <div class="copyright">
      <div class="address">address：FuZhou university</div>
      <div class="beian">
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Register',
  data() {
    return {
      phone: '',
      code: '',
      password: '',
      password1: '',
      agree: true
    }
  },
  methods: {

    async getCode() {
      try {
        const { phone } = this;
        phone && (await this.$store.dispatch('getCode', phone));
        this.code = this.$store.state.user.code;
      }
      catch (error) {

      }
    },
    async userRegister(){
      try{
      const {phone,code,password,password1}= this;
      if (phone &&code&&password==password1) {
        await this.$store.dispatch('userRegister',{phone,code,password});
        this.$router.push('/login');
      }else{
        alert(error.message);
      }
      }catch(error){
        alert(error.message);
      }
    }
  }
}
</script>

<style lang="less" scoped>
.register-container {
  .register {
    width: 1200px;
    height: 445px;
    border: 1px solid rgb(223, 223, 223);
    margin: 0 auto;

    h3 {
      background: #ececec;
      margin: 0;
      padding: 6px 15px;
      color: #333;
      border-bottom: 1px solid #dfdfdf;
      font-size: 20.04px;
      line-height: 30.06px;

      span {
        font-size: 14px;
        float: right;

        a {
          color: #000000;
        }
      }
    }

    div:nth-of-type(1) {
      margin-top: 40px;
    }

    .content {
      padding-left: 390px;
      margin-bottom: 18px;
      position: relative;

      label {
        font-size: 14px;
        width: 96px;
        text-align: right;
        display: inline-block;
      }

      input {
        width: 270px;
        height: 38px;
        padding-left: 8px;
        box-sizing: border-box;
        margin-left: 5px;
        outline: none;
        border: 1px solid #999;
      }

      img {
        vertical-align: sub;
      }

      .error-msg {
        position: absolute;
        top: 100%;
        left: 495px;
        color: rgb(0, 0, 0);
      }
    }

    .controls {
      text-align: center;
      position: relative;

      input {
        vertical-align: middle;
      }

      .error-msg {
        position: absolute;
        top: 100%;
        left: 495px;
        color: rgb(0, 0, 0);
      }
    }

    .btn {
      text-align: center;
      line-height: 36px;
      margin: 17px 0 0 55px;

      button {
        outline: none;
        width: 270px;
        height: 36px;
        background: #000000;
        color: #fff !important;
        display: inline-block;
        font-size: 16px;
      }
    }
  }

  .copyright {
    width: 1200px;
    margin: 0 auto;
    text-align: center;
    line-height: 24px;

    ul {
      li {
        display: inline-block;
        border-right: 1px solid #e4e4e4;
        padding: 0 20px;
        margin: 15px 0;
      }
    }
  }
}
</style>