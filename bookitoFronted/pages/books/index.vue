<template>
  <div>
       <div class="  mr-6 lg:hidden md:hidden absolute top-2 left-2">
        <span class="font-semibold text-3xl tracking-tight">
          <nuxt-link to="/">Bookito &nbsp; <i>!</i></nuxt-link>
        </span>
      </div>
      <!-- START navbar -->
      <div class="lg:flex sm:flex items-center justify-between flex-wrap bg-teal-500 p-6 hidden ">
        <div class="flex items-center flex-shrink-0  ml-7">
          <span class="font-semibold text-2xl tracking-tight">
           <nuxt-link to="/"><b>Bookito</b> </nuxt-link>
          </span>
        </div>

        <div class=" flex-grow flex items-center w-auto ">
            <div class="pt-2 relative mx-auto text-gray-600">
              <input class="border-2 border-gray-300 bg-gray-50 h-10 px-44 pr-16 rounded-lg text-sm focus:outline-none" type="search" name="search" placeholder="Search" v-model="query" v-on:keyup.enter="fetchData">
              <button type="submit" class="absolute right-0 top-0 mt-5 mr-4">
                <svg class="text-gray-600 h-4 w-4 fill-current" xmlns="http://www.w3.org/2000/svg"
                  xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" id="Capa_1" x="0px" y="0px"
                  viewBox="0 0 56.966 56.966" style="enable-background:new 0 0 56.966 56.966;" xml:space="preserve"
                  width="512px" height="512px">
                  <path
                    d="M55.146,51.887L41.588,37.786c3.486-4.144,5.396-9.358,5.396-14.786c0-12.682-10.318-23-23-23s-23,10.318-23,23  s10.318,23,23,23c4.761,0,9.298-1.436,13.177-4.162l13.661,14.208c0.571,0.593,1.339,0.92,2.162,0.92  c0.779,0,1.518-0.297,2.079-0.837C56.255,54.982,56.293,53.08,55.146,51.887z M23.984,6c9.374,0,17,7.626,17,17s-7.626,17-17,17  s-17-7.626-17-17S14.61,6,23.984,6z" />
                </svg>
              </button>
            </div>
        </div>

        <div class="flex items-center w-auto">
          <nuxt-link to="/user/login"><img src="~/assets/user.png" class="inline-block mr-12"></nuxt-link>
          <!-- icon by flaticon.com -->
          <div v-if="$auth.loggedIn">
            <p  class="mr-5">{{ $auth.user.username }}</p>
          </div>
        </div>
      </div>

      <nav class=" items-center justify-between flex-wrap w-auto text-center hidden lg:flex">

        <div class="  flex-grow flex items-center  w-auto mr-10  ">
          <div class="flex-grow ">
            <nuxt-link to="/" class=" inline-block mt-0   lg:text-base text-gray-500 ml-10   hover:text-indigo-600">
              Home
            </nuxt-link>

            <nuxt-link to="/books" class="  inline-block mt-0    lg:text-base text-gray-500 hover:text-indigo-600  ml-14 ">
              Books
            </nuxt-link>

   
          </div>
        </div>
      </nav>

    <b class="text-3xl lg:hidden ml-4 absolute top-28 border-gray-700 text-gray-700 border-l-4  "> &nbsp; All the Books</b>
    <b class="text-4xl xs:hidden ml-4 lg:absolute top-28 border-gray-700 text-gray-700 border-l-4  "> &nbsp; All the Books</b>
    <!--  icon by Icons8  -->

  
 

<div class="lg:flex xs:hidden">
  <div class="flex-1 ">
        <div class="lg:flex  mt-32    "> 
        <div class="flex-1 ml-16  " v-for="book in books" :key="book.id">
          <nuxt-link :to="`/book/${book.id}`">
            <Book :img="url +book.image" :author="book.author" :title="book.title" :book_id="book.id"></Book>
            
          </nuxt-link>
          
          <div class="mt-3  ">
            <button class="text-sm text-red-500 flex-1" @click="deleteBook(book.id)"> DELETE </button>
            <nuxt-link :to="`/books/edit/${book.id}`" class="text-sm text-yellow-500 ml-3   flex-1 mr-44"> EDIT </nuxt-link>
          </div>
        </div>
    </div>
  </div>

  <div class="lg:flex-1">
    <nuxt-link to="/books/new">
    <img src="https://img.icons8.com/ios/50/000000/plus.png" class="float-right  mr-10 mt-20 lg:mt-56" />
    </nuxt-link>
  </div>
