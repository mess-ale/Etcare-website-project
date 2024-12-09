import axios from 'axios';

export default defineNuxtPlugin(() => {
  const instance = axios.create({
    baseURL: process.env.NUXT_PUBLIC_API_BASE_URL || 'http://127.0.0.1:8000/api/', // Default API base URL
  });

  return {
    provide: {
      axios: instance,
    },
  };
});
