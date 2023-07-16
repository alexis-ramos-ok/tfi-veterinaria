import { createRouter, createWebHistory } from 'vue-router'
import HomePage from './views/HomePage.vue';
import ContactoPage from './views/ContactoPage.vue';
import AboutPage from './views/AboutPage';
import ServiciosPage from './views/ServiciosPage';
import BlogPage from './views/BlogPage';
import PetShopPage from './views/PetShopPage';
import TerminosPage from './views/TerminosPage';
import PoliticaPage from './views/PoliticaPage';
import AlimentacionPage from './views/AlimentacionPage';
import SocializacionPage from './views/SocializacionPage';
import PelajePage from './views/PelajePage';
import EjercicioPage from './views/EjercicioPage';

const routes = [
  { path: '/', component: HomePage },
  { path: '/ContactoPage', component: ContactoPage },
  { path: '/AboutPage', component: AboutPage},
  { path: '/ServiciosPage', component: ServiciosPage},
  { path: '/BlogPage', component: BlogPage},
  { path: '/PetShopPage', component: PetShopPage},
  { path: '/TerminosPage', component: TerminosPage},
  { path: '/PoliticaPage', component: PoliticaPage},
  { path: '/AlimentacionPage', component: AlimentacionPage},
  { path: '/SocializacionPage', component: SocializacionPage},
  { path: '/PelajePage', component: PelajePage},
  { path: '/EjercicioPage', component: EjercicioPage}
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router

