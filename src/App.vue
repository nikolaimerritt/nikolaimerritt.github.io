<template>
  <main>
    <nav>
      <h2>Elden Ring Boss Tracker</h2>
      <span>Password: {{ password }}</span>
      <button v-if="password.length > 0" @click="logout">Log out</button>
    </nav>
    <div class="main-container">
      <marquee scrollamount="10">ohhhhhhhhhhh sheldon ring</marquee>
      <LoginScreen @setPassword="loadAreas($event)" v-show="password.length === 0" />
      <div class="input-container" v-show="password.length > 0">
        <input type="text" v-model="searchText" placeholder="Search here" />
      </div>
      <div class="progress-bar-container" v-show="password.length > 0">
        <ProgressBar class="progress-bar" :progress="bossProgress()"></ProgressBar>
      </div>
      <div class="areas-container" v-show="password.length > 0">
        <AreaList :areas="areas" @boss-defeated="onBossDefeated($event)" />
      </div>
    </div>
  </main>
</template>

<script lang="ts">
import { Areas, type Area, type Boss } from './areas'
import AreaList from './components/AreaList.vue'
import LoginScreen from './components/LoginScreen.vue'
import ProgressBar from './components/ProgressBar.vue'
import { CookieManager } from './util/cookie-manager'
import { KeyValueStorage } from './util/key-value-store'

type Data = {
  password: string
  originalAreas: Area[]
  areas: Area[]
  searchText: string
  keyValueStorage: KeyValueStorage | undefined
}

export default {
  data(): Data {
    return {
      password: '',
      originalAreas: [],
      areas: [],
      searchText: '',
      keyValueStorage: undefined,
    }
  },
  methods: {
    async loadAreas(password: string) {
      this.password = password
      this.keyValueStorage = new KeyValueStorage(password)
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
    bossProgress() {
      const bosses = this.originalAreas.flatMap((area) => area.bosses)
      const progress = bosses.filter((boss) => boss.defeated).length / bosses.length
      if (isFinite(progress)) {
        return progress
      }
      return 0
    },
    logout() {
      CookieManager.deletePasswordCookie()
      window.location.reload()
    },
  },
  components: {
    LoginScreen,
    AreaList,
    ProgressBar,
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
nav {
  position: fixed;
  top: 0;
  background-color: #0f0f0f;
  width: 100%;
  padding-left: 10%;
  display: flex;
  flex-direction: row;
  z-index: 100;
}

nav h2 {
  width: 100%;
}

button {
  cursor: pointer;
}

nav button {
  width: 100px;
}

marquee {
  font-size: 20px;
  padding-bottom: 20px;
}

header {
  line-height: 1.5;
}

input {
  width: 700px;
  height: 35px;
  padding: 15px;
  border-radius: 12px;
  margin-bottom: 40px;
  font-size: 16px;
}

.input-container {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.areas-container {
  display: flex;
  justify-content: center;
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
  width: 85%;
  display: flex;
  flex-direction: column;
}

.progress-bar {
  width: 90%;
  margin-bottom: 15px;
}

.progress-bar-container {
  display: flex;
  flex-direction: row;
  justify-content: center;
  width: 100%;
}
</style>
