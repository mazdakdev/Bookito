<template>
    <div>

        <div class="flex mt-10">
            <div class="flex-1">
                <Single img="https://images-na.ssl-images-amazon.com/images/I/51pnouuPO5L.jpg"  class="absolute left-64 rtt z-10 top-56  " ></Single>
                <img src="../assets/blob (1).svg" class="w-3/4 z-0 ">
            </div>
            <div class="flex-1  mt-24  ">
                <Card class="w-3/4" author="Steve Author" title="Don't make me think" desc="A great book to start"  category="begginer"></Card>
            </div>
        </div>
     

    </div>
</template>
    
               



</template>

<script>
import Single from "../components/Single.vue";
import Card from "../components/Card.vue";





export default {
    data() {
        return {};
    },
    layout: "dashboard",
    components: { Single , Card }
}
</script>


