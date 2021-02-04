import Vue from "vue";
import App from "./App";
import router from "./router";
import { BootstrapVue, IconsPlugin } from "bootstrap-vue";
import ElementUI from "element-ui";
import axios from "axios";
import Vueaxios from "vue-axios";


//css
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";
import "element-ui/lib/theme-chalk/index.css";

Vue.config.productionTip = false;
Vue.prototype.$http = axios;

//axios
Vue.use(axios, Vueaxios);

//BoostrapVue
Vue.use(BootstrapVue);
Vue.use(IconsPlugin);

//ElementUI
Vue.use(ElementUI);

new Vue({
  el: "#app",
  router,
  components: { App },
  template: "<App/>"
});




