<template>
  <div class="area-list">
    <div v-for="(area, areaIndex) in areas" :key="areaIndex">
      <AreaCard
        :area="area"
        :boss-count="bossCounts === undefined ? 0 : bossCounts[area.name]"
        @boss-defeated="$emit('boss-defeated', $event)"
      />
    </div>
  </div>
</template>

<script lang="ts">
import AreaCard from './AreaCard.vue'
import { type Area } from '@/util/bosses-api'
import type { PropType } from 'vue'

export default {
  props: {
    areas: Array<Area>,
    bossCounts: Object as PropType<{ [location: string]: number }>,
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
