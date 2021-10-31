<template>
<div class="home">
  <header>

  <!-- Start navbar -->
   <nav class="navbar navbar-expand-lg navbar-dark mg  " style="margin-top:-20px">
      <a class="navbar-brand" href="#" >
        <h1><i>Bookito !</i></h1>
      </a>
      <button
        class="navbar-toggler"
        type="button"
        data-toggle="collapse"
        data-target="#navbarCollapse"
        aria-controls="navbarCollapse"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarCollapse">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item active">
            <a class="nav-link" href="#">Home </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Books</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">About us</a>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/auth">Login</router-link>
          </li>  <li class="nav-item">
            <router-link class="nav-link" to="/Reg">Register</router-link>
          </li>
       

        </ul>
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
        <nuxt-link to="#" class="bg-white text-black   py-4 px-8 rounded-full  " >
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

</script>

<style lang="scss" scoped>

</style>
