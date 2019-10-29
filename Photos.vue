// App.vue

<template>
  <div class="app">
    <div class="nav">
      <h2>Provoke Analog</h2>
      <ul class="galleries-list">
        <li :class="{'gallery-list-item': true, 'gallery-list-item-selected': (galleryName == activeGallery)}" v-for="(images, galleryName) in galleryMap " :key=galleryName>
          <a @click="changeGallery(galleryName)">{{galleryName}}</a>
        </li>
      </ul>
      <div class="social-icon-tray">
        <a href='https://webring.xxiivv.com/#random' target='_blank'><img class="social-icon" src='https://webring.xxiivv.com/icon.black.svg'/></a>
        <a href='https://twitter.com/Spoopert' target='_blank'><img class="social-icon" src='/static/assets/twitter-icon.svg'/></a>
        <a href='https://merveilles.town/@rupert' target='_blank'><img class="social-icon" src='/static/assets/mastodon-icon.svg'/><a>
      </div>
    </div>
    <div class="content">
      <gallery :galleryData=galleryMap[activeGallery] :galleryName=activeGallery>
    </div>
  </div>
</template>

<script>
import Vue from "vue";
import gallery_map from './static/gallery_map.json'
import Gallery from './components/Gallery'

export default Vue.extend({
  data() {
    return {
      bundler: "Parcel",
      galleryMap: gallery_map,
      activeGallery: '35mmBlackAndWhite'
    };
  },
  methods: {
    changeGallery: function(newGalleryName) {
      this.activeGallery = newGalleryName;
    }
  },
  components: {
    Gallery
  }
});
</script>

<style lang="scss" scoped>
h2 {
  color:  #EE0006
}

.container {
  color: green;
}

.nav {
  float: left;
  height: 100%;
  position: fixed;
  top: 0;
  z-index: 999999;
  width: 200px;
  min-height: 550px;
  left: 50px;
}

.content {
  margin-left: 280px;
}

.gallery-link {
  color: grey
}

.app {
  font-family: Be Vietnam, sans-serif
}

.galleries-list {
  list-style-type: none;
  margin: 1px;
  padding: 0;
}

.gallery-list-item-selected {
  color: #EE0006
}

.social-icon {
  max-height: 25px;
  max-width: 25px;
  color: black
}

.social-icon-tray {
  margin-top: 10px
}
</style>