import Vue from "vue";
import Router from "vue-router";
import layout from "@/components/layout_";
import COURSE000 from "@/pages/F0/COURSE000";
import FARMA000 from "@/pages/admin/A0/FARMA000";
import FARMA100 from "@/pages/admin/A1/FARMA100";
import login from "@/pages/admin/login";

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
    // {
    //   path: "/course",
    //   name: "layout",
    //   component: layout,
    //   children: [
    //     {
    //       path: "index",
    //       name: "COURSE000",
    //       component: COURSE000
    //     }
    //   ]
    // },
    {
      path: "/admin/sales",
      name: "FARMA100",
      component: FARMA100
    },
    {
      path: "/login",
      name: "login",
      component: login
    },
    {
      path: "/admin",
      name: "FARMA000",
      component: FARMA000
    }
  ]
});

export default router;
