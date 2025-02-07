<template>
  <div class="progress-container">
    <progress max="1" :value="progress"></progress>
    <span v-show="current !== undefined && max !== undefined">{{ current }} / {{ max }}</span>
  </div>
</template>

<script lang="ts">
export default {
  props: {
    current: Number,
    max: Number,
  },
  computed: {
    progress(): number {
      const ratio = (this.current ?? 0) / (this.max ?? 0)
      if (isFinite(ratio)) {
        return ratio
      } else {
        return 0
      }
    },
  },
}
</script>
<style lang="css">
span {
  width: 100px;
  padding-left: 20px;
}

progress {
  width: 100%;
}

.progress-container {
  display: flex;
  flex-direction: row;
  align-items: center;
}
</style>
