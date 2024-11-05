<template>
    <div>
        <ServiceCard text="service" imgservice="../_nuxt/assets/service/service.png" />

        <div class="grid grid-cols-1 md:grid-cols-2 gap-0 service-body">
            <div :class="{ 'image-container-left': isVisible }" class="box-image" ref="myElement">
                <img src="../../assets/service/saving.png" alt="Description" class="transform-image" />
            </div>
            <div :class="{ 'image-container-right': isVisible }" class="items-center flex">
                <div class="space-y-8 p-8">
                    <h1 class="text-secondary font-oswald text-5xl font-bold">Saving</h1>
                    <p class="text-primary font-robot text-xl text-justify">We understand the importance of saving for
                        the future, which is why we offer convenient and flexible savings options to help our members
                        build financial security. Whether it's short-term goals or long-term planning, our savings
                        accounts provide a safe and reliable way to grow your money.</p>
                    <div class="flex">
                        <nuxt-link class="service-button items-center text-xl font-oswald flex space-x-4 font-robot"
                            to="/about">
                            <svg xmlns="http://www.w3.org/2000/svg" width="2em" height="2em" viewBox="0 0 24 24">
                                <path fill="currentColor"
                                    d="m7.45 17.45l-1.4-1.4L9.075 13H2v-2h7.075L6.05 7.95l1.4-1.4L12.9 12zM13 17v-2h9v2zm0-8V7h9v2zm3 4v-2h6v2z">
                                </path>
                            </svg>
                            <span>Learn More</span>
                        </nuxt-link>
                    </div>
                </div>
            </div>
            <div class="items-center flex">
                <div class="space-y-8 p-8">
                    <h1 class="text-secondary font-oswald text-5xl font-bold">Training</h1>
                    <p class="text-primary font-robot text-xl text-justify">We understand the importance of saving for
                        the future, which is why we offer convenient and flexible savings options to help our members
                        build financial security. Whether it's short-term goals or long-term planning, our savings
                        accounts provide a safe and reliable way to grow your money.</p>
                    <div class="flex">
                        <nuxt-link class="service-button items-center text-xl font-oswald flex space-x-4 font-robot"
                            to="/about">
                            <svg xmlns="http://www.w3.org/2000/svg" width="2em" height="2em" viewBox="0 0 24 24">
                                <path fill="currentColor"
                                    d="m7.45 17.45l-1.4-1.4L9.075 13H2v-2h7.075L6.05 7.95l1.4-1.4L12.9 12zM13 17v-2h9v2zm0-8V7h9v2zm3 4v-2h6v2z">
                                </path>
                            </svg>
                            <span>Learn More</span>
                        </nuxt-link>
                    </div>
                </div>
            </div>
            <div class="saving-img">
                <img src="../../assets/service/training1.JPG" alt="saving" />
            </div>
            <div class="saving-img">
                <img src="../../assets/service/equb.png" alt="saving" />
            </div>
            <div class="items-center flex">
                <div class="space-y-8 p-8">
                    <h1 class="text-secondary font-oswald text-5xl font-bold">Equb</h1>
                    <p class="text-primary font-robot text-xl text-justify">We understand the importance of saving for
                        the future, which is why we offer convenient and flexible savings options to help our members
                        build financial security. Whether it's short-term goals or long-term planning, our savings
                        accounts provide a safe and reliable way to grow your money.</p>
                    <div class="flex">
                        <nuxt-link class="service-button items-center text-xl font-oswald flex space-x-4 font-robot"
                            to="/about">
                            <svg xmlns="http://www.w3.org/2000/svg" width="2em" height="2em" viewBox="0 0 24 24">
                                <path fill="currentColor"
                                    d="m7.45 17.45l-1.4-1.4L9.075 13H2v-2h7.075L6.05 7.95l1.4-1.4L12.9 12zM13 17v-2h9v2zm0-8V7h9v2zm3 4v-2h6v2z">
                                </path>
                            </svg>
                            <span>Learn More</span>
                        </nuxt-link>
                    </div>
                </div>
            </div>
            <div class="items-center flex">
                <div class="space-y-8 p-8">
                    <h1 class="text-secondary font-oswald text-5xl font-bold">loan</h1>
                    <p class="text-primary font-robot text-xl text-justify">We understand the importance of saving for
                        the future, which is why we offer convenient and flexible savings options to help our members
                        build financial security. Whether it's short-term goals or long-term planning, our savings
                        accounts provide a safe and reliable way to grow your money.</p>
                    <div class="flex">
                        <nuxt-link class="service-button items-center text-xl font-oswald flex space-x-4 font-robot"
                            to="/about">
                            <svg xmlns="http://www.w3.org/2000/svg" width="2em" height="2em" viewBox="0 0 24 24">
                                <path fill="currentColor"
                                    d="m7.45 17.45l-1.4-1.4L9.075 13H2v-2h7.075L6.05 7.95l1.4-1.4L12.9 12zM13 17v-2h9v2zm0-8V7h9v2zm3 4v-2h6v2z">
                                </path>
                            </svg>
                            <span>Learn More</span>
                        </nuxt-link>
                    </div>
                </div>
            </div>
            <div class="saving-img">
                <img src="../../assets/service/loan.png" alt="saving" />
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            isVisible: false,
        };
    },
    mounted() {
        window.addEventListener('scroll', this.handleScroll);
        this.handleScroll(); // Initial check
    },
    beforeDestroy() {
        window.removeEventListener('scroll', this.handleScroll);
    },
    methods: {
        handleScroll() {
            const imageContainer = this.$refs.myElement;
            const rect = imageContainer.getBoundingClientRect();
            this.isVisible = rect.top <= 299;
        }
    }
};
</script>

<style>

.image-container-left {
  transform: translateX(-100%); /* Starts off-screen */
  transition: transform 0.5s ease-in-out; /* Smooth transition */
}

.box-image {
  transform: translateX(0);
    overflow-x: hidden;
}

.cover-service-img {
    background-image: url('../assets/2.jpg');
    height: 33rem;
    display: flex;
    align-items: center;
    background-size: cover;
    background-position: center;
}

.service-body {
    padding: 4rem;
}

.service-body img {
    width: 100%;
    height: 100%;
}

.service-button {
    background-color: theme('colors.primary');
    color: theme('colors.background');
    padding: 0.5rem 2rem;
    border-radius: 0.25rem;
}
</style>