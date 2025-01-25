<template>
  <progress max="1" :value="progress !== undefined && isFinite(progress) ? progress : 0"></progress>
</template>

<script lang="ts">
export default {
  props: {
    progress: Number,
  },
}
</script>
