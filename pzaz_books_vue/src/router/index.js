import { createRouter, createWebHistory } from "vue-router";

import Book from "../views/Book.vue";
import Cart from "../views/Cart.vue";
import Category from "../views/Category.vue";
import HomeView from "../views/HomeView.vue";
import Login from "../views/Login.vue";
import Search from "../views/Search.vue";
import SignUp from "../views/SignUp.vue";

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

export default router;
