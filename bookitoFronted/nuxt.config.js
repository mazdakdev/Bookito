export default {

    mode: 'universal',
    /*
     ** Nuxt target
     ** See https://nuxtjs.org/api/configuration-target
     */
    target: 'server',
    // Global page headers: https://go.nuxtjs.dev/config-head
    head: {
        title: 'Bookito',
        meta: [
            { charset: 'utf-8' },
            { name: 'viewport', content: 'width=device-width, initial-scale=1' },
            { hid: 'description', name: 'description', content: '' }
        ],
        link: [
            { rel: 'icon', type: 'image/x-icon', href: '/icon.ico' }
        ]
    },

    // Global CSS: https://go.nuxtjs.dev/config-css
    css: [
        'assets/css/tailwind.css',
    ],

    // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
    plugins: [
        '~/plugins/vueTyper.client.js',
        '~/plugins/pagination.js',
        '~/plugins/pdf.client.js',
        '~/plugins/django.js',
    ],

    script: [{


    }],

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
    axios: {
        baseURL: 'http://127.0.0.1:8000/api/v1/'
    },

    auth: {
        strategies: {
            local: {
                endpoints: {
                    login: { url: 'login/', method: 'post', propertyName: 'token' },
                    user: {
                        url: 'user/',
                        method: 'GET',
                        propertyName: false
                    },
                    logout: { url: 'auth/logout/', method: 'post' },
                },
                tokenType: "Token",
                tokenName: "Authorization"
            },
            redirect: {
                login: '/user/login',
                home: '/books'

            }
        }
    },

    // PWA module configuration: https://go.nuxtjs.dev/pwa
    pwa: {
        manifest: {
            lang: 'en'
        }
    },

    // Build Configuration: https://go.nuxtjs.dev/config-build
    build: {},
    loading: {
        name: 'chasing-dots',
        color: '#58fccb',
        background: 'white',
        height: '4px'
    },

    toast: {
        position: 'top-right',
        duration: 2000
    },

}