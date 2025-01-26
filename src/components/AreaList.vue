<template>
  <div class="area-list">
    <div v-for="(area, areaIndex) in areas" :key="areaIndex">
      <AreaCard :area="area" @boss-defeated="$emit('boss-defeated', $event)" />
    </div>
  </div>
</template>

<script lang="ts">
import { type Area } from '@/areas'
import AreaCard from './AreaCard.vue'

export default {
  props: {
    areas: Array<Area>,
  },
  components: {
    AreaCard,
  },
}
</script>

<style>
.area-list {
  display: grid;
  grid-template-columns: repeat(auto-fit, 310px);
  column-gap: 30px;
  row-gap: 45px;
  max-width: 100%;
}

@media (max-width: 600px) {
  .area-list {
    grid-template-columns: initial;
  }
}
</style>
