<template>
    <div class="type-nav">
        <div class="container">
            <a href="https://dashing-camellia-dswbsb.mystrikingly.com/" target="_blank">
            <h2 class="all">Training video</h2>
            </a>
            <div class="sort">
                <div class="all-sort-list2">
                    <div class="item" v-for="(c1,index) in categoryList" :key="c1.categoryId">
                        <h3>
                            <a href="">{{c1.categoryName}}</a>
                        </h3>
                        <div class="item-list clearfix">
                            <div class="subitem" v-for="(c2,index) in c1.categoryChild" :key="c2.categoryId">
                                <dl class="fore">
                                    <dt>
                                        <a href="">{{c2.categoryName}}</a>
                                    </dt>
                                    <dd>
                                        <em v-for="(c3,index) in c2.categoryChild" :key="c3.categoryId">
                                            <a href="">{{c3.categoryName }}</a>
                                        </em>
                                    </dd>
                                </dl>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
    
<script>
import { mapState } from 'vuex';
export default {
    name: 'TypeNav',
    mounted(){
        this.$store.dispatch('categoryList')
    },
    computed:{
        ...mapState({
            categoryList:state=>state.home.categoryList
            
})
    }
}
</script>
    
<style scoped lang="less">
.type-nav {
    border-bottom: 2px solid #000000;

    .container {
        width: 1200px;
        margin: 0 auto;
        display: flex;
        position: relative;

        .all {
            width: 210px;
            height: 45px;
            background-color: #000000;
            line-height: 45px;
            text-align: center;
            color: #fff;
            font-size: 14px;
            font-weight: bold;
        }

        .nav {
            a {
                height: 45px;
                margin: 0 22px;
                line-height: 45px;
                font-size: 16px;
                color: #333;
            }
        }

        .sort {
            position: absolute;
            left: 0;
            top: 45px;
            width: 210px;
            height: 461px;
            position: absolute;
            background: #fafafa;
            z-index: 999;

            .all-sort-list2 {
                .item {
                    h3 {
                        line-height: 30px;
                        font-size: 14px;
                        font-weight: 400;
                        overflow: hidden;
                        padding: 0 20px;
                        margin: 0;

                        a {
                            color: #333;
                        }
                    }

                    .item-list {
                        display: none;
                        position: absolute;
                        width: 734px;
                        min-height: 460px;
                        background: #f7f7f7;
                        left: 210px;
                        border: 1px solid #ddd;
                        top: 0;
                        z-index: 9999 !important;

                        .subitem {
                            float: left;
                            width: 650px;
                            padding: 0 4px 0 8px;

                            dl {
                                border-top: 1px solid #eee;
                                padding: 6px 0;
                                overflow: hidden;
                                zoom: 1;

                                &.fore {
                                    border-top: 0;
                                }

                                dt {
                                    float: left;
                                    width: 54px;
                                    line-height: 22px;
                                    text-align: right;
                                    padding: 3px 6px 0 0;
                                    font-weight: 700;
                                }

                                dd {
                                    float: left;
                                    width: 415px;
                                    padding: 3px 0 0;
                                    overflow: hidden;

                                    em {
                                        float: left;
                                        height: 14px;
                                        line-height: 14px;
                                        padding: 0 8px;
                                        margin-top: 5px;
                                        border-left: 1px solid #ccc;
                                    }
                                }
                            }
                        }
                    }

                    &:hover {
                        .item-list {
                            display: block;
                        }
                    }
                }
            }
        }
    }
}
</style>