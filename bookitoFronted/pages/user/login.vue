<template>
<div class="py-6  mt-16 ">
  <div class="flex bg-white rounded-lg shadow-lg overflow-hidden mx-auto max-w-sm lg:max-w-4xl align-middle  " v-if="!$auth.loggedIn">
        <div   class=" lg:block lg:w-1/3 bg-cover hidden" >
          <img src="~/assets/5488161.jpg">
        </div>
        <div class="w-full p-8 lg:w-3/4  ">
          <form method="post" @submit.prevent="login">

            <p class="text-2xl text-gray-600 text-center">Welcome Back</p>
            <div class="mt-4 flex items-center justify-between">
                <span class="border-b w-1/5 lg:w-1/4"></span>
                <p  class="text-xs text-center text-gray-500 uppercase">login with Username</p>
                <span class="border-b w-1/5 lg:w-1/4"></span>
            </div>
            <div class="mt-4">
                <label class="block text-gray-700 text-sm font-bold mb-2">Username</label>
                <input class="bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none" type="text" v-model="username">
            </div>
            <div class="mt-4">
                <div class="flex justify-between">
                    <label class="block text-gray-700 text-sm font-bold mb-2">Password</label>
                </div>
                <input class="bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none" type="password" v-model="password">
            </div>
            <div class="mt-8">
                <input value="Log In" class="bg-gray-700 text-white font-bold py-2 px-4 w-full rounded hover:bg-gray-600" type="submit" />
              
            </div>
            <div class="mt-4 flex items-center justify-between">
                <span class="border-b w-1/5 md:w-1/4"></span>
                <nuxt-link to="/register" class="text-xs text-gray-500 uppercase">or sign up</nuxt-link>
                <span class="border-b w-1/5 md:w-1/4"></span>
            </div>

          </form>
        </div>
    </div>

   <div class="flex bg-white rounded-lg shadow-lg overflow-hidden mx-auto max-w-sm lg:max-w-4xl align-middle  " v-if="$auth.loggedIn">
        <div   class=" lg:block lg:w-1/3 bg-cover hidden" >
          <img src="~/assets/5488161.jpg" class="mt-5">
        </div>
        <div class="w-full p-8 lg:w-3/4  ">

            <p class="text-2xl text-gray-600 text-center">Welcome to Bookito <i>!</i></p>
            <div class="mt-4 flex items-center justify-between">
                <span class="border-b w-1/5 lg:w-1/4"></span>
                <p  class="text-xs text-center text-gray-500 uppercase">You'r details</p>
                <span class="border-b w-1/5 lg:w-1/4"></span>
            </div>
            <div class="mt-4">
                <label class="block text-gray-700 text-sm font-bold mb-2">Username</label>
                <p class="text-2xl">{{ $auth.user.username }}</p>
            </div>
            <div class="mt-4">
                <div class="flex justify-between">
                    <label class="block text-gray-700 text-sm font-bold mb-2">First Name</label>
                </div>
                <p class="text-2xl">{{ $auth.user.first_name }}</p>
            </div>
            <div class="mt-4">
                <div class="flex justify-between">
                    <label class="block text-gray-700 text-sm font-bold mb-2">Last Name</label>
                </div>
                <p class="text-2xl">{{ $auth.user.last_name }}</p>
            </div>
            <div class="mt-8">
                <button  class="bg-gray-700 text-white font-bold py-2 px-4 w-full rounded hover:bg-gray-600" @click="$auth.logout()" >Log out</button>

            </div>
            <div class="mt-4 flex items-center justify-between">
                <span class="border-b w-1/5 md:w-1/4"></span>
                <nuxt-link to="/user/register" class="text-xs text-gray-500 uppercase">or sign up</nuxt-link>
                <span class="border-b w-1/5 md:w-1/4"></span>
            </div>
        </div>
    </div>

</div>
</template>

<script>

export default{
  layout: "dashboard",
  data(){
    return {
      username : "",
      password : "",
    }
  },
  methods: {
    async login(){
      try{
        await this.$auth.loginWith('local',{
          data:{
            username : this.username,
            password : this.password,
          }
        })
        this.$router.push("/books")

      }catch(e){
        this.$toast.error(e)
        console.log(e)
      }
    }
  }
}

</script>

