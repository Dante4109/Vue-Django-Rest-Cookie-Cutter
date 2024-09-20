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
      path: '/password_reset/:resetToken',
      name: 'passwordreset',
      props: true,
      component: () => import("../components/password_reset/Password_Reset.vue"),
    },
    {
      path: '/email_verification/:verificationToken',
      name: 'emailverification',
      props: true,
      component: () => import("../components/email_verification/Email_Verification.vue"),
    },
    {
      path: '/ProfileSetup/',
      name: 'profilesetup',
      props: true,
      component: () => import("../components/profile_setup/Profile_Setup.vue"),
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
  ]
})

export default router