</div>
    
<!-- START | Book in responsive mood -->


<div class="xs:flex lg:hidden md:hidden ">
  <div class="flex-1">
        <div class=" flex items-center justify-center mt-52 ml-5  " >
      <div v-for="book in pageOfItemsR" :key="book.id">
        <nuxt-link :to="`/book/${book.id}`">
        <Book :img=" url + book.image" :author="book.author" :title="book.title"></Book>
        </nuxt-link>
        <div class="mt-3 flex ">
            <button class="text-sm text-red-500 flex-1" @click="deleteBook(book.id)"> DELETE </button>
            <nuxt-link :to="`/books/edit/${book.id}`" class="text-sm text-yellow-500 ml-3  flex-1 mr-44"> EDIT </nuxt-link>
        </div>
      </div>
    </div>
  </div>

  <div class="flex-1 mt-52 ">
    <nuxt-link to="/books/new">
    <img src="https://img.icons8.com/ios/50/000000/plus.png" class="float-right  mr-10 mt-20 lg:mt-56" />
    </nuxt-link>
  </div>

</div>

<!-- END | Book in responsive mood -->

<!-- START | Book in responsive mood md -->

<div class="md:flex lg:hidden xs:hidden ">
  <div class="flex-1">
    <div class=" flex items-center justify-center mt-52 ml-20  " >
      <div v-for="book in pageOfItemsRR" :key="book.id" class="ml-20">
        <nuxt-link :to="`/book/${book.id}`">
        <Book :img=" url + book.image" :author="book.author" :title="book.title"></Book>
        </nuxt-link>
        <div class="mt-3 flex ">
            <button class="text-sm text-red-500 flex-1" @click="deleteBook(book.id)"> DELETE </button>
            <nuxt-link :to="`/books/edit/${book.id}`" class="text-sm text-yellow-500 ml-3  flex-1 mr-44"> EDIT </nuxt-link>
        </div>
      </div>
    </div>
  </div>

  <div class="flex-1 mt-52 ">
    <nuxt-link to="/books/new">
    <img src="https://img.icons8.com/ios/50/000000/plus.png" class="float-right  mr-10 mt-20 lg:mt-56" />
    </nuxt-link>
  </div>

</div>


<!-- END | Book in responsive mood md -->

   <div class="flex  justify-center ">
      <div class="lg:inline-flex xs:hidden bottom-5 absolute" >
        <jw-pagination   :items="books"  @changePage="onChangePage" :pageSize="4" :labels="customLabels" ></jw-pagination>
      </div> 
      <div class="inline-flex bottom-5  absolute  lg:hidden md:hidden " >
        <jw-pagination   :items="books" @changePage="onChangePageR" :pageSize="1" :labels="customLabels"  ></jw-pagination>
      </div>
      <div class="md:inline-flex bottom-5  absolute  lg:hidden xs:hidden " >
        <jw-pagination   :items="books" @changePage="onChangePageRR" :pageSize="2" :labels="customLabels"  ></jw-pagination>
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
        pageOfItemsRR : [],
        paginate:['all_books'],
        customLabels,
        img: null,
        url:this.$Django.url,
        query:""
      };
    },
    methods : {

     async fetchData(){
      try{
        if(this.query !== ''|| this.query !== null) {
            let searchedBooks =  await this.$axios.$get(`books/books/?name=${this.query}`);
            this.books = searchedBooks;
        }
       }
       catch (e) {
          this.$toast.error(e);
        }
      
     },
      
      onChangePage(pageOfItems) {
            // update page of items
          this.pageOfItems = pageOfItems;
      },
      

      onChangePageR(pageOfItemsR){
        this.pageOfItemsR = pageOfItemsR;
      },

      onChangePageRR(pageOfItemsRR){
        this.pageOfItemsRR = pageOfItemsRR;
      },

      async deleteBook(book_id) {
        try {
          await this.$axios.$delete(`books/delete-book/${book_id}`);
          let newBooks = await this.$axios.$get("books/read-books"); // get new list of books
          this.books = newBooks; // update list of books
        } catch (e) {
          this.$toast.error(e);
        }
      }

    },
    

    components: { Book },
    middleware: 'userAuth'
}
</script>