<template>
  <div class="carousel">
    <div class="back-image relative">

      <svg class="svg_image_top_large" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
        <!-- Circle with gradient -->
        <circle cx="50" cy="50" r="40" fill="url(#grad1)" />

        <!-- Gradient Definition -->
        <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="0%">
          <stop offset="0%" style="stop-color:#214080;stop-opacity:1" />
          <stop offset="100%" style="stop-color:#D92A27;stop-opacity:1" />
        </linearGradient>
      </svg>

      <svg class="svg_image_top_small" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
        <!-- Circle with gradient -->
        <circle cx="50" cy="50" r="40" fill="url(#grad1)" />

        <!-- Gradient Definition -->
        <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="0%">
          <stop offset="0%" style="stop-color:#214080;stop-opacity:1" />
          <stop offset="100%" style="stop-color:#D92A27;stop-opacity:1" />
        </linearGradient>
      </svg>

      <svg class="svg_image_bottom_large" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
        <!-- Circle with gradient -->
        <circle cx="50" cy="50" r="40" fill="url(#grad1)" />

        <!-- Gradient Definition -->
        <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="0%">
          <stop offset="0%" style="stop-color:#214080;stop-opacity:1" />
          <stop offset="100%" style="stop-color:#D92A27;stop-opacity:1" />
        </linearGradient>
      </svg>

      <svg class="svg_image_bottom_small" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
        <!-- Circle with gradient -->
        <circle cx="50" cy="50" r="40" fill="url(#grad1)" />

        <!-- Gradient Definition -->
        <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="0%">
          <stop offset="0%" style="stop-color:#214080;stop-opacity:1" />
          <stop offset="100%" style="stop-color:#D92A27;stop-opacity:1" />
        </linearGradient>
      </svg>

      <img :src="images[currentImageIndex]" class="home_image" alt="home page image" />

      <div class="center_this body-padding_margin">
        <div>
          <div class="carousel-content flex justify-center items-center text-center"><button @click="prevImage">
              <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1.5em" viewBox="0 0 24 24">
                <path fill="currentColor"
                  d="m8.165 11.63l6.63-6.43C15.21 4.799 16 5.042 16 5.57v12.86c0 .528-.79.771-1.205.37l-6.63-6.43a.5.5 0 0 1 0-.74">
                </path>
              </svg>
            </button>

            <div class=" flex flex-col items-center xxxs:space-y-12 md:space-y-24 xxl:space-y-32">
              <div class="homecontent">
                <h1
                  class="text-primary xxxs:text-xl xs:text-2xl sm:text-3xl md:text-4xl xxl:text-5xl font-bold text-f font-oswald pb-8">
                  {{ title[currentImageIndex] }}</h1>

                <nuxt-link :to="link[currentImageIndex]"
                  class="xxxs:text-xs xs:text-sm sm:text-base md:text-lg xxl:text-xl etcare-button px-5 py-2 md:px-10 xxl:px-14 md:py-1 xxl:py-2 items-center font-oswald">
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
            <nuxt-link class="link-home"
              :class="{ 'xxxs:border-t-2 md:border-t-4 border-primary': 0 === currentImageIndex }"
              to="/service/saving">Saving Service</nuxt-link>
            <nuxt-link class="link-home"
              :class="{ 'xxxs:border-t-2 md:border-t-4 border-primary': 1 === currentImageIndex }"
              to="/service/training">Training Service</nuxt-link>
            <nuxt-link class="link-home"
              :class="{ 'xxxs:border-t-2 md:border-t-4 border-primary': 2 === currentImageIndex }"
              to="/service/equb">Equb
              Service</nuxt-link>
            <nuxt-link class="link-home"
              :class="{ 'xxxs:border-t-2 md:border-t-4 border-primary': 3 === currentImageIndex }"
              to="/service/loan">Loan
              Service</nuxt-link>
          </div>
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
        '../_nuxt/assets/home_page/file2.png',
        '../_nuxt/assets/home_page/file1.png',
        '../_nuxt/assets/home_page/file3.png',
        '../_nuxt/assets/home_page/file4.png',
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

  .svg_image_top_large {
    position: absolute;
    top: -20%;
    left: -40%;
    z-index: 1;
    width: 450px;
    height: 450px;
  }

  .svg_image_top_small {
    position: absolute;
    top: -5%;
    left: 35%;
    z-index: 2;
    width: 150px;
    height: 150px;
  }

  .svg_image_bottom_large {
    position: absolute;
    bottom: -20%;
    right: -40%;
    z-index: 1;
    width: 450px;
    height: 450px;
  }

  .svg_image_bottom_small {
    position: absolute;
    bottom: -5%;
    right: 35%;
    z-index: 2;
    width: 150px;
    height: 150px;
  }

  img.home_image {
    position: relative;
    width: 100%;
    height: 60%;
    background-size: cover;
    background-position: center;
    transition: background-image 1s ease;
    z-index: 3;
    opacity: 0.4;
  }

}

