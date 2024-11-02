<template>
  <div class="carousel">
    <div class="carousel-content" :style="{ backgroundImage: `url(${images[currentImageIndex]})` }">
      <img :src="images[currentImageIndex]" :alt="`Image ${currentImageIndex + 1}`" class="carousel-image" />
      <div class="carousel-controls" >
        <button @click="prevImage">❮</button>
        <button @click="nextImage">❯</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      images: [
        '../_nuxt/assets/homepage1.png',
        '../_nuxt/assets/dall2.png',
        '../_nuxt/assets/dall3.png',
      ],
      currentImageIndex: 0,
    };
  },
  methods: {
    nextImage() {
      this.currentImageIndex = (this.currentImageIndex + 1) % this.images.length;
    },
    prevImage() {
      this.currentImageIndex =
        (this.currentImageIndex - 1 + this.images.length) % this.images.length;
    },
  },
  mounted() {
    this.interval = setInterval(this.nextImage, 7000);
  },
  beforeDestroy() {
    clearInterval(this.interval);
  },
};
</script>

<style scoped>
.carousel {
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
}

.carousel-content {
  position: relative;
}

.carousel-image {
  width: 100vw;
  height: 105vh;
  transition: opacity 0.5s ease;
}

.carousel-controls {
  position: absolute;
  padding: 0 4rem;
  top: 50%;
  width: 100%;
  display: flex;
  justify-content: space-between;
  transform: translateY(-50%);
}

.carousel-controls button {
  background-color: theme('colors.background');
  color: theme('colors.primary');
  font-weight: bolder;
  border: none;
  padding: 10px 15px;
  border-radius: 5px;
  cursor: pointer;
}

.carousel-controls button:hover {
   background-color: rgb(240, 245, 255,0.5);
}
</style>
