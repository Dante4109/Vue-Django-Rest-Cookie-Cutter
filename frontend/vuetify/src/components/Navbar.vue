<template>
  <v-app-bar app rounded color="primary" class="hidden-xs-and-down">
    <!-- Logo -->
    
      <v-toolbar-title>
      <a @click="$router.replace('/')">
      <v-img
      src="@/assets/logo.png"
      max-height="40"
      max-width="40"
      contain
      class="mr-4">
      </v-img>
      </a>
      </v-toolbar-title>
    
    <!-- Navigation items -->
    <v-toolbar-items>
      <v-menu v-for="item in navItems" :key="item.title" class="md-center" open-on-hover offset-y>
        <template v-slot:activator="{ props }">
          <v-btn
          v-bind="props"
          :class="{ 'highlight-nav': item.highlight }"
          @click="$router.push('/product/' + item.num)"
          @mouseover="highlightItem(item)"
          @mouseleave="unhighlightItem(item)"
          >
          {{ item.title }}
        </v-btn>
      </template>
      <v-list>
        <v-list-item
        v-for="n in 5"
        :key="n"
        :value="n"
        @click="() => {}"
        >
        <v-list-item-title>Option {{ n }}</v-list-item-title>
      </v-list-item>
    </v-list>
  </v-menu>
</v-toolbar-items>

<v-spacer></v-spacer>

<!-- User profile icon -->
<v-btn icon>
  <v-icon>mdi-account-circle</v-icon>
</v-btn>
</v-app-bar>
</template>

<script setup>
import { ref } from 'vue'

const navItems = ref([
  { num: 1, title: 'Game', highlight: false },
  { num: 2, title: 'Cards', highlight: false },
  { num: 3, title: 'Community', highlight: false },
  { num: 4, title: 'News', highlight: false },
  { num: 5, title: 'Test', highlight: false },
])

const highlightItem = (item) => {
  item.highlight = true
}

const unhighlightItem = (item) => {
  item.highlight = false
}
</script>

<style scoped>
.highlight-nav {
  background-color: rgba(248, 5, 5, 0.1);
}
</style>