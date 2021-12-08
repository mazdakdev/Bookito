import Vue from 'vue'

export default ({ app }, inject) => {
    inject('Django', Vue.observable({ url: 'http://127.0.0.1:8000' }))
}