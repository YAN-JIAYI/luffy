import Vue from 'vue'
import App from './App.vue'
import router from './router'
import router from './router'
import store from './store'

Vue.config.productionTip = false;

// 全局样式和配置
import '@/assets/css/global.css'
import settings from '@/assets/js/settings'
Vue.prototype.$settings = settings;


// ajax配置axios
import axios from 'axios'
Vue.prototype.$axios = axios;

// 配置vue-cookies
import cookies from 'vue-cookies'
Vue.prototype.$cookies = cookies;

// 配置element-ui
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
Vue.use(ElementUI);

// 配置bs+jq配置
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'


new Vue({
    router,
    store,
    render: h => h(App)
}).$mount('#app');
