<template>
  <div v-if="errorMsg" class="error-modal">
    <div class="error-modal-content">
      <span>{{ errorMsg }}</span>
      <button @click="$emit('close')" class="btn btn-primary mt-4">关闭</button>
    </div>
  </div>
</template>
<script setup lang="ts">
const props = defineProps<{ errorMsg: string }>()
defineEmits(['close'])
</script>

