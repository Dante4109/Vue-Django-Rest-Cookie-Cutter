import { createRouter, createWebHistory } from 'vue-router'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('../pages/Home.vue')
    },
    {
    path: "/product/:productPath",
    name: "product",
    props: true,
    component: () => import("../pages/GenericPage.vue")
    },
    {
    path: "/fake",
    name: "fake",
    component: () => import("../pages/FakePage.vue")
    },
    {
    path: "/emit",
    name: "emitTest",
    component: () => import("../components/EmitTest.vue")
    },
    {
    path: "/emitTS",
    name: "emitTestTS",
    component: () => import("../components/EmitTestTS.vue")
    },
    {
    path: "/login",
    name: "login",
    component: () => import("../components/registration/LoginForm.vue")
    }
  ]
})

export default router