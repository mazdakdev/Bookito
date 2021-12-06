<template>
<div class="py-6  mt-16 ">
  <div class="flex bg-white rounded-lg shadow-lg overflow-hidden mx-auto max-w-sm lg:max-w-4xl align-middle  " >
        <div   class=" lg:block lg:w-1/3 bg-cover hidden "  >
            <Single v-if="preview" :img="preview"  class="absolute left-72 rtt z-10 top-72   mt-5 " ></Single>
            <Single v-else class="absolute left-72 rtt z-10 top-72   mt-5 " :img="url + book.image" ></Single>
        </div>
        <div class="w-full p-8 lg:w-3/4  ">
          <form method="post" @submit.prevent="editBook">

            <p class="text-2xl text-gray-600 text-center">Edit you'r Book </p>
            <div class="mt-4 flex items-center justify-between">
                <span class="border-b w-1/5 lg:w-1/4"></span>
                <p  class="text-xs text-center text-gray-500 uppercase">Edit form below</p>
                <span class="border-b w-1/5 lg:w-1/4"></span>
            </div>
            <div class="mt-4">
                <div class="flex">
                    <div class="flex-1 mr-2">
                        <label class="block text-gray-700 text-sm font-bold mb-2">Name</label>
                         <input class="bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none" type="text" v-model="book.title">  
                    </div>
                    <div class="flex-1">
                        <label class="block text-gray-700 text-sm font-bold mb-2">Author</label>
                         <input class="bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none" type="text" v-model="book.author">  
                    </div>
                </div>
            </div>
            <div class="mt-4">
                <div class="flex">
                    <div class="flex-1 mr-2">
                        <label class="block text-gray-700 text-sm font-bold mb-2">Image</label>
                         <input  @change="onFileChange" class="bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none" type="file" >  
                    </div>
                    <div class="flex-1">
                        <label class="block text-gray-700 text-sm font-bold mb-2">PDF</label>
                         <input  v-on:change="pdfChange" class=" bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none" type="file">  
                    </div>
                </div>
            </div>
            <div class="mt-4">
                <div class="flex justify-between">
                    <label class="block text-gray-700 text-sm font-bold mb-2">Category</label>
                </div>
                <input type="text" v-model="book.category" class="bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none">
                 
            </div>
            <div class="mt-8">
                <input value="Edit" class="bg-gray-700 text-white font-bold py-2 px-4 w-full rounded hover:bg-gray-600" type="submit" />
              
            </div>
            <div class="mt-4 flex items-center justify-between">
                <span class="border-b w-1/5 md:w-1/4"></span>
                <nuxt-link to="/register" class="text-xs text-gray-500 uppercase">or see all books</nuxt-link>
                <span class="border-b w-1/5 md:w-1/4"></span>
            </div>

          </form>
        </div>
    </div>
    </div>

   
</template>



<script>
import Book from "~/components/Book.vue"


export default {
  
    async asyncData({ $axios, params }) {
        try {
        let book = await $axios.$get(`books/get-book/${params.id}`);
        return { book };
        } 
        catch (e) {
        return { book: [] };
      }
    },

    data() {
        return {
          
            book :{ 
                title : "",
                image : "",
                pdf : "",
                author : "",
                category : "",
                user_id : this.$auth.user.id

            },
            url: "http://127.0.0.1:8000",
            preview: ""
            
        };
    },
    methods : {
     
        onFileChange(e) {
        let files = e.target.files || e.dataTransfer.files;
        if (!files.length) {
            return;
        }
        this.book.image = files[0];
        this.createImage(files[0]);
        },
        pdfChange(e){
            let files = e.target.files || e.dataTransfer.file;
            if(!files.length){
                return
            }
            this.book.pdf = files[0];

        },
        // to show a preview of image
        createImage(file) {
        let reader = new FileReader();
        let vm = this;
        reader.onload = e => {
            vm.preview = e.target.result;
        };
        reader.readAsDataURL(file);
        },

        async editBook(){
            let editedBook = this.book

            if(!this.editBook.pdf ){
                this.$toast.error("PDF is required  !")
            }

            const config = {
                headers: { "content-type": "multipart/form-data" }
            };

            let formData = new FormData();
            for (let data in editedBook) {
                formData.append(data, editedBook[data]);
            }

            try {
                let response = await this.$axios.$put(`books/update-book/${editedBook.id}`, formData, config);
                this.$router.push("/books");
            } catch (e) {
                console.log(e);
            }
    }
    },
    components: { Book },
    layout:'dashboard',
    middleware: 'userAuth'
}
</script>