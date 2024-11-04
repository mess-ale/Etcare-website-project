<template>
    <div class="cover">
        <div class="text">
            <h1 class="text-secondary font-oswald font-bold text-5xl">{{ text }}</h1>
        </div>
    </div>
    <img src="../assets/Group 40.png" class="pt-4 pb-12" alt="line header" />
</template>

<script>
export default {
    props: {
        text: {
            type: String,
            required: true
        }
    }
};
</script>

<style scoped>
.cover {
    background-image: url('../assets/2.jpg');
    height: 23rem;
    display: flex;
    align-items: center;
    background-size: cover;
    background-position: center;
}

.text {
    width: 100%;
    display: flex;
    text-align: center;
    justify-content: center;
}
</style>