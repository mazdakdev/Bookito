<template>
<div class="py-6   ">
  <div class="flex bg-white rounded-lg shadow-lg overflow-hidden mx-auto max-w-sm lg:max-w-4xl align-middle  ">

        <div class="w-full p-8 lg:w-3/4 align-middle mx-auto max-w-sm  ">
          <form method="post" @submit.prevent="register">

            <p class="text-2xl text-gray-600 text-center">Welcome Back</p>
            <div class="mt-4 flex items-center justify-between">
                <span class="border-b w-1/5 lg:w-1/4"></span>
                <p  class="text-xs text-center text-gray-500 uppercase">Register Now</p>
                <span class="border-b w-1/5 lg:w-1/4"></span>
            </div>
            <div class="mt-4">
                <label class="block text-gray-700 text-sm font-bold mb-2">Username</label>
                <input class="bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none" type="text" v-model="username">
            </div>
            <div class="mt-4">
                <label class="block text-gray-700 text-sm font-bold mb-2">First Name</label>
                <input class="bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none" type="text" v-model="first_name">
            </div>
            <div class="mt-4">
                <label class="block text-gray-700 text-sm font-bold mb-2">Last Name</label>
                <input class="bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none" type="text" v-model="last_name">
            </div>
            <div class="mt-4">
                <div class="flex justify-between">
                    <label class="block text-gray-700 text-sm font-bold mb-2">Password</label>
                </div>
                <input class="bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none" type="password" v-model="password">
            </div>
            <div class="mt-4">
                <div class="flex justify-between">
                    <label class="block text-gray-700 text-sm font-bold mb-2">Password Confirmation</label>
                </div>
                <input class="bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none" type="password" v-model="password2">
            </div>
            <div class="mt-8">
                <input value="Sign Up" class="bg-gray-700 text-white font-bold py-2 px-4 w-full rounded hover:bg-gray-600" type="submit" />
              
            </div>
            <div class="mt-4 flex items-center justify-between">
                <span class="border-b w-1/5 md:w-1/4"></span>
                <nuxt-link to="/user/login" class="text-xs text-gray-500 uppercase">or Login</nuxt-link>
                <span class="border-b w-1/5 md:w-1/4"></span>
            </div>

          </form>
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
      password2:"",
      first_name:"",
      last_name:"",
    }
  },
  methods: {
    async register(){
      if (this.password == this.password2){
        await this.$axios.post('register/',{"username":this.username , "password":this.password ,
             "first_name":this.first_name, "last_name":this.last_name}).then((reponse) => {
               this.$toast.success("Registered successfully :)")
             })
             .catch((error) =>{
               this.$toast.error(error)
             })
             this.$auth.loginWith('local' , {
               data : {"username" : this.username , "password" : this.password}
             })
      }
      else{
        this.$toast.error("Password and Password Confirmation aren't same")
      }
    }
  }
}

</script>

<style scoped>

</style>