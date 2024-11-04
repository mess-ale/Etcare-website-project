<template>
  <div class="bg-white shadow-md rounded-lg overflow-hidden">
    <div class="bg-gray-100 p-6">
      <h2 class="text-xl font-bold mb-2">{{ title }}</h2>
      <p class="text-gray-700 text-sm">{{ summary }}</p>
    </div>
    <div class="bg-gray-200 p-6">
      <img :src="image" alt="Blog Image" class="w-full h-auto mb-4">
      <p class="text-gray-700">{{ content }}</p>
    </div>
    <div class="bg-gray-100 p-6 flex justify-between items-center">
      <div>
        <p class="text-gray-700 text-sm">By {{ author }}</p>
        <p class="text-gray-700 text-sm">{{ publishedAt }}</p>
      </div>
      <div>
        <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
          Read More
        </button>
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