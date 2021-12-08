<template>
    <section>
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

  

        <div class="flex items-center w-auto">
          <nuxt-link to="/user/login"><img src="~/assets/user.png" class="inline-block mr-12"></nuxt-link>
          <!-- icon by flaticon.com -->
          <div v-if="$auth.loggedIn">
            <p  class="mr-5">{{ $auth.user.username }}</p>
          </div>
        </div>
      </div>

      <nav class=" items-center justify-between flex-wrap w-auto text-center hidden lg:flex -mt-12">

        <div class="  flex-grow flex items-center  w-auto mr-20  ">
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

      <div>
        
        <Nuxt/>
    
      </div>

    </section>
</template>


