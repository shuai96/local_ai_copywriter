<template>
  <div class="app-bg">
    <div class="app-container">
      <div v-if="!output" class="form-center-row">
        <CopyForm :form="form" :loading="loading" @submit="submitForm" />
      </div>
      <div v-else class="app-main-row">
        <CopyForm :form="form" :loading="loading" @submit="submitForm" />
        <CopyOutput
          :output="output"
          :thinkOutput="thinkOutput"
          :contentOutput="contentOutput"
          :generatedList="generatedList"
          :currentPage="currentPage"
          @copy="copyText"
          @prev="prevPage"
          @next="nextPage"
        />
      </div>
      <ErrorModal :errorMsg="errorMsg" @close="errorMsg = ''" />
    </div>
  </div>
</template>

<script setup lang="ts">
import CopyForm from '../components/CopyForm.vue'
import CopyOutput from '../components/CopyOutput.vue'
import ErrorModal from '../components/ErrorModal.vue'
import {
  contentOutput,
  copyText,
  currentPage,
  errorMsg,
  form,
  generatedList,
  loading,
  nextPage,
  output,
  prevPage,
  submitForm,
  thinkOutput,
} from '../App.logic'
</script>
