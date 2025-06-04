import { ref } from 'vue'

export const form = ref({
  product_name: '耳机',
  product_features: '音质好，佩戴舒适，续航长',
  target_audience: '上班族、学生',
  use_scenarios: '通勤',
  tone: '专业',
  style: '小红书种草风，10字',
  platform: '通用',
  output_format: 'text',
  lang: 'zh',
  model: '1',
})
export const loading = ref(false)
export const output = ref('')
export const thinkOutput = ref('')
export const contentOutput = ref('')
export const generatedList = ref<string[]>([])
export const currentPage = ref(0)
export const errorMsg = ref('')

const requiredFields = [
  { key: 'product_name', label: '产品名称' },
  { key: 'product_features', label: '产品卖点' },
  { key: 'platform', label: '平台' },
]

const validateForm = () => {
  for (const field of requiredFields) {
    const value = form.value[field.key as keyof typeof form.value] as string
    if (value === undefined || value === null || value === '') {
      errorMsg.value = `${field.label}为必填项`
      return false
    }
  }
  return true
}

export const submitForm = async () => {
  if (!validateForm()) return
  output.value = ''
  thinkOutput.value = ''
  contentOutput.value = ''
  loading.value = true
  errorMsg.value = ''
  let inThink = false
  let thinkBuffer = ''
  let contentBuffer = ''
  try {
    const response = await fetch('/ai/stream-generate', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(form.value),
    })
    if (!response.body) throw new Error('No response body')
    const reader = response.body.getReader()
    const decoder = new TextDecoder('utf-8')
    while (true) {
      const { done, value } = await reader.read()
      if (done) break
      const chunk = decoder.decode(value, { stream: true })
      output.value += chunk
      let temp = chunk
      while (temp.length > 0) {
        if (!inThink) {
          const thinkStart = temp.indexOf('<think>')
          if (thinkStart !== -1) {
            contentBuffer += temp.slice(0, thinkStart)
            contentOutput.value = contentBuffer.trim()
            temp = temp.slice(thinkStart + 7)
            inThink = true
          } else {
            contentBuffer += temp
            contentOutput.value = contentBuffer.trim()
            temp = ''
          }
        } else {
          const thinkEnd = temp.indexOf('</think>')
          if (thinkEnd !== -1) {
            thinkBuffer += temp.slice(0, thinkEnd)
            thinkOutput.value = thinkBuffer.trim()
            temp = temp.slice(thinkEnd + 8)
            inThink = false
          } else {
            thinkBuffer += temp
            thinkOutput.value = thinkBuffer.trim()
            temp = ''
          }
        }
      }
    }
    contentOutput.value = contentBuffer.trim()
    thinkOutput.value = thinkBuffer.trim()
    if (contentOutput.value) {
      generatedList.value.unshift(contentOutput.value)
      currentPage.value = 0
    }
  } catch (_err) {
    errorMsg.value = '生成失败，请检查后端服务或网络：' + _err
  } finally {
    loading.value = false
  }
}

export function prevPage() {
  if (currentPage.value < generatedList.value.length - 1) {
    currentPage.value++
    contentOutput.value = generatedList.value[currentPage.value]
  }
}
export function nextPage() {
  if (currentPage.value > 0) {
    currentPage.value--
    contentOutput.value = generatedList.value[currentPage.value]
  }
}
export function copyText(text: string) {
  navigator.clipboard.writeText(text)
}

