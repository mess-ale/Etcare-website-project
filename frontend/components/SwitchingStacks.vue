<template>
  <div class="carousel">
    <div class="back-image" :style="{ backgroundImage: `url(${images[currentImageIndex]})` }">
      <div class="center_this body-padding_margin">
        <div class="carousel-content flex justify-center items-center text-center">
          <button @click="prevImage">
            <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1.5em" viewBox="0 0 24 24">
              <path fill="currentColor"
                d="m8.165 11.63l6.63-6.43C15.21 4.799 16 5.042 16 5.57v12.86c0 .528-.79.771-1.205.37l-6.63-6.43a.5.5 0 0 1 0-.74">
              </path>
            </svg>
          </button>
          <div class=" flex flex-col items-center xxxs:space-y-12 md:space-y-32">
            <div class="homecontent">
              <h1
                class="text-primary xxxs:text-xl xs:text-2xl sm:text-3xl md:text-4xl xl:text-5xl text-f font-oswald pb-8">
                {{ title[currentImageIndex] }}</h1>

              <nuxt-link :to="link[currentImageIndex]"
                class="xxxs:text-xs xs:text-sm sm:text-base md:text-xl etcare-button px-5 py-2 md:px-14 md:py-2 items-center font-oswald">
                Read More
              </nuxt-link>
            </div>
          </div>
          <button @click="nextImage"> <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1.5em"
              viewBox="0 0 24 24">
              <path fill="currentColor"
                d="M15.835 11.63L9.205 5.2C8.79 4.799 8 5.042 8 5.57v12.86c0 .528.79.771 1.205.37l6.63-6.43a.5.5 0 0 0 0-.74">
              </path>
            </svg>
          </button>
        </div>

        <div class="home-links flex font-oswald">
          <nuxt-link class="link-home" :class="{ 'xxxs:border-t-2 md:border-t-4 border-primary': 0 === currentImageIndex }"
            to="/service/saving">Saving Service</nuxt-link>
          <nuxt-link class="link-home" :class="{ 'xxxs:border-t-2 md:border-t-4 border-primary': 1 === currentImageIndex }"
            to="/service/training">Training Service</nuxt-link>
          <nuxt-link class="link-home" :class="{ 'xxxs:border-t-2 md:border-t-4 border-primary': 2 === currentImageIndex }"
            to="/service/equb">Equb Service</nuxt-link>
          <nuxt-link class="link-home" :class="{ 'xxxs:border-t-2 md:border-t-4 border-primary': 3 === currentImageIndex }"
            to="/service/loan">Loan Service</nuxt-link>
        </div>
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
@media (min-width: 200px) {
  .carousel button {
    color: theme('colors.primary');
    padding: 0.2rem 0.7rem;
    background-color: rgba(255, 255, 255, 0.5);
    border-radius: 6px;
    font-size: 1rem;
    cursor: pointer;
  }

  .carousel {
    height: 100vh;
  }

  .carousel-content {
    justify-content: space-between;
    margin: 4rem 0 14rem 0;
  }

  .homecontent {
    width: 100%;
  }

  .home-links {
    justify-content: space-between;
    /* padding: 0 1.5rem; */
    color: theme('colors.secondary'
      );
    font-weight: bolder;
    font-size: theme('fontSize.xs');
    width: 100%;
  }

  .link-home:hover {
    border-top: solid 2px theme('colors.primary');
  }
}

@media (min-width: 668px) {
  .carousel button {
    color: theme('colors.primary');
    padding: 0.5rem 0.9rem;
    background-color: rgba(255, 255, 255, 0.5);
    border-radius: 6px;
    font-size: 1.2rem;
    cursor: pointer;
  }

  .carousel {
    height: 100vh;
  }

  .carousel-content {
    justify-content: space-between;
    margin: 4rem 0 14rem 0;
  }

  .homecontent {
    width: 80%;
  }

  .home-links {
    justify-content: space-between;
    /* padding: 0 2.5rem; */
    color: theme('colors.secondary'
      );
    font-weight: bolder;
    font-size: theme('fontSize.lg');
    width: 100%;
  }

  .link-home:hover {
    border-top: solid 3px theme('colors.primary');
  }
}

@media (min-width: 1268px) {
  .carousel button {
    color: theme('colors.primary');
    padding: 0.7rem 0.9rem;
    background-color: rgba(255, 255, 255, 0.5);
    border-radius: 6px;
    font-size: 1.5rem;
    cursor: pointer;
  }

  .carousel {
    height: 105vh;
  }

  .carousel-content {
    justify-content: space-between;
    height: 90vh;
  }

  .homecontent {
    width: 65%;
  }

  .home-links {
    justify-content: space-between;
    color: theme('colors.secondary'
      );
    font-weight: bolder;
    font-size: theme('fontSize.2xl');
    width: 100%;
    padding: 0 14rem;
  }

  .link-home:hover {
    border-top: solid 2px theme('colors.primary');
  }
}

.carousel {
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

.back-image {
  width: 100%;
  height: 100%;
  background-size: cover;
  background-position: center;
  transition: background-image 1s ease;
}

.link-home {
  transition: border-top 0.2s ease-in-out;
}

.carousel button:hover {
  background: theme('colors.white');
}

.center_this {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100%;
}
</style>
