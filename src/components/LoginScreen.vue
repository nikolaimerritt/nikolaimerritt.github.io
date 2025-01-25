<template>
  <div class="root">
    <div class="boxy">
      <p>So you need a password to save your boss kill list.</p>
      <p>
        Stick a password in the input box if youre friend sent you one. that way youll be sharing
        the boss list with your friend.
      </p>
      <br />
      <p>Otherwise, you can generate a password.</p>
      <p>
        Press "Generate a new password". No, you can't set your own password, we set one for you!
        Log in with the password you got and share it with your friends.
      </p>
      <br />
      <div class="row">
        <button :disabled="newPassword.length > 0" @click="getPassword">
          Generate a new password
        </button>
        <input disabled v-model="newPassword" />
      </div>
      <br />
      <div class="row">
        <button id="set-password" @click="setPassword()">Log in</button>
        <input type="text" v-model="password" placeholder="Enter your password here." />
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { CookieManager } from '@/util/cookie-manager'
import { KeyValueStorage } from '@/util/key-value-store'

export default {
  data() {
    return {
      password: '',
      newPassword: '',
    }
  },
  methods: {
    setPassword() {
      if (this.password.length > 0) {
        CookieManager.setPasswordCookie(this.password)
        this.$emit('setPassword', this.password)
      }
    },
    async getPassword() {
      if (this.newPassword.length === 0) {
        this.newPassword = await KeyValueStorage.getPassword()
      }
    },
  },
  mounted() {
    const password = CookieManager.getPasswordCookie()
    if (password !== undefined && password.length > 0) {
      this.$emit('setPassword', password)
    }
  },
}
</script>
<style lang="css" scoped>
.root {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.boxy {
  display: flex;
  padding-top: 30px;
  flex-direction: column;
  justify-content: left;
  width: 800px;
}

.row {
  display: flex;
  flex-direction: row;
}

button {
  width: 180px;
  margin-right: 12px;
}

input {
  padding-left: 12px;
}

button:not(:disabled) {
  cursor: pointer;
}
</style>
