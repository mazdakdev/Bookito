<template>
<div class="py-6   ">
  <div class="flex bg-white rounded-lg shadow-lg overflow-hidden mx-auto max-w-sm lg:max-w-3xl align-middle  ">

        <div class=" absolute right-5 p-8 lg:w-3/4 align-middle mx-auto max-w-sm  ">
  
            <p class="text-2xl text-gray-600 text-center">Welcome Back</p>

            <div class="mt-8">
                <input value="Sign Up" class="bg-gray-700 text-white font-bold py-2 px-4 w-full rounded hover:bg-gray-600" type="submit" />
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