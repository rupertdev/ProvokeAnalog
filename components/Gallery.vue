<template>
    <ul>
	    <v-lazy-image @click="viewImage(image)" class="gallery-image" v-for="(image, index) in imageLinks" :key=index :src=image :src-placeholder=getLowResImage(image)>
    </ul>
</template>

<script>
import VLazyImage from "v-lazy-image";

export default {
    data() {
        return {
            totalWidth: 0,
        }
    },
    props: {
        galleryName: String,
        galleryData: Array
    },
    computed: {
        imageLinks: function () {
            var links = [];
            for (var i = 0; i < this.galleryData.length; i++) {
                if (!this.galleryData[i].includes('lowres')) {
                    console.log(this.galleryData[i])
                    links.push('/galleries/' + this.galleryName + '/' + this.galleryData[i])
                }
            }
            return links
        }
    },
    methods: {
        viewImage: function(imagePath) {
            window.open(imagePath)
        },
        getLowResImage: function(imagePath) {
            return imagePath + "-lowres.jpg"
        }
    },
    components: {
    	VLazyImage
    }
}
</script>

<style lang="scss" scoped>
.gallery-image {
    max-height: 512px;
    min-height: 256px;
    margin: 10px;
}
.v-lazy-image {
   filter: blur(10px);
   transition: filter 0.5s;
}
.v-lazy-image-loaded {
   filter: blur(0);
}

</style>
