<template>
  <div class="home">
    <header>
      <!-- START navbar -->
      <nav class="lg:flex sm:flex items-center justify-between flex-wrap bg-teal-500 p-6 hidden ">
        <div class="flex items-center flex-shrink-0 text-white mr-6">
          <span class="font-semibold text-4xl tracking-tight">
            <i>Bookito</i> &nbsp; <i>!</i>
          </span>
        </div>

        <div class="  flex-grow flex items-center w-auto ">
          <div class="flex-grow  ">
            <a href="#responsive-header" class=" inline-block mt-0 sm:text-3xl   lg:text-xl text-white ml-10 ">
              Home
            </a>

            <a href="#responsive-header" class="  inline-block mt-0 sm:text-3xl   lg:text-xl text-white ml-14 ">
              Books
            </a>


          </div>
        </div>
      </nav>
      <!-- END navbar -->

      <!-- START main of header -->
      <section>
        <div class="flex  ">
          <div class="flex-1 slideInLeft">
            <div class="flex flex-col text-center justify-center mt-52 xs:mt-32 space-y-7 " >
              <div class="flex-1 ">
                <p class="text-white  lg:text-5xl text-3xl sm:text-6xl ">
                  All the books you want
                </p>
              </div>

              <div class="flex-1">
                <p class=" text-white text-sm sm:text-xl xs:text-xl">
                  welcome to your own book library all the books are organized
                  <br />
                  just the way you like
                </p>
              </div>

              <div class="flex-1 ">
                <nuxt-link to="#" class="bg-white text-black   sm:text-2xl lg:text-xl lg:py-4 lg:px-7 py-4 px-8 xs:py-4 xs:px-7  rounded-full ">
                 All the books
                </nuxt-link>
              </div>
            </div>
          </div>
          <div class="flex-1 ">
            <img id="book" src="../assets/header-img.png" class="book position-absolute zoomInDown sm:mt-64 lg:w-3/5 lg:ml-48 lg:mt-5  xs:mt-32 "  alt="Book" />
          </div>
        </div>
      </section>
      <!-- END main of header -->

      <!-- START of Mobile nav -->

      <div class="xs:flex items-center  w-10/12 rounded-full flex-wrap bg-teal-500 p-6 lg:hidden sm:hidden md:hidden absolute bottom-3 left-8 bg-purple-800  ">
        <div class="flex-grow flex items-center w-auto ">
          <div class="flex-grow  ">

            <a href="#responsive-header" class=" inline-block mt-0 xs:text-2xl   text-white ml-10 ">
              Home
            </a>

            <a href="#responsive-header" class="  inline-block mt-0 xs:text-2xl   text-white ml-14 ">
              Books
            </a>

          </div>
        </div>
      </div>
      <!-- END -->

  </header>
     
  
  </div>
</template>
<script>
export default {};
</script>

<style lang="scss" scoped></style>
