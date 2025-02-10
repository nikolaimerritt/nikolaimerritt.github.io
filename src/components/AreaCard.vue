<template>
  <div class="root">
    <h3 :class="{ defeated: area?.bosses.filter((boss) => boss.defeated).length === bossCount }">
      {{ area?.name }}
    </h3>

    <hr />
    <div>
      <div v-for="(boss, index) in area?.bosses" :key="index" class="boss">
        <span @click="onToggleDefeated(boss)" :class="{ defeated: boss.defeated }">
          {{ boss.name }}
        </span>
      </div>
    </div>
  </div>
</template>
<script lang="ts">
import { type Area, type Boss } from '@/util/bosses-api'
import type { PropType } from 'vue'

export default {
  props: {
    area: Object as PropType<Area>,
    bossCount: Number,
  },
  methods: {
    onToggleDefeated(boss: Boss) {
      this.$emit('boss-defeated', boss)
    },
  },
}
</script>

<style scoped>
h3 {
  font-size: 20px;
}

hr {
  margin-bottom: 8px;
}

.root {
  width: 100%;
  height: 100%;
  background-color: #413a2b;
  border-radius: 6px;
  padding: 12px 24px;
}

.root:hover {
  transform: scale(1.01);
  animation-timing-function: ease;
}

.boss {
  padding: 4px 0;
}

span {
  cursor: pointer;
}

.defeated {
  text-decoration: line-through;
  font-style: italic;
  font-weight: 100;
  color: #6d6961;
}
</style>
