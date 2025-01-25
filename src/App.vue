<template>
  <main>
    <div class="main-container">
      <LoginScreen @setToken="loadAreas($event)" v-show="token.length === 0" />
      <div class="area-stuff" v-show="token.length > 0">
        <input type="text" v-model="searchText" placeholder="Search here" />
        <AreaList :areas="areas" @boss-defeated="onBossDefeated($event)" />
      </div>
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
  originalAreas: Area[]
  areas: Area[]
  searchText: string
  keyValueStorage: KeyValueStorage | undefined
}

export default {
  data(): Data {
    return {
      token: '',
      originalAreas: [],
      areas: [],
      searchText: '',
      keyValueStorage: undefined,
    }
  },
  methods: {
    async loadAreas(token: string) {
      this.token = token
      this.keyValueStorage = new KeyValueStorage(token)
      this.originalAreas = await this.keyValueStorage.loadBossesDefeated(Areas)
      this.areas = this.originalAreas.slice()
    },
    async onBossDefeated(boss: Boss) {
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
  watch: {
    searchText(toSearch: string) {
      const toSearchLowered = toSearch.toLowerCase().trim()
      console.log('Searching with', toSearch)
      this.areas = this.originalAreas.map(
        (area) => ({ location: area.location, bosses: area.bosses.slice() }) as Area,
      )
      for (const area of this.areas) {
        if (area.location.toLowerCase().includes(toSearchLowered)) {
          continue
        }
        area.bosses = area.bosses.filter((boss) =>
          boss.name.toLowerCase().includes(toSearchLowered),
        )
      }
      this.areas = this.areas.filter(
        (area) => area.location.toLowerCase().includes(toSearchLowered) || area.bosses.length > 0,
      )
    },
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
