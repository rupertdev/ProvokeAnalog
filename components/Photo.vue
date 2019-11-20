<template>
  <img @click="viewImage(imagePath)" class="gallery-image" :src="lfsImagePath" />
</template>

<script>
import VLazyImage from "v-lazy-image";
export default {
  props: {
    imagePath: String
  },
  methods: {
    viewImage: function(imagePath) {
      window.open(imagePath);
    }
  },
  computed: {
    lfsImagePath: function() {
      return this.imagePath + "?nf_resize=fit&w=300";
    }
  }
};
</script>

<style lang="scss" scoped>
.gallery-image {
  max-height: 512px;
  min-height: 256px;
  margin: 10px;
  display: inline-block;
}
</style>