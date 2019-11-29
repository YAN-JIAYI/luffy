<template>
    <div class="banner">
        <el-carousel height="400px">
            <el-carousel-item v-for="banner in banner_list" :key="banner.title">
                <router-link :to="banner.link">
                    <img :src="banner.image" alt="" :title="banner.title">
                    <!--<div class="img"></div>-->
                </router-link>
            </el-carousel-item>
        </el-carousel>
    </div>
</template>

<script>
    export default {
        name: "Banner",
        data() {
            return {
                banner_list: [],
            }
        },
        created() {
            // 请求轮播图数据
            // this.$axios({
            //     url: this.$settings.base_url + '/home/banners',
            // });
            // 直接发送get请求
            this.$axios.get(this.$settings.base_url + '/home/banners').then(response => {
                // console.log(response)
                this.banner_list = response.data
            })
        }
    }
</script>

<style scoped>
    .banner {
        height: 400px;
    }

    .banner img {
        height: 400px;
        margin-left: calc(50% - 1920px / 2);
    }

    .banner .img {
        height: 400px;
        /*background-color: red;*/
        background-image: url("../assets/img/banner1.png");
        background-size: auto 400px;
        background-position: center;
    }
    .el-carousel__item {
        min-width: 1200px;
    }



</style>