<template>
  <div class="home">
    <header>
    
      <div class=" text-white mr-6 lg:hidden md:hidden absolute top-2 left-2">
          <span class="font-semibold text-3xl tracking-tight">
            <nuxt-link to="/"><i>Bookito</i> &nbsp; <i>!</i></nuxt-link>
          </span>
        </div>
      <!-- START navbar -->
      <nav class="lg:flex sm:flex items-center justify-between flex-wrap bg-teal-500 p-6 hidden ">
        <div class="flex items-center flex-shrink-0 text-white mr-6">
          <span class="font-semibold text-4xl tracking-tight">
            <nuxt-link to="/"><i>Bookito</i> &nbsp; <i>!</i></nuxt-link>
          </span>
        </div>

        <div class="  flex-grow flex items-center w-auto ">
          <div class="flex-grow  ">
            <nuxt-link to="/" class=" inline-block mt-0 sm:text-3xl   lg:text-xl text-white ml-10 ">
              Home
            </nuxt-link>

            <nuxt-link to="/books" class="  inline-block mt-0 sm:text-3xl   lg:text-xl text-white ml-14 ">
              Books
            </nuxt-link>


          </div>
        </div>
      </nav>
      <!-- END navbar -->

      <!-- START main of header -->
      <div class=" absolute top-24 left-3">
        <div class="flex  ">
          <div class="flex-1 slideInLeft ml-1">
            <div class="flex flex-col text-center justify-center mt-52 xs:mt-32 space-y-7 " >
              <div class="flex-1 ">
           
                  <vue-typer text="All the books you want"  ></vue-typer>
  
              </div>

              <div class="flex-1">
                <p class=" text-white text-sm sm:text-xl xs:text-xl">
                  
                  welcome to your own book library all the books are organized
                  <br />
                  just the way you like
                </p>
              </div>

              <div class="flex-1 ">
                <nuxt-link to="/books" class="bg-white text-black   sm:text-2xl lg:text-xl lg:py-4 lg:px-7 py-4 px-8 xs:py-4 xs:px-7  rounded-full ">
                 All the books
                </nuxt-link>
              </div>
            </div>
          </div>
          <div class="flex-1 mr-1 ">
            <img id="book" src="../assets/header-img.png" class="book zoomInDown  lg:w-3/5 lg:ml-48 lg:mt-5 md:mt-10 xs:mt-32 "  alt="Book" />
          </div>

      </div>
      </div>
      <!-- END main of header -->

      <!-- START of Mobile nav -->

      <div class="xs:flex items-center  w-10/12 rounded-full flex-wrap  p-6 lg:hidden sm:hidden md:hidden absolute bottom-5 mt-10 shadow-md  left-8 bg-purple-800 ">
        <div class="flex-grow flex items-center w-auto justify-center  ">
          <div class="flex-grow  ">

            <nuxt-link to="/" class=" inline-block mt-0 xs:text-2xl   text-white ml-10 ">
              Home
            </nuxt-link>

            <nuxt-link to="/books" class="  inline-block mt-0 xs:text-2xl   text-white ml-14 ">
              Books
            </nuxt-link>

          </div>
        </div>
      </div>
      <!-- END -->
 
    </header>
  </div>

</template>
