<template>
  <div>
    <p>So you need a "token" to save your boss kill list.</p>
    <p>
      Stick a token in the input box if youre friend sent you one. that way youll be sharing the
      boss list with your friend.
    </p>
    <p>Otherwise, you can make a token.</p>
    <p>
      Press "Generate a new token". Itll look like a key smash. Log in with that token and share it
      with your friends.
    </p>
    <div class="row">
      <button :disabled="newToken.length > 0" @click="getToken">Generate a new token</button>
      <textarea disabled v-model="newToken"></textarea>
    </div>
    <br />
    <div class="row">
      <button id="set-token" @click="setToken()">Log in with token</button>
      <input type="text" v-model="token" placeholder="Enter your token here." />
    </div>
  </div>
</template>

<script lang="ts">
import { CookieManager } from '@/util/cookie-manager'
import { KeyValueStorage } from '@/util/key-value-store'

export default {
  data() {
    return {
      token: '',
      newToken: '',
    }
  },
  methods: {
    setToken() {
      if (this.token.length > 0) {
        CookieManager.setTokenCookie(this.token)
        this.$emit('setToken', this.token)
      }
    },
    async getToken() {
      if (this.newToken.length === 0) {
        this.newToken = await KeyValueStorage.getToken()
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
<style lang="css" scoped>
.row {
  display: flex;
  flex-direction: row;
}

button:not(:disabled) {
  cursor: pointer;
}
</style>
