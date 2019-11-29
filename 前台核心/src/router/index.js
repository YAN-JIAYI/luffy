import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Free from '../views/Free.vue'
import Course from '../views/Course.vue'
import LightCourse from '../views/LightCourse.vue'

Vue.use(VueRouter);

const routes = [
    {
        path: '/',
        name: 'home',
        component: Home
    },
    {
        path: '/home',
        redirect: '/'
    },
    {
        path: '/free',
        name: 'free',
        component: Free
    },
    {
        path: '/course',
        name: 'course',
        component: Course
    },
    {
        path: '/light-course',
        name: 'light-course',
        component: LightCourse
    },
];

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
});

export default router
