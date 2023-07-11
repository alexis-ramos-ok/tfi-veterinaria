import { createRouter, createWebHistory } from 'vue-router'
import HomePage from './views/HomePage.vue'
import ContactoPage from './views/ContactoPage.vue';
import AboutPage from './views/AboutPage';
import ServiciosPage from './views/ServiciosPage';
import BlogPage from './views/BlogPage';
import PetShopPage from './views/PetShopPage';

const routes = [
  { path: '/', component: HomePage },
  { path: '/ContactoPage', component: ContactoPage },
  { path: '/AboutPage', component: AboutPage},
  { path: '/ServiciosPage', component: ServiciosPage},
  { path: '/BlogPage', component: BlogPage},
  { path: '/PetShopPage', component: PetShopPage}
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router

