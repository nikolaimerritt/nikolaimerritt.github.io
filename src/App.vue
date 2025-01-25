<template>
  <main>
    <div class="main-container">
      <LoginScreen @setToken="loadAreas($event)" v-show="areas.length === 0" />
      <AreaList :areas="areas" @boss-defeated="onBossDefeated($event)" />
    </div>
  </main>
</template>

<script lang="ts">
import { Areas, type Area, type Boss } from './areas'
import AreaList from './components/AreaList.vue'
import LoginScreen from './components/LoginScreen.vue'
import { KeyValueStorage } from './util/key-value-store'

type Data = {
  token: string
  areas: Area[]
  keyValueStorage: KeyValueStorage | undefined
}

export default {
  data(): Data {
    return {
      token: '',
      areas: [],
      keyValueStorage: undefined,
    }
  },
  methods: {
    async loadAreas(token: string) {
      this.keyValueStorage = new KeyValueStorage(token)
      this.areas = await this.keyValueStorage.loadBossesDefeated(Areas)
      console.log('Loaded bosses', this.areas)
    },
    async onBossDefeated(boss: Boss) {
      console.log('app: boss defeated', boss)
      const ownBoss = this.areas.flatMap((area) => area.bosses).find((b) => b.id == boss.id)
      if (ownBoss) {
        ownBoss.defeated = !ownBoss?.defeated
        await this.keyValueStorage?.saveBossesDefeated(this.areas)
      }
    },
  },
  components: {
    LoginScreen,
    AreaList,
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

main {
  display: flex;
  flex-direction: row;
  justify-content: center;
}

.main-container {
  width: 80%;
}
</style>
