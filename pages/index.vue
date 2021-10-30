<template>
<div class="home">
  <header>

  <!-- Start navbar -->
    <nav class="flex items-center justify-between flex-wrap bg-teal-500 p-6">
      <div class="flex items-center flex-shrink-0 text-white mr-6">
        <span class="font-semibold text-4xl tracking-tight"><i>Bookito</i> &nbsp; <i>!</i> </span>
      </div>
      <div class="block lg:hidden">
        <button class="flex items-center px-3 py-2 border rounded text-teal-200 border-teal-400 hover:text-white hover:border-white">
          <svg class="fill-current h-3 w-3" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><title>Menu</title><path d="M0 3h20v2H0V3zm0 6h20v2H0V9zm0 6h20v2H0v-2z"/></svg>
        </button>
      </div>
      <div class="w-full block flex-grow lg:flex lg:items-center lg:w-auto">
        <div class=" lg:flex-grow ml-16 ">
                    
          <a href="#responsive-header" class="block mt-4 lg:inline-block lg:mt-0 text-xl text-white mr-8  ">
            Home
            
          </a>

          <a href="#responsive-header" class="block mt-4 lg:inline-block lg:mt-0  text-xl text-white mr-8  ">
            Books
          </a>

          <a href="#responsive-header" class="block mt-4 lg:inline-block lg:mt-0 text-xl text-white">
            About us
          </a>

        </div>
      </div>
    </nav>
<!-- End navbar -->

<section>
  <div class="flex  ">
    <div class="flex-1 slideInLeft">
      <div class="flex flex-col text-center justify-center mt-52 space-y-7">

        <div class="flex-1 ">
          <p class="text-white  text-5xl"> All the books you want </p>
        </div>
      
      <div class="flex-1">
        <p class=" text-white text-sm">welcome to your own book library all the books are organized  <br>  just the way you like   </p>
      </div>
      
      <div class="flex-1 m-t">
        <nuxt-link to="#" class="bg-white text-black   py-4 px-8 rounded-full  ">
          All Books
       
        </nuxt-link>
      </div>
      </div>
    </div>
    <div class="flex-1 ">
           
         <img id="book" src="../assets/header-img.png" class="book position-absolute zoomInDown " alt="Book" />
          
    </div>

  </div>
</section>

  </header>
</div>



</template>

<script>
export default {};
</script>

<style lang="scss" scoped>

</style>
