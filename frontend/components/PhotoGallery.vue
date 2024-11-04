<template>
    <div class="photo-gallary">
        <div class="grid grid-cols-1 md:grid-cols-5 gap-2 items-center justify-center">
            <img v-for="(photo, index) in photos" :key="index" :src="photo.url" alt="Photo" class="hover-photo" @click="showPhoto(index)">
        </div>
        <div v-if="selectedPhoto !== null" class="modal" @click="closeModal">
            <img :src="photos[selectedPhoto].url" alt="Selected Photo" class="modal-img">
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            photos: [
                { url: '../_nuxt/assets/gallary1.png' },
                { url: '../_nuxt/assets/gallary2.png' },
                { url: '../_nuxt/assets/gallary3.png' },
                { url: '../_nuxt/assets/gallary4.png' },
                { url: '../_nuxt/assets/gallary5.png' },
            ],
            selectedPhoto: null
        };
    },
    methods: {
        showPhoto(index) {
            this.selectedPhoto = index;
        },
        closeModal() {
            this.selectedPhoto = null;
        }
    }
};
</script>

<style>
.photo-gallary {
    padding: 3rem 4rem;
}
.hover-photo {
    cursor: pointer;
    transition: transform 0.3s ease-in-out;
}
 .hover-photo:hover {
  transform: scale(1.05);
}

.modal {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.7);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 11;
}
</style>