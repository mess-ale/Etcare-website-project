<template>
    <div>
        <header :style="{ backgroundColor: headerBackgroundColor }" class="fixed top-0 left-0 right-0 z-10 w-full flex items-center justify-between text-primary
            xs:h-12 sm:h-16 md:h-20 xl:h-24 xs:pl-8 sm:pl-10 md:pl-12 xl:pl-16 xs:pr-8 sm:pr-10 md:pr-12 xl:pr-14">
            <div>
                <img class="xs:h-[65%] xs:w-[65%] md:h-[100%] md:w-[100%]" src="../assets/Etcare_logo1-removebg.png"
                    alt="etcare logo" />
            </div>

            <div class="hidden md:inline xs:text-xs md:text-base">
                <div class="space-x-7 flex item-center">
                    <nuxt-link to="/" class="links">HOME</nuxt-link>
                    <div class="flex items-center" @mouseenter="showDropdown = true" @mouseleave="showDropdown = false">
                        <nuxt-link to="/service" class="links">SERVICE</nuxt-link>
                        <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24"
                            class="ml-1">
                            <path fill="currentColor" d="m5 8l7 8l7-8z"></path>
                        </svg>
                        <div v-if="showDropdown" class="dropdown">
                            <div class="dropdown-item space-x-3">
                                <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24">
                                    <path fill="currentColor"
                                        d="M5.925 21q-.575 0-1.112-.4t-.713-.975q-.625-2.1-1.025-3.637t-.638-2.7t-.337-2.063T2 9.5q0-2.3 1.6-3.9T7.5 4h5q.675-.9 1.713-1.45T16.5 2q.625 0 1.063.438T18 3.5q0 .15-.038.3t-.087.275q-.1.275-.187.55t-.138.6L19.825 7.5H21q.425 0 .713.288T22 8.5v5.25q0 .325-.187.575t-.513.375l-2.125.7l-1.25 4.175q-.2.65-.725 1.038T16 21h-2q-.825 0-1.412-.587T12 19h-2q0 .825-.587 1.413T8 21zM16 11q.425 0 .713-.288T17 10t-.288-.712T16 9t-.712.288T15 10t.288.713T16 11m-4-2q.425 0 .713-.288T13 8t-.288-.712T12 7H9q-.425 0-.712.288T8 8t.288.713T9 9z">
                                    </path>
                                </svg>
                                <nuxt-link to="/service/saving">Saving</nuxt-link>
                            </div>
                            <div class="dropdown-item  space-x-3">
                                <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24">
                                    <path fill="currentColor"
                                        d="M5.189 18.1q-.814-1.085-1.251-2.37Q3.5 14.444 3.5 13q0-3.558 2.471-6.029T12 4.5h1.412l-2.12-2.12l.689-.688L15.288 5l-3.307 3.308l-.714-.714L13.362 5.5H12q-3.111 0-5.306 2.194T4.5 13q0 1.237.374 2.352t1.047 2.035zm6.08.092q-.096-.748-.455-1.32q-.358-.572-.756-1.107q-.399-.536-.709-1.103t-.31-1.278q0-1.219.87-2.09q.872-.871 2.091-.871t2.09.871t.872 2.09q0 .712-.311 1.269q-.31.556-.709 1.102q-.398.545-.756 1.117q-.359.572-.455 1.32zm.039 2.5v-1.115h1.384v1.115zm7.504-2.592l-.733-.713q.673-.92 1.047-2.035T19.5 13q0-1.611-.62-3.014t-1.724-2.43l.713-.714q1.239 1.174 1.935 2.744T20.5 13q0 1.444-.437 2.73q-.438 1.285-1.251 2.37">
                                    </path>
                                </svg><nuxt-link to="/service/training">training</nuxt-link>
                            </div>
                            <div class="dropdown-item  space-x-3">
                                <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 48 48">
                                    <path fill="none" stroke="currentColor" stroke-linecap="round"
                                        stroke-linejoin="round"
                                        d="M18.595 41.825H5.5V35.23l8.285-3.352c-1.472 4.825 3.464 7.685 6.315 6.051z">
                                    </path>
                                    <path fill="none" stroke="currentColor" stroke-linecap="round"
                                        stroke-linejoin="round"
                                        d="M20.1 37.93c0-.374 1.239-2.087 1.698-2.087c.565 0 2.202-.884 2.202-1.978V7.35c-.367-1.502-2.602-1.695-2.956.196l-1.483 10.065c-.26 1.634-.99 1.634-1.272 3.267c-.389 3.18-.76 8.729-4.504 11.001m15.62 9.946H42.5V35.23l-8.285-3.352c1.472 4.825-3.464 7.685-6.315 6.051z">
                                    </path>
                                    <path fill="none" stroke="currentColor" stroke-linecap="round"
                                        stroke-linejoin="round"
                                        d="M27.9 37.93c0-.374-1.239-2.087-1.698-2.087c-.565 0-2.202-.884-2.202-1.978V7.35c.367-1.502 2.602-1.695 2.956.196l1.484 10.065c.259 1.634.989 1.634 1.271 3.267c.389 3.18.76 8.729 4.504 11.001M12.498 14.475l-3.631.148m6.285-2.523l.547-3.593m-2.019 4.64l-1.886-2.105m22.884 3.433l3.63.148M32.024 12.1l-.547-3.593m2.019 4.64l1.885-2.105">
                                    </path>
                                </svg><nuxt-link to="/service/equb">equb</nuxt-link>
                            </div>
                            <div class="dropdown-item  space-x-3">
                                <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 32 32">
                                    <path fill="currentColor"
                                        d="m15 22l-1.41 1.41L16.17 26H4V8H2v18c0 1.103.897 2 2 2h12.17l-2.58 2.59L15 32l5-5z">
                                    </path>
                                    <circle cx="11" cy="16" r="1" fill="currentColor"></circle>
                                    <path fill="currentColor"
                                        d="M24 20H8c-1.103 0-2-.897-2-2v-4c0-1.103.897-2 2-2h16c1.103 0 2 .897 2 2v4c0 1.103-.897 2-2 2M8 14v4h16v-4z">
                                    </path>
                                    <path fill="currentColor"
                                        d="M28 4H15.83l2.58-2.59L17 0l-5 5l5 5l1.41-1.41L15.83 6H28v18h2V6c0-1.102-.897-2-2-2">
                                    </path>
                                </svg><nuxt-link to="/service/loan">loan</nuxt-link>
                            </div>
                        </div>
                    </div>
                    <nuxt-link to="/about" class="links">ABOUT</nuxt-link>
                    <nuxt-link to="/blog" class="links">BLOG</nuxt-link>
                    <nuxt-link to="/contact" class="links">CONTACT</nuxt-link>
                </div>
            </div>

            <div class="md:hidden">
                <svg xmlns="http://www.w3.org/2000/svg" width="2.5em" height="2.5em" viewBox="0 0 24 24">
                    <path fill="currentColor"
                        d="M4 18q-.425 0-.712-.288T3 17t.288-.712T4 16h16q.425 0 .713.288T21 17t-.288.713T20 18zm0-5q-.425 0-.712-.288T3 12t.288-.712T4 11h16q.425 0 .713.288T21 12t-.288.713T20 13zm0-5q-.425 0-.712-.288T3 7t.288-.712T4 6h16q.425 0 .713.288T21 7t-.288.713T20 8z">
                    </path>
                </svg>

            </div>
            <div>
                <nuxt-link to="/login"
                    class="xs:text-xs md:text-base flex items-center etcare-button xs:pt-1 xs:pb-1 xs:pl-5 xs:pr-5 md:pt-2 md:pb-2 md:pl-8 md:pr-8 space-x-10">
                    SIGN IN
                    <svg xmlns="http://www.w3.org/2000/svg" width="1.5em" height="1.5em" viewBox="0 0 24 24">
                        <path fill="currentColor"
                            d="M12 21v-2h7V5h-7V3h7q.825 0 1.413.588T21 5v14q0 .825-.587 1.413T19 21zm-2-4l-1.375-1.45l2.55-2.55H3v-2h8.175l-2.55-2.55L10 7l5 5z">
                        </path>
                    </svg>
                </nuxt-link>
            </div>
        </header>

        <div class="bg-background text-white h-100">
            <slot />
        </div>

        <footer class="bg-primary text-white">
            <div class="footerpadding">
                <div class="grid grid-cols-1 md:grid-cols-4 gap-4 pt-10 pb-10">

                    <div class="space-y-3 ">
                        <div class="items-center flex space-x-5">
                            <svg xmlns="http://www.w3.org/2000/svg" width="2em" height="2em" viewBox="0 0 24 24">
                                <path fill="currentColor"
                                    d="M12 20.556q-.235 0-.47-.077t-.432-.25q-1.067-.981-2.164-2.185q-1.096-1.203-1.99-2.493t-1.468-2.633t-.572-2.622q0-3.173 2.066-5.234Q9.037 3 12 3t5.03 2.062q2.066 2.061 2.066 5.234q0 1.279-.572 2.613q-.572 1.333-1.458 2.632q-.885 1.3-1.981 2.494T12.92 20.21q-.191.173-.434.26q-.244.086-.487.086m.004-8.825q.667 0 1.14-.476q.472-.475.472-1.143t-.476-1.14t-1.143-.472t-1.14.476t-.472 1.143t.475 1.14t1.144.472">
                                </path>
                            </svg>
                            <h4>Addis Ababa, Ethiopia</h4>
                        </div>

                        <div class="items-center flex space-x-5">
                            <svg xmlns="http://www.w3.org/2000/svg" width="2em" height="2em" viewBox="0 0 24 24">
                                <g fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"
                                    stroke-width="2">
                                    <path stroke-dasharray="64" stroke-dashoffset="64"
                                        d="M4 5h16c0.55 0 1 0.45 1 1v12c0 0.55 -0.45 1 -1 1h-16c-0.55 0 -1 -0.45 -1 -1v-12c0 -0.55 0.45 -1 1 -1Z">
                                        <animate fill="freeze" attributeName="stroke-dashoffset" dur="0.6s"
                                            values="64;0"></animate>
                                    </path>
                                    <path stroke-dasharray="24" stroke-dashoffset="24" d="M3 6.5l9 5.5l9 -5.5">
                                        <animate fill="freeze" attributeName="stroke-dashoffset" begin="0.6s" dur="0.2s"
                                            values="24;0"></animate>
                                    </path>
                                </g>
                            </svg>

                            <h4>Etcare@gmail.com</h4>
                        </div>

                        <div class="items-center flex space-x-5">
                            <svg xmlns="http://www.w3.org/2000/svg" width="2em" height="2em" viewBox="0 0 24 24">
                                <path fill="currentColor"
                                    d="M19.95 21q-3.125 0-6.175-1.362t-5.55-3.863t-3.862-5.55T3 4.05q0-.45.3-.75t.75-.3H8.1q.35 0 .625.238t.325.562l.65 3.5q.05.4-.025.675T9.4 8.45L6.975 10.9q.5.925 1.187 1.787t1.513 1.663q.775.775 1.625 1.438T13.1 17l2.35-2.35q.225-.225.588-.337t.712-.063l3.45.7q.35.1.575.363T21 15.9v4.05q0 .45-.3.75t-.75.3">
                                </path>
                            </svg>

                            <h4>+251-91-755-0560</h4>
                        </div>

                    </div>


                    <div>
                        <h4 class="mb-4 font-bold">COMPANY</h4>
                        <ul class="space-y-2">
                            <li>
                                <nuxt-link to="/about" class="links">About</nuxt-link>
                            </li>
                            <li>
                                <nuxt-link to="/service" class="links">Service</nuxt-link>
                            </li>
                            <li>
                                <nuxt-link to="/blog" class="links">Blog</nuxt-link>
                            </li>
                            <li>
                                <nuxt-link to="/service/saving" class="links">Saving</nuxt-link>
                            </li>
                            <li>
                                <nuxt-link to="/service/equb" class="links">Equb</nuxt-link>
                            </li>
                            <li>
                                <nuxt-link to="/service/loan" class="links">Loan</nuxt-link>
                            </li>
                        </ul>
                    </div>


                    <div class="space-y-3">
                        <h4 class="mb-4 font-bold">LATEST NEWS</h4>
                        <div>
                            <div class="flex space-x-3">
                                <img src="../assets/dall1.png" />
                                <div>
                                    <h6 class="font-light text-sm">Empowering Members Through Financial Education
                                    </h6>
                                    <h4 class="font-bold">21th Joly 2017</h4>
                                </div>

                            </div>
                        </div>
                        <div>
                            <div class="flex space-x-3">
                                <img src="../assets/dall2.png" />
                                <div>
                                    <h6 class="font-light text-sm">Empowering Members Through Financial Education
                                    </h6>
                                    <h4 class="font-bold">21th Joly 2017</h4>
                                </div>

                            </div>
                        </div>
                        <div>
                            <div class="flex space-x-3">
                                <img src="../assets/dall3.png" />
                                <div>
                                    <h6 class="font-light text-sm">Empowering Members Through Financial Education
                                    </h6>
                                    <h4 class="font-bold">21th Joly 2017</h4>
                                </div>

                            </div>
                        </div>
                    </div>

                    <div>
                        <h5 class="text-justify mb-4 font-bold ">Contact your nearest Etcare SACCO branch to receive
                            your
                            account username and password.</h5>
                        <div class="flex justify-center pt-5">
                            <nuxt-link to="/contact"
                                class="etcare-button xs:pt-1 xs:pb-1 xs:pl-5 xs:pr-5 md:pt-2 md:pb-2 md:pl-8 md:pr-8 footer-button flex items-center space-x-4">
                                <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 20 20">
                                    <path fill="currentColor"
                                        d="M17 11v3l-3-3H8a2 2 0 0 1-2-2V2c0-1.1.9-2 2-2h10a2 2 0 0 1 2 2v7a2 2 0 0 1-2 2zm-3 2v2a2 2 0 0 1-2 2H6l-3 3v-3H2a2 2 0 0 1-2-2V8c0-1.1.9-2 2-2h2v3a4 4 0 0 0 4 4z">
                                    </path>
                                </svg>
                                <h1> contact us</h1>
                            </nuxt-link>
                        </div>

                        <div class="flex justify-center">
                            <div class="flex space-x-3 pt-5">
                                <nuxt-link to="https://web.facebook.com/etcaresacco" target="_blank"><svg
                                        class="socialM" xmlns="http://www.w3.org/2000/svg" width="2em" height="2em"
                                        viewBox="0 0 24 24">
                                        <path fill="currentColor"
                                            d="M22 12c0-5.52-4.48-10-10-10S2 6.48 2 12c0 4.84 3.44 8.87 8 9.8V15H8v-3h2V9.5C10 7.57 11.57 6 13.5 6H16v3h-2c-.55 0-1 .45-1 1v2h3v3h-3v6.95c5.05-.5 9-4.76 9-9.95">
                                        </path>
                                    </svg></nuxt-link>

                                <svg class="socialM" xmlns="http://www.w3.org/2000/svg" width="2em" height="2em"
                                    viewBox="0 0 24 24">
                                    <path fill="currentColor"
                                        d="M12.244 4c.534.003 1.87.016 3.29.073l.504.022c1.429.067 2.857.183 3.566.38c.945.266 1.687 1.04 1.938 2.022c.4 1.56.45 4.602.456 5.339l.001.152v.174c-.007.737-.057 3.78-.457 5.339c-.254.985-.997 1.76-1.938 2.022c-.709.197-2.137.313-3.566.38l-.504.023c-1.42.056-2.756.07-3.29.072l-.235.001h-.255c-1.13-.007-5.856-.058-7.36-.476c-.944-.266-1.687-1.04-1.938-2.022c-.4-1.56-.45-4.602-.456-5.339v-.326c.006-.737.056-3.78.456-5.339c.254-.985.997-1.76 1.939-2.021c1.503-.419 6.23-.47 7.36-.476zM9.999 8.5v7l6-3.5z">
                                    </path>
                                </svg>
                                <nuxt-link to="https://vm.tiktok.com/ZMhQxWYC7/" target="_blank"> <svg class="socialM"
                                        xmlns="http://www.w3.org/2000/svg" width="2em" height="2em" viewBox="0 0 24 24">
                                        <path
                                            d="M19.59 6.69a4.83 4.83 0 0 1-3.77-4.25V2h-3.45v13.67a2.89 2.89 0 0 1-5.2 1.74a2.89 2.89 0 0 1 2.31-4.64a2.93 2.93 0 0 1 .88.13V9.4a6.84 6.84 0 0 0-1-.05A6.33 6.33 0 0 0 5 20.1a6.34 6.34 0 0 0 10.86-4.43v-7a8.16 8.16 0 0 0 4.77 1.52v-3.4a4.85 4.85 0 0 1-1-.1z"
                                            fill="currentColor"></path>
                                    </svg></nuxt-link>

                                <nuxt-link to="https://t.me/etcaresacco" target="_blank"><svg class="socialM"
                                        xmlns="http://www.w3.org/2000/svg" width="2em" height="2em" viewBox="0 0 24 24">
                                        <path
                                            d="M9.78 18.65l.28-4.23l7.68-6.92c.34-.31-.07-.46-.52-.19L7.74 13.3L3.64 12c-.88-.25-.89-.86.2-1.3l15.97-6.16c.73-.33 1.43.18 1.15 1.3l-2.72 12.81c-.19.91-.74 1.13-1.5.71L12.6 16.3l-1.99 1.93c-.23.23-.42.42-.83.42z"
                                            fill="currentColor"></path>
                                    </svg></nuxt-link>

                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="textcopy w-full flex items-center justify-between text-primary">
                <div>
                    <img src="../assets/Etcare_logo1-removebg.png" alt="etcare logo" />
                </div>
                <div>
                    <nuxt-link to="/Privacy" class="links">Privacy Policy</nuxt-link>
                    <h4 class="font-bold">© 2024 by EtCare Sacco. All Rights Reserved.</h4>
                </div>
            </div>
        </footer>
    </div>
