<template>
  <div class="form-card">
    <h1 class="form-title">AI 文案生成器</h1>
    <p class="form-desc">快速生成高质量产品文案，支持多平台多风格</p>
    <label class="select-label" for="product_name">产品名称</label>
    <input id="product_name" v-model="form.product_name" class="input" placeholder="产品名称，如 蓝牙耳机" title="请输入产品名称" />
    <label class="select-label" for="product_features">产品卖点</label>
    <textarea id="product_features" v-model="form.product_features" class="textarea" placeholder="产品卖点，如 高清音质，佩戴舒适，续航10小时" title="请输入产品卖点" />
    <label class="select-label" for="target_audience">目标人群</label>
    <input id="target_audience" v-model="form.target_audience" class="input" placeholder="目标人群，如 上班族、学生" title="请输入目标人群" />
    <label class="select-label" for="use_scenarios">使用场景</label>
    <input id="use_scenarios" v-model="form.use_scenarios" class="input" placeholder="使用场景，如 通勤、运动" title="请输入使用场景" />
    <label class="select-label" for="tone">语气风格</label>
    <input id="tone" v-model="form.tone" class="input" placeholder="语气风格，如 专业、亲切、幽默" title="请输入语气风格" />
    <label class="select-label" for="style">文案风格</label>
    <textarea id="style" v-model="form.style" class="textarea" placeholder="文案风格，如 小红书种草风，300字" title="请输入文案风格" />
    <div class="form-row">
      <div class="select-multi-wrap">
        <label class="select-label" for="platform-select">请选择平台</label>
        <select id="platform-select" v-model="form.platform" class="select select-multi">
          <option value="通用">通用</option>
          <option value="小红书">小红书</option>
          <option value="抖音">抖音</option>
          <option value="淘宝">淘宝</option>
          <option value="京东">京东</option>
        </select>
      </div>
      <div class="select-multi-wrap">
        <label class="select-label" for="lang-select">请选择语言</label>
        <select id="lang-select" v-model="form.lang" class="select select-multi" title="请选择语言">
          <option value="zh">中文</option>
          <option value="en">英文</option>
          <option value="jp">日文</option>
        </select>
      </div>
    </div>
    <div class="form-row">
      <div class="select-multi-wrap">
        <label class="select-label" for="output_format">生成格式</label>
        <select id="output_format" v-model="form.output_format" class="select select-multi">
          <option value="text">纯文本</option>
          <option value="markdown">Markdown</option>
          <option value="html">HTML</option>
        </select>
      </div>
      <div class="select-multi-wrap">
        <label class="select-label" for="output_format">选择模型</label>
        <select id="output_format" v-model="form.model" class="select select-multi">
          <option value="">请选择模型</option>
          <option value="1">deepseek-r1:7b</option>
          <option value="2">mistral</option>
        </select>
      </div>
    </div>
    <button @click="$emit('submit')" :disabled="loading" class="btn btn-primary btn-block mt-2">
      {{ loading ? '生成中...' : '生成文案' }}
    </button>
  </div>
</template>
<script setup lang="ts">
const props = defineProps<{ form: any; loading: boolean }>()
defineEmits(['submit'])
</script>

