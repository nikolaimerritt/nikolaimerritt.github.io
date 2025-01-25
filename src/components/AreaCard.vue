<template>
  <div class="root">
    <h3>{{ area?.location }}</h3>
    <div>
      <div v-for="(boss, index) in area?.bosses" :key="index" class="boss">
        <span
          @click="onToggleDefeated(boss)"
          class="boss-text"
          :class="{ defeated: boss.defeated }"
        >
          {{ boss.name }}
        </span>
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
  width: 100%;
  height: 100%;
  background-color: teal;
  border-radius: 6px;
  padding: 4px;
}

.boss {
  padding: 4px 0;
}

.boss-text {
  cursor: pointer;
}

.defeated {
  text-decoration: line-through;
  font-style: italic;
}
</style>
