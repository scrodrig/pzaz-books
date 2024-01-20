import { createRouter, createWebHistory } from "vue-router";

import Book from "../views/Book.vue";
import Cart from "../views/Cart.vue";
import Category from "../views/Category.vue";
import Checkout from "@/views/Checkout.vue";
import HomeView from "../views/HomeView.vue";
import Login from "../views/Login.vue";
import MyAccount from "@/views/MyAccount.vue";
import Search from "../views/Search.vue";
import SignUp from "../views/SignUp.vue";
import Success from "../views/Success.vue";
import store from "../store";

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/about",
    name: "about",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/AboutView.vue"),
  },
  {
    path: "/search",
    name: "search",
    component: Search,
  },
  {
    path: "/cart",
    name: "cart",
    component: Cart,
  },
  {
    path: "/sign-up",
    name: "signup",
    component: SignUp,
  },
  {
    path: "/my-account",
    name: "myaccount",
    component: MyAccount,
    meta: {
      requireLogin: true,
    },
  },
  {
    path: "/cart/success",
    name: "success",
    component: Success,
  },
  {
    path: '/cart/checkout',
    name: 'checkout',
    component: Checkout,
    meta: {
      requireLogin: true
    }
  },
  {
    path: "/log-in",
    name: "login",
    component: Login,
  },
  {
    path: "/:category_slug/:book_slug",
    name: "book",
    component: Book,
  },
  {
    path: "/:category_slug",
    name: "category",
    component: Category,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
    next({ name: 'login', query: { to: to.path } });
  } else {
    next()
  }
});

export default router;
