<template>
  <div class="blog-card bg-white shadow-md rounded-lg overflow-hidden">
    <div class="bg-gray-100 p-6">
      <h2 class="text-xl font-bold mb-2 text-secondary">{{ title }}</h2>
      <p class="text-primary text-sm">{{ summary }}</p>
    </div>
    <div class="bg-gray-200 p-6">
      <img :src="image" alt="Blog Image" class="w-full h-auto mb-4">
      <p class="text-primary">{{ content }}</p>
    </div>
    <div class="bg-gray-100 p-6 flex justify-between items-center">
      <div>
        <p class="text-primary text-sm">By {{ author }}</p>
        <p class="text-primary text-sm">{{ publishedAt }}</p>
      </div>
      <div>
        <nuxt-link class="etcare-button px-4 py-2" to="/readMore" >
          Read More
        </nuxt-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    title: String,
    summary: String,
    image: String,
    content: String,
    author: String,
    publishedAt: String,
  },
};
</script>

<style>
.blog-card {
}
</style>