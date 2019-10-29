<template>
  <ul>
    <Photo v-for="(image, index) in imageLinks" :key="index" :imagePath="image"></Photo>
  </ul>
</template>

<script>
import Photo from "./Photo";
export default {
  data() {
    return {
      totalWidth: 0
    };
  },
  props: {
    galleryName: String,
    galleryData: Array
  },
  computed: {
    imageLinks: function() {
      var links = [];
      for (var i = 0; i < this.galleryData.length; i++) {
        if (!this.galleryData[i].includes("lowres")) {
          console.log(this.galleryData[i]);
          links.push(
            "/galleries/" + this.galleryName + "/" + this.galleryData[i]
          );
        }
      }
      return links;
    }
  },
  components: {
    Photo
  }
};
</script>


