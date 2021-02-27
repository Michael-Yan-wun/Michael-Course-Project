<template>
  <swiper class="swiper" :options="swiperOption">
    <div
      class="parallax-bg"
      slot="parallax-bg"
      data-swiper-parallax="-23%"
    ></div>
    <swiper-slide>
      <div class="title" data-swiper-parallax="-100">Michael Studio</div>
      <div class="subtitle" data-swiper-parallax="-240">工作室</div>
      <div class="text" data-swiper-parallax="-360">
        <p>
          此工作室的宗旨為『分享』，
        </p>
      </div>
    </swiper-slide>
    <swiper-slide>
      <div class="title" data-swiper-parallax="-100">Slide 2</div>
      <div class="subtitle" data-swiper-parallax="-240">Subtitle</div>
      <div class="text" data-swiper-parallax="-360">
        <p>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam
          dictum mattis velit, sit amet faucibus felis iaculis nec. Nulla
          laoreet justo vitae porttitor porttitor. Suspendisse in sem justo.
          Integer laoreet magna nec elit suscipit, ac laoreet nibh euismod.
          Aliquam hendrerit lorem at elit facilisis rutrum. Ut at ullamcorper
          velit. Nulla ligula nisi, imperdiet ut lacinia nec, tincidunt ut
          libero. Aenean feugiat non eros quis feugiat.
        </p>
      </div>
    </swiper-slide>
    <swiper-slide>
      <div class="title" data-swiper-parallax="-100">Slide 3</div>
      <div class="subtitle" data-swiper-parallax="-240">Subtitle</div>
      <div class="text" data-swiper-parallax="-360">
        <p>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam
          dictum mattis velit, sit amet faucibus felis iaculis nec. Nulla
          laoreet justo vitae porttitor porttitor. Suspendisse in sem justo.
          Integer laoreet magna nec elit suscipit, ac laoreet nibh euismod.
          Aliquam hendrerit lorem at elit facilisis rutrum. Ut at ullamcorper
          velit. Nulla ligula nisi, imperdiet ut lacinia nec, tincidunt ut
          libero. Aenean feugiat non eros quis feugiat.
        </p>
      </div>
    </swiper-slide>
    <div
      class="swiper-pagination swiper-pagination-white"
      slot="pagination"
    ></div>
    <div
      class="swiper-button-prev swiper-button-white"
      slot="button-prev"
    ></div>
    <div
      class="swiper-button-next swiper-button-white"
      slot="button-next"
    ></div>
  </swiper>
</template>

<script>
import { swiper, swiperSlide } from "vue-awesome-swiper";
import "swiper/swiper-bundle.css";
export default {
  name: "swiper-example-parallax",
  title: "Parallax",
  components: {
    swiper,
    swiperSlide
  },
  data() {
    return {
      swiperOption: {
        speed: 600,
        parallax: true,
        pagination: {
          el: ".swiper-pagination",
          clickable: true
        },
        navigation: {
          nextEl: ".swiper-button-next",
          prevEl: ".swiper-button-prev"
        }
      }
    };
  }
};
</script>

<style scoped>
.parallax-bg {
  position: absolute;
  left: 0;
  top: 0;
  width: 130%;
  height: 100%;
  background-size: cover;
  background-position: left;
  background-image: url("../assets/img/doit.jpg");
}
.swiper {
  width: 100%;
  height: 625px;
}
.swiper-slide {
  display: flex;
  flex-direction: column;
  justify-content: center;
  box-sizing: border-box;
  padding: 0 80px;
  background-color: transparent;
}
.title {
  font-weight: bold;
}
.text {
  max-width: 430px;
  line-height: 1.32;
  margin-bottom: 280px;
}
</style>
