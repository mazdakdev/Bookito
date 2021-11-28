<template>
    <div @mouseover="width = 'w-56' ,height = 'h-72' "  @mouseleave="width = 'w-48' ,height = 'h-64'" >
        <div class="overlay" @mouseover="width = 'w-56' ,height = 'h-72' "  @mouseleave="width = 'w-48' ,height = 'h-64'">
        </div>
        <img :src="img"  :class="[width ,  height ] "  />
                
        <div class="mt-3">
            <p class="text-gray-800 text-xl "> {{ title }} </p>
             <p class="text-sm text-gray-500 "> {{ author }} </p>
        </div> 
    </div>
</template>

<script>

  export default {
    name: 'Book',
    props: ['img' , 'title' , 'author' , 'isResponsive'],
    data () {
      return {
       width:'w-48',
       height: 'h-64',
       
     
      }
      
    },



  }
</script>

<style>


</style>