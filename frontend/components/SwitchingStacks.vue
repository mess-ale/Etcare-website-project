<template>
  <div class="home-page">
    <div class="carousel" :style="{ transform: `translateX(-${currentMovieIndex * 100}%)` }">
      <div v-for="(movie, index) in movies" :key="movie.id" class="carousel-slide"
        :style="{ backgroundImage: `url(${movie.featured_image})` }">
        <div class="movie-info-container">
          <h1 class="movie-title" @click="openmovie(movie.id)">{{ movie.title }}</h1>
          <div class="movie-meta">
            <span class="rating">Genre:</span>
            <span class="quality">{{ movie.genre.name }}</span>
            <span class="rating">Director:</span>
            <span class="quality">{{ movie.director.name }}</span>
          </div>
          <p class="movie-description">
            {{ movie.description }}
          </p>
          <button class="get-tickets-button" @click="openModal(movie.id)">GET TICKETS</button>
          <div class="pagination">
            <span v-for="(dot, dotIndex) in movies" :key="dotIndex" class="dot"
              :class="{ active: currentMovieIndex === dotIndex }" @click="setMovieIndex(dotIndex)">
            </span>
          </div>
        </div>

        <div class="movie-release">
          <span class="text">In theater</span>
          <h3 class="time text-4xl font-bold">
            {{ movie.release_date }}
          </h3>
          <img src="../static/images/underline-heading-entire.png" alt="line" />
        </div>
      </div>
    </div>
    <TicketModal v-if="isModalOpen" :id="selectedMovieId" @close="closeModal" />
  </div>
</template>

<script>
import { ref, onMounted, onUnmounted } from 'vue';
import { useNuxtApp } from '#app';
import TicketModal from './TicketModal.vue';

export default {
  components: {
    TicketModal
  },
  setup() {
    const movies = ref([]);
    const currentMovieIndex = ref(0);
    const { $axios } = useNuxtApp();
    let interval = null;

    const fetchMovies = async () => {
      try {
        const response = await $axios.get('/api/Released-movies/');
        movies.value = response.data;
      } catch (error) {
        console.error('Error fetching movies:', error);
      }
    };

    const changeMovie = () => {
      currentMovieIndex.value = (currentMovieIndex.value + 1) % movies.value.length;
    };

    const setMovieIndex = (index) => {
      currentMovieIndex.value = index;
    };

    onMounted(async () => {
      await fetchMovies();
      interval = setInterval(changeMovie, 50000);
    });

    onUnmounted(() => {
      clearInterval(interval);
    });

    return {
      movies,
      currentMovieIndex,
      setMovieIndex
    };
  },
  data() {
    return {
      isModalOpen: false,
      selectedMovieId: null
    };
  },
  methods: {
    openModal(movieId) {
      this.selectedMovieId = movieId;
      this.isModalOpen = true;
    },
    closeModal() {
      this.isModalOpen = false;
      this.selectedMovieId = null;
    },
    openmovie(movieId) {
      this.$router.push(`/movie/${movieId}`);
    },
  }
};
</script>

<style scoped>
.movie-release {
  margin-top: -20rem;
}

.home-page {
  height: 120vh;
  overflow: hidden;
  position: relative;
}

.carousel {
  display: flex;
  transition: transform 1.5s ease-in-out;
  height: 100%;
}

.carousel-slide {
  min-width: 100%;
  position: relative;
  display: flex;
  height: 120vh;
  align-items: center;
  background-size: cover;
  background-position: center;
  justify-content: space-around;
}

.carousel-slide::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 250px;
  background: linear-gradient(to bottom, rgba(0, 0, 0, 0.5), transparent);
  pointer-events: none;
}

.movie-info-container {
  padding: 20px;
  color: #fff;
  max-width: 650px;
}

.movie-title {
  font-size: 4.5rem;
  font-weight: 1000;
  margin-bottom: 10px;
  cursor: pointer;
}

.movie-title:hover {
  color: theme('colors.primary');
}

.movie-meta {
  display: flex;
  gap: 10px;
  font-size: 3rem;
  margin-bottom: 15px;
}

.movie-meta span {
  display: inline-block;
  background-color: #444;
  padding: 5px 10px;
  border-radius: 5px;
}

.rating,
.quality,
.caption {
  font-size: 1rem;
}

.release-date {
  font-size: 1rem;
  color: #ccc;
}

.movie-description {
  font-size: 1rem;
  line-height: 1.5;
  margin-bottom: 20px;
}

.pagination {
  display: flex;
  gap: 5px;
  margin-top: 15px;
}

.dot {
  width: 10px;
  height: 10px;
  margin: 5px;
  background-color: #ffffff;
  border-radius: 50%;
  display: inline-block;
  cursor: pointer;
}

.dot.active {
  background-color: theme('colors.primary');
}
</style>
