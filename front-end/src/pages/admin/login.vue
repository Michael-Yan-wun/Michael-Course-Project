<template>
  <body>
    <div class="loginBox">
      <div class="login-container">
        <div class="login-container-img"></div>
        <div class="login-container-content">
          <p v-if="incorrectAuth">錯誤帳號密碼</p>
          <form v-on:submit.prevent="login" action="" class="login-form">
            <h1>Login</h1>
            <p class="field">
              <label>Users name or Email</label>
              <input type="text" name="username" placeholder="user" v-model="username" />
            </p>
            <p class="field">
              <label>Password</label>
              <input type="password" name="password" placeholder="password" v-model="password" />
              <a href="">forget password?</a>
            </p>
            <!-- <router-link :to="{name:'COURSEA000'}"> -->
            <button type="submit" class="submitBtn">Sign in</button>
            <!-- </router-link> -->
          </form>
        </div>
      </div>
    </div>
  </body>
</template>

<script>
export default {
  name: "login",
  data() {
    return {
      incorrectAuth: false,
      username: "",
      password: ""
    };
  },
  methods: {
    go() {
      this.$router.push({ name: "COURSEA000" });
    },
    login() {
      this.$store
        .dispatch("userLogin", {
          username: this.username,
          password: this.password
        })
        .then(() => {
          this.$router.push({ name: "COURSEA000" });
        })
        .catch(err => {
          console.log(err);
          this.incorrectAuth = true;
        });
    }
  }
};
</script>

<style scoped>
body {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.login-container {
  width: 640px;
  height: 400px;
  display: flex;
}

.field-text,
.login-container-content .login-form .parting-line,
.login-container-content .login-form .field > label,
.login-container-content .login-form .field > a {
  font-size: 5px;
  color: #a7a7a7;
}

.login-container-content {
  flex: 50%;
  background: white;
  text-align: center;
  display: flex;
  align-items: center;
  border-top-right-radius: 15px;
  border-bottom-right-radius: 15px;
}
.login-container-content .login-form {
  padding: 2px;
  width: 100%;
}
.login-container-content .login-form .buttonX {
  position: absolute;
  right: 2%;
  top: 2%;
  border: none;
  background: transparent;
  outline: none;
}
.login-container-content .login-form h1 {
  letter-spacing: 1rem;
  color: transparent;
  -webkit-background-clip: text;
  background-clip: text;
  background-image: linear-gradient(45deg, #6767ed 45%, #4daef2 75%);
  font-family: "Aguafina Script", Arial, Helvetica, sans-serif;
}
.login-container-content .login-form .field {
  margin: 10px auto;
  padding: 5px;
  width: 75%;
  height: 25%;
  display: grid;
  grid-row-gap: 0.2rem;
}
.login-container-content .login-form .field > label,
.login-container-content .login-form .field > input {
  text-align: left;
}
.login-container-content .login-form .field > input {
  outline: none;
  border-top: none;
  border-left: none;
  border-right: none;
  border-bottom: 1px solid grey;
}
.login-container-content .login-form .field > input:focus {
  border-bottom-color: #1838e7;
}
.login-container-content .login-form .field > a {
  text-align: right;
  text-decoration: none;
}
.login-container-content .login-form > .submitBtn {
  width: 75%;
  height: 2rem;
  position: relative;
  background: linear-gradient(135deg, #3ce77b 0%, #008eff 70%);
  color: white;
  outline: none;
  border-style: none;
  border-radius: 15px;
  transition: 0.3s ease-in-out;
}
.login-container-content .login-form > .submitBtn:hover {
  filter: hue-rotate(45deg);
}
.login-container-content .login-form .parting-line {
  position: relative;
  margin-top: 1rem;
  margin-bottom: 1rem;
  margin-left: 2.5rem;
  margin-right: 2.5rem;
  overflow: hidden;
}
.login-container-content .login-form .parting-line::before,
.login-container-content .login-form .parting-line::after {
  content: "";
  position: absolute;
  top: 50%;
  width: 45%;
  display: block;
  text-align: center;
  border-top: 1px solid;
}
.login-container-content .login-form .parting-line::before {
  right: 55%;
}
.login-container-content .login-form .parting-line::after {
  right: 0%;
}

.login-container-img {
  flex: 50%;
  font-family: "Franklin Gothic Medium", "Arial Narrow", Arial, sans-serif;
  background: url("../../../src/assets/img/logo.png");
  /* background: url("https://images-production.bookshop.org/spree/images/attachments/3926574/original/9781798052105.jpg?1574260520  "); */
  background-size: cover;
  background-repeat: no-repeat;
  border-top-left-radius: 15px;
  border-bottom-left-radius: 15px;
}
.login-container-img > h1 {
  display: grid;
  text-align: center;
  color: black;
  margin-top: 50%;
  padding-left: 20px;
  padding-right: 20px;
  letter-spacing: 2px;
  margin-bottom: 10px;
}
.login-container-img > h1 > span {
  text-align: center;
  font-size: 16px;
}

.loginBox {
  box-shadow: 0 0 15px 5px;
  border-radius: 15px;
}
</style>
