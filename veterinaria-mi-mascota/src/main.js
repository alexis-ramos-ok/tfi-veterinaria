import { createApp } from 'vue'
import App from './App.vue'
import NavApp from './NavApp.vue'
import FooterApp from './FooterApp.vue'
import router from './router'

window.addEventListener('DOMContentLoaded', () => {
    createApp(App).use(router).mount('#app')
    createApp(NavApp).use(router).mount('#nav')
    createApp(FooterApp).use(router).mount('#footer')
})