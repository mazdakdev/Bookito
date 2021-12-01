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

        <div class=" flex-grow flex items-center w-auto ">
            <div class="pt-2 relative mx-auto text-gray-600">
              <input class="border-2 border-gray-300 bg-gray-50 h-10 px-44 pr-16 rounded-lg text-sm focus:outline-none" type="search" name="search" placeholder="Search">
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
          <nuxt-link to="/login"><img src="../assets/user.png" class="inline-block mr-12"></nuxt-link>
          <!-- icon by flaticon.com -->
          <div v-if="$auth.loggedIn">
            <nuxt-link to="/profile" class="mr-5">{{ $auth.user.username }}</nuxt-link>
          </div>
        </div>
      </div>

      <nav class=" items-center justify-between flex-wrap w-auto text-center hidden lg:flex">

        <div class="  flex-grow flex items-center  w-auto ">
          <div class="flex-grow ">
            <nuxt-link to="/" class=" inline-block mt-0   lg:text-base text-gray-500 ml-10   hover:text-indigo-600">
              Home
            </nuxt-link>

            <nuxt-link to="Allbooks" class="  inline-block mt-0    lg:text-base text-gray-500 hover:text-indigo-600  ml-14 ">
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


