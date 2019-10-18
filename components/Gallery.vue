<template>
    <ul>
        <img @click="viewImage(image)" class="gallery-image" v-for="(image, index) in imageLinks" :key=index :src=image>
    </ul>
</template>

<script>
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
                console.log(this.galleryData[i])
                links.push('/galleries/' + this.galleryName + '/' + this.galleryData[i])
            }
            return links
        }
    },
    methods: {
        viewImage: function(imagePath) {
            window.open(imagePath)
        }
    }

}
</script>

<style lang="scss" scoped>
.gallery-image {
    max-height: 512px;
    margin: 10px;
}
</style>