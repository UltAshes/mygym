<template>
    <div class="footer">
        <div class="footer-container">
            <div class="footerList">
                <div class="footerItem">
                <div class="footerItem">
                    <!--<img src="./images/wx_cz.jpg"> -->
                </div>
            </div>
            </div>
            <div class="copyright">
                <h3>daily knowledge</h3>
                <p>In addition to physical benefits of exercise, it is also to make a fresh spirit of the people to keep the best way。</p>
                <p></p>
            </div>
        </div>
    </div>
</template>

<script>

</script>

<style scoped lang="less">
.footer {
    background-color: #eaeaea;
    h3{
        text-align: center;
    }
    .footer-container {
        width: 1200px;
        margin: 0 auto;
        padding: 0 15px;

        .footerList {
            padding: 20px;
            border-bottom: 1px solid #e4e1e1;
            border-top: 1px solid #e4e1e1;
            overflow: hidden;
            padding-left: 535px;

            .footerItem {
                width: 16.6666667%;
                float: left;

                h4 {
                    font-size: 14px;
                }

                .footerItemCon {
                    li {
                        line-height: 18px;
                    }
                }

                &:last-child img {
                    width: 121px;
                }
            }
        }

        .copyright {
            padding: 20px;

            .helpLink {
                text-align: center;

                li {
                    display: inline;

                    .space {
                        border-left: 1px solid #666;
                        width: 1px;
                        height: 13px;
                        background: #666;
                        margin: 8px 10px;
                    }
                }
            }

            p {
                margin: 10px 0;
                text-align: center;
            }
        }
    }
}
</style>