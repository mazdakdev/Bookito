<template>
  <div>
    <b class="text-3xl lg:hidden ml-4 absolute top-28 border-gray-700 text-gray-700 border-l-4  "> &nbsp; All the Books</b>
    <b class="text-4xl xs:hidden ml-4 lg:absolute top-28 border-gray-700 text-gray-700 border-l-4  "> &nbsp; All the Books</b>
    <!--  icon by Icons8  -->
    <nuxt-link to="/books/new">
    <img src="https://img.icons8.com/ios/50/000000/plus.png" class="float-right  mr-10 mt-20" />
    </nuxt-link>
 

    <div class="lg:flex  mt-44 ml-28   xs:hidden ">  


  
        <div class="flex-1 " v-for="book in pageOfItems" :key="book.id">
          <nuxt-link :to="`/book/${book.id}`">
            <Book :img="url +book.image" :author="book.author" :title="book.title" :book_id="book.id"></Book>
      
          </nuxt-link>
          <div class="mt-3 ">
            <button class="text-sm text-red-500 flex-1" @click="deleteBook(book.id)"> DELETE </button>
            <nuxt-link :to="`/books/edit/${book.id}`" class="text-sm text-yellow-500 ml-5 flex-1 mr-44"> EDIT </nuxt-link>
          </div>
        </div>
    </div>
    

    <div class=" flex items-center justify-center mt-60 lg:hidden " >
      <div v-for="book in pageOfItemsR" :key="book.id">
        <nuxt-link :to="`/book/${book.id}`">
        <Book :img=" url + book.image" :author="book.author" :title="book.title"></Book>
        </nuxt-link>
      </div>
    </div>

   <div class="flex  justify-center ">
      <div class="lg:inline-flex xs:hidden bottom-5 absolute" >
        <jw-pagination   :items="books"  @changePage="onChangePage" :pageSize="4" :labels="customLabels" ></jw-pagination>
      </div> 
      <div class="inline-flex bottom-5  absolute  lg:hidden " >
        <jw-pagination   :items="books" @changePage="onChangePageR" :pageSize="1" :labels="customLabels"  ></jw-pagination>
      </div>
    </div>

  </div>
</template>



<script>
import Book from "~/components/Book.vue"

const customLabels = {

    previous: '<',
    next: '>',
    last:'>>',
    first:'<<',
};

export default {


  async asyncData({ $axios }) {
    try {
      let books = await $axios.$get('books/read-books/');

    
      return { books  };
    } catch (e) {
      return  {books: [] };
    }
  },

  data() {
      return {
        books : [],
        pageOfItems : [],
        pageOfItemsR : [],
        paginate:['all_books'],
        customLabels,
        img: null,
        url:this.$Django.url
      };
    },
    methods : {

      
      onChangePage(pageOfItems) {
            // update page of items
            this.pageOfItems = pageOfItems;
      },

      onChangePageR(pageOfItemsR){
        this.pageOfItemsR = pageOfItemsR;
      },

      async deleteBook(book_id) {
        try {
          await this.$axios.$delete(`/books/delete-book/${book_id}`);
          let newBooks = await this.$axios.$get("/books/read-books"); // get new list of books
          this.books = newBooks; // update list of books
        } catch (e) {
          console.log(e);
        }
      }

    },
    

    components: { Book },
    layout:'dashboard',
    middleware: 'userAuth'
}
</script>