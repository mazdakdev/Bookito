<template>
    <div>
        <div class="overlaysingle">
        </div>
        <img :src="img"  class="w-56 h-72"  />
    </div>
</template>

<script>

  export default {
    name: 'BookSingle',
    props: ['img'],
  }

</script>

<style>


</style>