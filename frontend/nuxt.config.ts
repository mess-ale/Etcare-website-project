// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  modules: ["@nuxtjs/tailwindcss",'@nuxtjs/google-fonts'],
  compatibilityDate: '2024-04-03',
  googleFonts: {
    families: {
      Oswald: [400, 500, 600, 700], // specify the font weights you need
      Roboto: [400, 500, 700]       // add Roboto with desired weights
    },
    display: 'swap'
  }
})
