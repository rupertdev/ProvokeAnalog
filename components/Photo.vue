<template>
  <v-lazy-image
    @click="viewImage(imagePath)"
    class="gallery-image"
    :src="imagePath"
    :src-placeholder="getLowResImage(imagePath)"
  ></v-lazy-image>
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
    },
    getLowResImage: function(imagePath) {
      return imagePath + "-lowres.jpg";
    }
  },
  components: { VLazyImage }
};
</script>

<style lang="scss" scoped>
.gallery-image {
  max-height: 512px;
  min-height: 256px;
  margin: 10px;
  display: inline-block;
}
.v-lazy-image {
  filter: blur(10px);
  transition: filter 0.5s;
}
.v-lazy-image-loaded {
  filter: blur(0);
}
</style>