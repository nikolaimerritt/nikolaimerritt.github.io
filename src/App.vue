<template>
  <main>
    <LoginScreen @setToken="token = $event" v-show="token === ''" />
  </main>
</template>

<script lang="ts">
import LoginScreen from './components/LoginScreen.vue'

export default {
  data() {
    return {
      token: '',
    }
  },
  methods: {},
  components: {
    LoginScreen,
  },
}
</script>

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
