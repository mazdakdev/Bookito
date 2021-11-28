<template>
    <div>

        <div class="lg:flex mt-10 xs:hidden  ">
            <div class="flex-1">
                <Single img="https://images-na.ssl-images-amazon.com/images/I/51pnouuPO5L.jpg"  class="absolute left-64 rtt z-10 top-56  " ></Single>
                <img src="../assets/blob (1).svg" class="w-3/4 z-0 ">
            </div>
            <div class="flex-1  mt-24  ">
            <div class="bg-white rounded-md overflow-hidden relative   shadow-md  w-4/5">
                <div class="p-4">
                    <h2 class="text-2xl text-green-500">s</h2>
                    <div class="flex justify-between mt-4 mb-4 text-gray-500">
                
                    <div class="flex items-center">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                        <path d="M9 6a3 3 0 11-6 0 3 3 0 016 0zM17 6a3 3 0 11-6 0 3 3 0 016 0zM12.93 17c.046-.327.07-.66.07-1a6.97 6.97 0 00-1.5-4.33A5 5 0 0119 16v1h-6.07zM6 11a5 5 0 015 5v1H1v-1a5 5 0 015-5z" />
                        </svg>
                        <span class="ml-1 lg:text-xl"> &nbsp; s</span>
                    </div>
                    </div>
                    <p class="mb-4 text-gray-600"></p>
                    <button class="text-white bg-green-500 p-4 rounded-md w-full uppercase">Buy Now </button>
                </div>
                <div class="absolute top-0 right-0 mt-4 mr-4 bg-purple-600 text-white rounded-full pt-1 pb-1 pl-4 pr-5 text-xs uppercase">
                <span>Action</span>
                </div>


            </div>
            </div>
        </div>

        <div class=" w-11/12 ml-4  text-left mt-52 lg:hidden">

            <div class="bg-white rounded-md overflow-hidden relative   shadow-md">
                <div class="p-4">
                    <h2 class="text-2xl text-green-500">Book title</h2>
                    <div class="flex justify-between mt-4 mb-4 text-gray-500">
                
                    <div class="flex items-center">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                        <path d="M9 6a3 3 0 11-6 0 3 3 0 016 0zM17 6a3 3 0 11-6 0 3 3 0 016 0zM12.93 17c.046-.327.07-.66.07-1a6.97 6.97 0 00-1.5-4.33A5 5 0 0119 16v1h-6.07zM6 11a5 5 0 015 5v1H1v-1a5 5 0 015-5z" />
                        </svg>
                        <span class="ml-1 lg:text-xl"> &nbsp; Book author</span>
                    </div>
                    </div>
                    <p class="mb-4 text-gray-600">book is loream book is ipsum book is dolar</p>
                    <button class="text-white bg-green-500 p-4 rounded-md w-full uppercase">Buy Now </button>
                </div>
                <div class="absolute top-0 right-0 mt-4 mr-4 bg-purple-600 text-white rounded-full pt-1 pb-1 pl-4 pr-5 text-xs uppercase">
                <span>Action</span>
            
                </div>


            </div>
        </div>
     
        <div class="xs:flex items-center  w-10/12 rounded-full flex-wrap  p-6 lg:hidden sm:hidden md:hidden absolute bottom-5 mt-10 shadow-md  left-8 bg-purple-800 ">
        <div class="flex-grow flex items-center w-auto justify-center  ">
          <div class="flex-grow  ">

            <nuxt-link to="/" class=" inline-block mt-0 xs:text-2xl   text-white ml-10 ">
              Home
            </nuxt-link>

            <nuxt-link to="/Allbooks" class="  inline-block mt-0 xs:text-2xl   text-white ml-14 ">
              Books
            </nuxt-link>

          </div>
        </div>
      </div>
    </div>
</template>
    
               



</template>

<script>
import Single from "../components/Single.vue";


export default {
    data() {
        return {};
    },
    layout: "dashboard",
    components: { Single  }
}
</script>


