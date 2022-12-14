import { createRouter, createWebHistory } from 'vue-router'
import Post from '@/components/PostIndex'
import Author from '@/components/AuthorIndex'
import PostsByTag from '@/components/PostsByTag'
import AllPosts from '@/components/AllPosts'

const router = createRouter({
    history: createWebHistory(),
    routes: [
        { path: '/author/:username', component: Author },
        { path: '/post/:slug', component: Post },
        { path: '/tag/:tag', component: PostsByTag },
        { path: '/', component: AllPosts },
    ]
}
)

export default router
