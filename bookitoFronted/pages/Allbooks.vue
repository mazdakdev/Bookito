<template>
  <div>
    <b class="text-3xl lg:hidden ml-4 absolute top-28 border-gray-700 text-gray-700 border-l-4  "> &nbsp; All the Books</b>
    <b class="text-4xl xs:hidden ml-4 lg:absolute top-28 border-gray-700 text-gray-700 border-l-4  "> &nbsp; All the Books</b>
    <!--  icon by Icons8  -->
    <nuxt-link to="/newBook">
    <img src="https://img.icons8.com/ios/50/000000/plus.png" class="float-right  mr-10 mt-20" />
    </nuxt-link>

    <div class="lg:flex  mt-44 ml-28   xs:hidden ">  
        <div class="flex-1 " v-for="book in books" :key="book.id">
          <nuxt-link :to="`/book/${book.id}/`">
          <Book :img=" url + book.image" :author="book.author" :title="book.title"></Book>
          </nuxt-link>
        </div>
    </div>
    

    <div class=" flex items-center justify-center mt-52 lg:hidden " >
      <div v-for="book in books" :key="book.id">
        <nuxt-link :to="`/book/${book.id}/`">
        <Book :img=" url + book.image" :author="book.author" :title="book.title"></Book>
        </nuxt-link>
      </div>
    </div>

   <div class="flex  justify-center ">
      <div class="inline-flex bottom-5 absolute ml-14" >
        <button class="bg-gray-200 hover:bg-gray-300 text-gray-800 font-bold py-2 px-4 rounded-l">
          Prev
        </button>
        <button class="bg-gray-200  lg:hidden :bg-gray-300 text-gray-800 font-bold py-2 px-4 rounded-r">
          Home
        </button>


        <button class="bg-gray-200 hover:bg-gray-300 text-gray-800 font-bold py-2 px-4 rounded-r">
          Next
        </button>
      </div> 
    </div>



  </div>
</template>



<script>
import Book from "../components/Book.vue"


export default {
  async asyncData({ $axios }) {
    try {
      let books = await $axios.$get('books/read-books' ,{
        params: { 
          _limit:4
        }
      });
      return { books };
    } catch (e) {
      return { books: [] };
    }
  },

  data() {
      return {
        books : [],
        url : "http://127.0.0.1:8000"
      };
    },
    methods: {
        scrollX(e) {
          this.$refs['scroll_container'].scrollLeft += e.deltaY;
        }
    },
    components: { Book },
    layout:'dashboard',
    middleware: 'auth'
}
</script>