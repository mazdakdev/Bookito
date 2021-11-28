<template>
        <div class="bg-white rounded-md overflow-hidden relative   shadow-md">
          <div class="p-4">
            <h2 class="text-2xl text-green-500">{{ title }}</h2>
            <div class="flex justify-between mt-4 mb-4 text-gray-500">
        
              <div class="flex items-center">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                  <path d="M9 6a3 3 0 11-6 0 3 3 0 016 0zM17 6a3 3 0 11-6 0 3 3 0 016 0zM12.93 17c.046-.327.07-.66.07-1a6.97 6.97 0 00-1.5-4.33A5 5 0 0119 16v1h-6.07zM6 11a5 5 0 015 5v1H1v-1a5 5 0 015-5z" />
                </svg>
                <span class="ml-1 lg:text-xl"> &nbsp; {{ author }}</span>
              </div>
            </div>
            <p class="mb-4 text-gray-600">{{ desc }}</p>
            <button class="text-white bg-green-500 p-4 rounded-md w-full uppercase">Buy Now </button>
          </div>
          <div class="absolute top-0 right-0 mt-4 mr-4 bg-purple-600 text-white rounded-full pt-1 pb-1 pl-4 pr-5 text-xs uppercase">
            <span>{{ category }}</span>
            
          </div>

        </div>
</template>

<script>
import { defineComponent } from '@vue/composition-api'

export default defineComponent({
  props: [ 'title' , 'author' , 'desc' , 'category'],
})
</script>
