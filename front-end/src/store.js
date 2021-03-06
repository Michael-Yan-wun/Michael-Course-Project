import Vue from "vue";
import Vuex from "vuex";
import { getAPI } from "./service";

Vue.use(Vuex);
export default new Vuex.Store({
  state: {
    accessToken: null,
    refreshToken: null,
    APIData: "",
    username: ""
  },
  mutations: {
    updatedStorage(state, { access, refresh }) {
      state.accessToken = access;
      state.refreshToken = refresh;
    },
    updatedUsername(state, { username }) {
      state.username = username;
    }
  },
  actions: {
    userLogin(context, usercredentials) {
      return new Promise((resolve, reject) => {
        getAPI
          .post("/api/auth/get_token/", {
            username: usercredentials.username,
            password: usercredentials.password
          })
          .then(response => {
            console.log(response);
            context.commit("updatedStorage", {
              access: response.data.access,
              refresh: response.data.refresh
            });
            context.commit("updatedUsername", {
              username: usercredentials.username
            });
            resolve();
          })
          .catch(err => {
            reject(err);
          });
      });
    }
  }
});
