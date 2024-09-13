<template>
  <v-app>
    <v-main>
      <Navbar />
      <router-view :key="$route.fullPath"/>
    </v-main>
    <AppFooter />
  </v-app>
</template>

<script setup>
import Navbar from './components/Navbar.vue';

  //
</script>
