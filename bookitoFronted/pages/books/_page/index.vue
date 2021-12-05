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
    

    <div class=" flex items-center justify-center mt-60 lg:hidden " >
      <div v-for="book in books_responsive" :key="book.id">
        <nuxt-link :to="`/book/${book.id}/`">
        <Book :img=" url + book.image" :author="book.author" :title="book.title"></Book>
        </nuxt-link>
      </div>
    </div>

   <div class="flex  justify-center ">
      <div class="inline-flex bottom-5 absolute " >
        <button class="bg-gray-200 hover:bg-gray-300 text-gray-800 font-bold py-2 px-4 rounded-l">
          Prev
        </button>
        <button class="bg-gray-200  lg:hidden :bg-gray-300 text-gray-800 font-bold py-2 px-4 rounded-r">
          Home
        </button>


        <nuxt-link to="/3" class="bg-gray-200 hover:bg-gray-300 text-gray-800 font-bold py-2 px-4 rounded-r">
          Next
        </nuxt-link>
      </div> 
    </div>



  </div>
</template>



<script>
import Book from "~/components/Book.vue"

export default {

  // PAGE 1 | FROM 0 / TO 4 
  //PAGE 2 | FROM 4 / TO 8
  //PAGE 3 | FROM 8 / TO 12
  //PAGE 4 | FROM 12 / TO 16
  //---------------------------
  //PAGE n ⤵️
  // TO = n x 4
  // FROM = TO - 4
  //--------------------------
  // 4 because we want to show 4 books in every page

  beforeMount(){
   // this.next_page+=1;
  },
  
  async asyncData({ $axios , params }) {
    try {
      
      page = params.page;
      to_page = page*4
      from_page = to_page-4

      let books = await $axios.$get(`books/read-books/${from_page}/${to_page}`);
      let books_responsive = await $axios.$get('books/read-books/0/1');

    
      return { books , books_responsive };
    } catch (e) {
      return { books: []  , books_responsive: []};
    }
  },

  data() {
      return {
        books : [],
        books_responsive : [],
        url : "http://127.0.0.1:8000",
        //next_page : $route.query.page,
      };
    },

    components: { Book },
    layout:'dashboard',
    middleware: 'userAuth'
}
</script>