<template>
  <div>
    <div class="card">
      <img src="img_avatar.png" alt="Avatar" style="width:100%" />
      <div class="container">
        <h4><b>John Doe</b></h4>
        <p>Architect & Engineer</p>
      </div>
    </div>
    <div class="card">
      <img src="img_avatar.png" alt="Avatar" style="width:100%" />
      <div class="container">
        <h4><b>John Doe</b></h4>
        <p>Architect & Engineer</p>
      </div>
    </div>
    <Footer id="footer" />
  </div>
</template>

<script>
import Footer from "@/components/Footer.vue";

export default {
  name: "COURSE000",
  components: { Footer },
  data() {
    return {
      images: []
    };
  }
};
</script>
<style scoped>
#footer {
  margin-top: 100px;
  padding-top: 50px;
  position: relative;
  bottom: 0;
  height: 240px;
  background-color: rgb(237, 237, 237);
  width: 100vw;
  padding:0;
  font-family: "Helvetica Neue", Arial, "Hiragino Kaku Gothic ProN",
    "Hiragino Sans", Meiryo, sans-serif;
}

.card {
  /* Add shadows to create the "card" effect */
  margin:10px;
  display: inline-block;
  height: 300px;
  width: 200px;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
  transition: 0.3s;
}

/* On mouse-over, add a deeper shadow */
.card:hover {
  box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2);
}

/* Add some padding inside the card container */
.container {
  padding: 2px 16px;
}
.container.top {
  margin-bottom: 50px;
}
</style>
