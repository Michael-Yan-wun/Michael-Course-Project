import Vue from "vue";
import Router from "vue-router";
import COURSE000 from "@/pages/F0/COURSE000";
import COURSEA000 from "@/pages/admin/A0/COURSEA000";
import Login from "@/pages/admin/login";

Vue.use(Router);

const router = new Router({
  mode: "history",
  routes: [
    {
      path: "/",
      redirect: "/course/index"
    },
    {
      path: "*",
      redicect: "/course/index"
    },
    {
      path: "/course/index",
      name: "COURSE000",
      component: COURSE000
    },
    {
      path: "/course/login",
      name: "login",
      component: Login
    },
    {
      path: "/course/admin",
      name: "COURSEA000",
      component: COURSEA000
    }
  ]
});

export default router;
