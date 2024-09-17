<template>
  <v-app>
    <v-main>
      <Navbar />
      <v-layout>
        <Registration />
      </v-layout>
      <router-view :key="$route.fullPath"/>
    </v-main>
    <notifications group="authentication" position="bottom right" style="z-index: 99999;"/>
    <AppFooter />
  </v-app>
</template>

<script setup>
import Navbar from './components/Navbar.vue';

  //
</script>
