<template>
  <div class="output-wrap">
    <div v-if="output">
      <div class="output-main-flex">
        <div class="output-side-col">
          <div v-if="thinkOutput">
            <div class="output-card output-think-card enhanced-think-card">
              <div class="output-think-header sticky-header">
                <details class="output-think-details think-scrollable" open>
                  <summary>
                    <div class="output-think-header-left">
                      <span class="output-think-icon">💡</span>
                      <span class="output-title">模型思考</span>
                      <span class="output-think-tip">（可折叠）</span>
                    </div>
                    <div class="output-think-summary-text">点击展开/收起</div>
                  </summary>
                  <div class="output-think-content">{{ thinkOutput }}</div>
                </details>
              </div>
            </div>
          </div>
          <div v-if="contentOutput">
            <div class="output-card output-result-card enhanced-result-card">
              <div class="output-result-header output-result-header-flex">
                <span class="output-title text-blue-700">生成文案</span>
                <button class="btn btn-primary btn-copy" @click="$emit('copy', contentOutput)">
                  一键复制
                </button>
              </div>
              <pre class="output-content output-content-beauty">{{
                contentOutput
              }}</pre>
              <div class="output-pager-bar">
                <button
                  class="pager-btn"
                  :disabled="currentPage >= generatedList.length - 1"
                  @click="$emit('prev')"
                >
                  ←
                </button>
                <span class="pager-info">第{{ currentPage + 1 }}/{{ generatedList.length }}页</span>
                <button class="pager-btn" :disabled="currentPage === 0" @click="$emit('next')">
                  →
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script setup lang="ts">
defineProps<{
  output: string
  thinkOutput: string
  contentOutput: string
  generatedList: string[]
  currentPage: number
}>()
defineEmits(['copy', 'prev', 'next'])
</script>
