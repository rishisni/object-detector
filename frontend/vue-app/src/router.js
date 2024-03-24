import { createRouter, createWebHistory } from 'vue-router';
import HomePage from './components/HomePage.vue';
import UploadImage from './components/UploadImage.vue';

const routes = [
  {
    path: '/',
    name: 'HomePage',
    component: HomePage
  },
  {
    path: '/upload',
    name: 'UploadImage',
    component: UploadImage
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;


