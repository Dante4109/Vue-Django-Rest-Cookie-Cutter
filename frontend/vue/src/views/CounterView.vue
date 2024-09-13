<script setup>
import { storeToRefs } from 'pinia'
import { useCounterStore } from '@/stores/counter';

const store = useCounterStore();
const { count } = storeToRefs(store) // REACTIVE
console.log(count) // => REF
store.count++;
store.increment(2);
</script>


<template>
  <div class="counter">
    <h1>Count is {{ store.count }}</h1>
    <button @click="store.increment(1)"> Increment</button>
    <h1>Double is {{ store.doubleCount }}</h1>
    <button @click="store.waitAndAdd">Wait + Increment</button>
  </div>
  
</template>


<style>
@media (min-width: 1024px) {
  .counter {
    /* min-height: 100vh; */
    /* display: flex; */
    align-items: center;

    text-align: center;
    margin-top: 60px;
  }
}
</style>
