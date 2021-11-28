<template>
  <div>
    <b class="text-3xl lg:hidden ml-4 absolute top-28 border-gray-700 text-gray-700 border-l-4  "> &nbsp; All the Books</b>
    <b class="text-4xl xs:hidden ml-4 lg:absolute top-28 border-gray-700 text-gray-700 border-l-4  "> &nbsp; All the Books</b>
    <div class="lg:flex  mt-44 ml-28   xs:hidden ">

      <div class="flex-1 ">
        <nuxt-link to="Singlebook">
          <Book img="https://images-na.ssl-images-amazon.com/images/I/51pnouuPO5L.jpg" author="Steve Krug" title="Dont make me think"></Book>
        </nuxt-link>
      </div>

      <div class="flex-1 ">
        <Book img="https://images-na.ssl-images-amazon.com/images/I/61hBuTEWKGS._AC_SX368_.jpg" author="International" title="Guiness World Record"></Book>
      </div>

      <div class="flex-1 ">
        <Book img="https://images-na.ssl-images-amazon.com/images/I/41Xi50NeleL._AC_SX368_.jpg" author="Rachel Campos-Dulify"  title="All Amircans Christmas" ></Book>
      </div>

      <div class="flex-1 ">
        <Book img="https://images-na.ssl-images-amazon.com/images/I/41Q7dRE4StL._AC_SX368_.jpg" author="MICHAEL CON" title="The Dark Hours"></Book>
      </div>

    </div>

    <div class=" flex items-center justify-center mt-52 lg:hidden " >

      <Book img="https://images-na.ssl-images-amazon.com/images/I/51pnouuPO5L.jpg" class="" author="Steve Krug" title="Dont make me think"></Book>

    </div>


    <div class="flex  justify-center ">
      <div class="inline-flex bottom-5 absolute" >
        <button class="bg-gray-200 hover:bg-gray-300 text-gray-800 font-bold py-2 px-4 rounded-l">
          Prev
        </button>
        <button class="bg-gray-200  lg:hidden :bg-gray-300 text-gray-800 font-bold py-2 px-4 rounded-r">
          Home
        </button>
        <button class="bg-gray-200 lg:hidden hover:bg-gray-300 text-gray-800 font-bold py-2 px-4 rounded-r">
          About
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
  
    data() {
        return {
            
            
        };
    },
    components: { Book },
    layout:'dashboard'
}
</script>