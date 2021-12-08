<template>
    <vue-pdf-app style="height: 100vh;" :pdf="url + book.pdf"></vue-pdf-app>
</template>


<script>

export default {
    async asyncData({ $axios , params }) {
        try {
        let book = await $axios.$get(`books/get-book/${params.id}`);

        
        return { book };
        } catch (e) {
        return  {book: [] };
        }
    },
    data(){
        return {
            book:[],
            url: this.$Django.url
      
        }
    }
}
</script>

