<template>
  <div>
    <p>So you need a "token" to save your boss kill list.</p>
    <p>
      Stick a token in the input box if youre friend sent you one. that way youll be sharing the
      boss list with your friend.
    </p>
    <p>Otherwise, you can make a token.</p>
    <p>
      Go to
      <a href="https://keyvalue.immanuel.co/">this website</a> (dont ask lol) and press Get App Key
      on the top right. Itll look like a key smash. Thats your token.
    </p>
    <input type="text" v-model="token" />
    <button id="set-token" @click="setToken()">Log in with token.</button>
  </div>
</template>

<script lang="ts">
import { CookieManager } from '@/util/cookie-manager'

export default {
  data() {
    return {
      token: '',
    }
  },
  methods: {
    setToken() {
      if (this.token.length > 0) {
        CookieManager.setTokenCookie(this.token)
        this.$emit('setToken', this.token)
      }
    },
  },
  mounted() {
    const token = CookieManager.getTokenCookie()
    if (token !== undefined && token.length > 0) {
      this.$emit('setToken', token)
    }
  },
}
</script>
