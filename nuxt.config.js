export default {
  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    title: 'bookstore',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
    ]
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: [

    'assets/css/tailwind.css',
    'assets/font-awesome-4.7.0/css/font-awesome.min.css',

  ],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [

   
  ],

  script: [
    {
      src: 'assets/jquery-3.6.0.min.js',
      src: 'https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js',
      src: 'assets/js/bootstrap.min.js',
      
      }
    ],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
    '@nuxtjs/tailwindcss',
    
  ],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    // https://go.nuxtjs.dev/axios
    '@nuxtjs/axios',
    // https://go.nuxtjs.dev/pwa
    '@nuxtjs/pwa',
    '@nuxtjs/auth',
    '@nuxtjs/toast',
  

  ],

  // Axios module configuration: https://go.nuxtjs.dev/config-axios
  axios: {},

  // PWA module configuration: https://go.nuxtjs.dev/pwa
  pwa: {
    manifest: {
      lang: 'en'
    }
  },

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {
  },
  loading: {
    name: 'chasing-dots',
    color: '#58fccb',
    background: 'white',
    height: '4px'
  },
    axios: {
    baseURL: 'http://127.0.0.1:8000/api/v1/'
  },
  auth: {

    strategies: {

      local: {

        endpoints: {

          login: {url: '/login/', method: 'post', propertyName: 'token'},

          user: {url: '/user/', method: 'get', propertyName: false},

          logout: false

        }
      }
    }
  },
  
  toast: {
    position: 'top-right',
    duration: 2000
  }
}
