// import { createRouter, createWebHashHistory } from 'vue-router'
// import HomeView from '../views/HomeView.vue'
// import Vue from 'vue'
import * as createRouter from 'vue-router'
import Post from '@/components/PostIndex'
import Author from '@/components/AuthorIndex'
import PostsByTag from '@/components/PostsByTag'
import AllPosts from '@/components/AllPosts'

// Vue.use(VueRouter)

const router = createRouter([
    // {path: '/', name: 'home', component: HomeView},
    { path: '/author/:username', component: Author },
    { path: '/post/:slug', component: Post },
    { path: '/tag/:tag', component: PostsByTag },
    { path: '/', component: AllPosts },
    { path: '/about', name: 'about', component: () => import('../views/AboutView.vue') },
])

// const router = new VueRouter({
//     routes: routes,
//     mode: 'history',
// })

export default router
