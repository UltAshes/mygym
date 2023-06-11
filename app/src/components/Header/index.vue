<template>
    <header class="header">
        <!-- 头部的第一行 -->
        <div class="top">
            <div class="container">
                <div class="loginList">
                    <p>Welcome to the Heart Gym</p>
                    <p>
                        <span>try to </span>
                        <router-link to="/login">login</router-Link>
                        <router-link class="register" to="/register">register</router-link>
                    </p>
                </div>
                <div class="typeList">
                    <a href="###">My Gym</a>
                    <a href="###">become the Gym VIP</a>
                    <a href="###">Follow us</a>
                </div>
            </div>
        </div>
        <!--头部第二行 搜索区域-->
        <div class="bottom">
            <h1 class="logoArea">
                <router-link class="logo" to="/home">
                    <img src="./images/logo1.png" alt="">
                </router-link>
            </h1>
            <div class="searchArea">
                <form action="###" class="searchForm">
                    <!--<input 
                    type="text" 
                    id="autocomplete" 
                    class="input-error input-xxlarge" 
                    v-model="keyword"
                    />-->
                    <button class="sui-btn btn-xlarge btn-danger" type="button" @click="goSearch">
                        Rental equipment
                    </button>
                </form>
            </div>
        </div>
    </header>
</template>
  
<script>
export default {
    name: "",
    data() {
        return {
            keyword: ''
        }
    },
    methods: {
        goSearch() {
            //this.$router.push('/search/'+this.keyword+"?k="+this.keyword.toUpperCase())
            //this.$router.push(`/search/${this.keyword}?k=${this.keyword.toUpperCase()}`)
            this.$router.push({name:"search",params:{keyword:this.keyword},query:{k:this.keyword.toLocaleUpperCase()}})
        }
    },
};
</script>
<!--样式-->
<style scoped lang = 'less'>
.header {
    &>.top {
        background-color: #eaeaea;
        height: 30px;
        line-height: 30px;

        .container {
            width: 1200px;
            margin: 0 auto;
            overflow: hidden;

            .loginList {
                float: left;

                p {
                    float: left;
                    margin-right: 10px;

                    .register {
                        border-left: 1px solid #b3aeae;
                        padding: 0 5px;
                        margin-left: 5px;
                    }
                }
            }

            .typeList {
                float: right;

                a {
                    padding: 0 10px;

                    &+a {
                        border-left: 1px solid #b3aeae;
                    }
                }

            }

        }
    }

    &>.bottom {
        width: 1200px;
        margin: 0 auto;
        overflow: hidden;

        .logoArea {
            float: left;

            .logo {
                img {
                    width: 175px;
                    margin: 25px 45px;
                }
            }
        }

        .searchArea {
            float: right;
            margin-top: 35px;

            .searchForm {
                overflow: hidden;

                input {
                    box-sizing: border-box;
                    width: 490px;
                    height: 32px;
                    padding: 0px 4px;
                    border: 2px solid #000000;
                    float: left;

                    &:focus {
                        outline: none;
                    }
                }

                button {
                    height: 50px;
                    width: 200px;
                    background-color: #b54848;
                    border: none;
                    color: #fff;
                    float: left;
                    cursor: pointer;

                    &:focus {
                        outline: none;
                    }
                }
            }
        }
    }
}
</style>
  