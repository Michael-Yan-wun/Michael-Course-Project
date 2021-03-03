import Vue from "vue";
import Router from "vue-router";
import COURSE000 from "@/pages/F0/COURSE000";
import COURSE100 from "@/pages/F0/COURSE100";
import COURSEA000 from "@/pages/admin/A0/COURSEA000";
import Login from "@/pages/admin/login";
import Logout from "@/pages/admin/logout";

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
      path: "/course/index/user",
      name: "COURSE100",
      component: COURSE100
    },
    {
      path: "/course/login",
      name: "login",
      component: Login
    },
    {
      path: "/course/logout",
      name: "logout",
      component: Logout
    },
    {
      path: "/course/admin",
      name: "COURSEA000",
      component: COURSEA000,
      beforeEnter: (to, from, next) => {
        if(from.name ==null||from.name!='login'){
          next({'name':'login'})
        }else{
          next();
        }
      }
    }
  ]
});

export default router;
