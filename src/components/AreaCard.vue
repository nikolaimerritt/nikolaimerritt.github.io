<template>
  <div class="root">
    <h3>{{ area?.location }}</h3>
    <div class="boss-list">
      <div v-for="(boss, index) in area?.bosses" :key="index" class="boss">
        <button @click="onToggleDefeated(boss)">X</button>
        <span> {{ boss.name }} </span>
        <span v-if="boss.defeated"> (Defeated) </span>
      </div>
    </div>
  </div>
</template>
<script lang="ts">
import { type Area, type Boss } from '@/areas'
import type { PropType } from 'vue'

export default {
  props: {
    area: Object as PropType<Area>,
  },
  methods: {
    onToggleDefeated(boss: Boss) {
      this.$emit('boss-defeated', boss)
    },
  },
}
</script>

<style scoped>
.root {
  width: 250px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  margin: 0 10px;
}
.boss-list {
  display: flex;
  flex-direction: column;
}

.boss {
  display: flex;
  flex-direction: row;
  width: 200px;
}
</style>
