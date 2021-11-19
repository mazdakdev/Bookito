<template>
  <div>
    <b class="text-4xl ml-12 absolute top-44 border-gray-700 text-gray-700 border-l-4  "> &nbsp; All the Books</b>

    <div class="flex mt-36">

      <div class="flex-1 ml-32">
        <Book img="https://images-na.ssl-images-amazon.com/images/I/51pnouuPO5L.jpg" author="Steve Krug" title="Dont make me think"></Book>
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