</template>

<script>
export default {
    data() {
        return {
            headerBackgroundColor: 'transparent',
            showDropdown: false
        };
    },
    mounted() {
        window.addEventListener('scroll', this.handleScroll);
    },
    destroyed() {
        window.removeEventListener('scroll', this.handleScroll);
    },
    methods: {
        handleScroll() {
            if (window.scrollY > 100) {
                this.headerBackgroundColor = '#fff';
            } else {
                this.headerBackgroundColor = 'rgba(255, 255, 255, 0.55)';
            }
        }
    }
};
</script>

<style>
.links:hover {
    color: theme('colors.secondary');
}

.button {
    cursor: pointer;
}

.search {
    cursor: pointer;
}



.etcare-button {
    background-color: theme('colors.primary');
    color: theme('colors.white');
    border-radius: 10px 10px 10px 0;
    border: none;
    cursor: pointer;
    transition: background-color 0.3s;
}

.etcare-button:hover {
    background-color: theme('colors.background');
    color: theme('colors.secondary');
}

.footer-button {
    font-size: 0.8rem;
    border-radius: 1px;
    background-color: theme('colors.secondary');
    color: theme('colors.background');

}

.inputclass {
    border-width: 2px;
    width: 25rem;
    border: none;
    padding: 0.5rem 1rem;
    outline: none;
    background-color: transparent;
}

.searchbox {
    border: 2px solid theme('colors.primary');
}

.searchbox:focus-within {
    background-color: theme('colors.secondary');
}

.textcopy {
    background-color: theme('colors.background');
    height: 90px;
    padding: 0 4rem;
}

.footerlink {
    justify-content: space-between;
    padding: 1.75rem 0;
    border-bottom: 2px solid #181818;
}

.footerpadding {
    padding: 0 4rem;
    height: 400px;
}

.socialM {
    transition: transform .3s ease-in-out;
}

.socialM:hover {
    transform: translateY(-15%);
    color: theme('colors.secondary');
}

.socialM::after {
    transition: transform .3s ease-in-out;
}


.bg-background {
    height: 70rem;
}



.dropdown {
    position: absolute;
    background-color: theme('colors.white');
    top: 65%;
    z-index: 10;
    width: 25%;
}

.dropdown-item {
    display: flex;
    padding: 10px;
    align-items: center;
    border-bottom: solid 1px theme('colors.secondary');
    text-decoration: none;
    color: theme('colors.primary');
}

.dropdown-item:hover {
    color: theme('colors.secondary');
}
</style>
