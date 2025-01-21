<template>
  <div>
    <div v-for="(area, areaIndex) in areas" :key="areaIndex">
      <span> {{ area.location }} </span>
      <div v-for="(boss, bossIndex) in area.bosses" :key="bossIndex">
        <span> {{ boss.name }} </span>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { type Area } from '@/areas'

export default {
  props: {
    areas: Array<Area>,
  },
}
</script>
