<template>
  <div id="app">
    <Ingredients />
  </div>
</template>

<script>
import Ingredients from "./components/Ingredients.vue";
export default {
  name: "App",
  components: {
    Ingredients,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