@media (min-width: 768px) {
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

  .svg_image_top_large {
    position: absolute;
    top: -40%;
    left: -30%;
    z-index: 1;
    width: 850px;
    height: 850px;
  }

  .svg_image_top_small {
    position: absolute;
    top: -15%;
    left: 15%;
    z-index: 2;
    width: 250px;
    height: 250px;
  }

  .svg_image_bottom_large {
    position: absolute;
    bottom: -40%;
    right: -30%;
    z-index: 1;
    width: 850px;
    height: 850px;
  }

  .svg_image_bottom_small {
    position: absolute;
    bottom: -15%;
    right: 15%;
    z-index: 2;
    width: 250px;
    height: 250px;
  }


  img.home_image {
    position: relative;
    width: 100%;
    height: 100%;
    background-size: cover;
    background-position: center;
    transition: background-image 1s ease;
    z-index: 3;
    opacity: 0.4;
  }
}

@media (min-width: 1024px) {
  img.home_image {
    position: relative;
    width: 100%;
    height: 100%;
    background-size: cover;
    background-position: center;
    transition: background-image 1s ease;
    z-index: 3;
    opacity: 0.4;
  }

  .carousel button {
    color: theme('colors.primary');
    padding: 0.45rem 0.65rem;
    background-color: rgba(255, 255, 255, 0.5);
    border-radius: 5px;
    font-size: 1.25rem;
    cursor: pointer;
  }

  .carousel {
    height: 105vh;
  }

  .carousel-content {
    justify-content: space-between;
    height: 40vh;
  }

  .homecontent {
    width: 65%;
  }

  .home-links {
    justify-content: space-between;
    color: theme('colors.secondary'
      );
    font-weight: bolder;
    font-size: theme('fontSize.xl');
    width: 100%;
    padding: 0 14rem;
  }

  .link-home:hover {
    border-top: solid 2px theme('colors.primary');
  }

  .svg_image_top_large {
    position: absolute;
    top: -40%;
    left: -30%;
    z-index: 1;
    width: 850px;
    height: 850px;
  }

  .svg_image_top_small {
    position: absolute;
    top: -15%;
    left: 15%;
    z-index: 2;
    width: 250px;
    height: 250px;
  }

  .svg_image_bottom_large {
    position: absolute;
    bottom: -40%;
    right: -30%;
    z-index: 1;
    width: 850px;
    height: 850px;
  }

  .svg_image_bottom_small {
    position: absolute;
    bottom: -15%;
    right: 15%;
    z-index: 2;
    width: 250px;
    height: 250px;
  }
}

@media (min-width: 1468px) {
  img.home_image {
    position: relative;
    width: 100%;
    height: 100%;
    background-size: cover;
    background-position: center;
    transition: background-image 1s ease;
    z-index: 3;
    opacity: 0.4;
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

  .carousel-content {
    justify-content: space-between;
    height: 50vh;
  }

  .link-home:hover {
    border-top: solid 2px theme('colors.primary');
  }

  .svg_image_top_large {
    position: absolute;
    top: -40%;
    left: -30%;
    z-index: 1;
    width: 1200px;
    height: 1200px;
  }

  .svg_image_top_small {
    position: absolute;
    top: -25%;
    left: 15%;
    z-index: 2;
    width: 500px;
    height: 500px;
  }

  .svg_image_bottom_large {
    position: absolute;
    bottom: -40%;
    right: -30%;
    z-index: 1;
    width: 1200px;
    height: 1200px;
  }

  .svg_image_bottom_small {
    position: absolute;
    bottom: -25%;
    right: 15%;
    z-index: 2;
    width: 500px;
    height: 500px;
  }
}

img.home_image {
  position: relative;
  width: 100%;
  height: 100%;
  background-size: cover;
  background-position: center;
  transition: background-image 1s ease;
  z-index: 3;
  opacity: 0.4;
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
  z-index: 4;
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
