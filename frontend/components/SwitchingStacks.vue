<template>
  <div class="carousel">
    <div class="back-image" :style="{ backgroundImage: `url(${images[currentImageIndex]})` }">
      <div class="carousel-content flex justify-center items-center text-center">
        <button @click="prevImage">❮</button>
        <div class=" flex flex-col items-center space-y-32">
          <div class="homecontent">
            <h1 class="text-primary text-4xl text-f font-oswald pb-8">{{ title[currentImageIndex] }}</h1>

            <nuxt-link :to="link[currentImageIndex]"
              class="xs:text-xs md:text-xl etcare-button px-5 py-2 md:px-14 md:py-2 items-center font-oswald">
              Read More
            </nuxt-link>
          </div>
        </div>
        <button @click="nextImage">❯</button>
      </div>
      <div class="home-links flex text-xl font-oswald">
        <nuxt-link class="link-home" :class="{ 'border-t-4 border-primary': 0 === currentImageIndex }" to="/service/saving">Saving Service</nuxt-link>
        <nuxt-link class="link-home" :class="{ 'border-t-4 border-primary': 1 === currentImageIndex }" to="/service/training">Training Service</nuxt-link>
        <nuxt-link class="link-home" :class="{ 'border-t-4 border-primary': 2 === currentImageIndex }" to="/service/equb">Equb Service</nuxt-link>
        <nuxt-link class="link-home" :class="{ 'border-t-4 border-primary': 3 === currentImageIndex }" to="/service/loan">Loan Service</nuxt-link>
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
        '../_nuxt/assets/homepage3.png',
        '../_nuxt/assets/homepage1.png',
        '../_nuxt/assets/homepage3.png',
      ],
      title: [
        "Secure Your Financial Future with Our Trustworthy Saving Solutions – Building Wealth with Confidence.",
        "Empower Your Future with Skill-Building Training Programs Designed to Elevate Your Financial Independence.",
        "Join a Community of Collective Savings with Equb – Build Wealth Together for a Brighter Future!",
        "Achieve Your Ambitions with Our Flexible Loan Options – Empowering You to Take the Next Step!",
      ],
      link: [
        "/service/saving",
        "/service/training",
        "/service/equb",
        "/service/loan",
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
  position: relative;
  height: 105vh;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

.carousel-content {
  justify-content: space-between;
  height: 90vh;
  padding: 0 6rem;
}

.back-image {
  width: 100%;
  height: 100%;
  background-size: cover;
  background-position: center;
  transition: background-image 1s ease;
}

.carousel button {
  color: theme('colors.primary');
  padding: 0.25rem 0.8rem;
  background-color: rgb(255, 255, 255, 0.5);
  border-radius: 6px;
  font-size: 2rem;
  cursor: pointer;
}

.carousel button:hover {
  background: theme('colors.white');
}

.homecontent {
  width: 65%;
}
.home-links {
  justify-content: space-between;
  padding: 0 8rem;
  color: theme(
    'colors.secondary'
  );
  font-weight: bolder;
}.link-home {
  transition: border-top 0.2s ease-in-out;
}
.link-home:hover {
  border-top: solid 4px theme('colors.primary');
}
</style>
