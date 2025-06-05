/// <reference types="vite/client" />

interface ImportMetaEnv {
  readonly BASE_URL: string
  // 你可以在这里添加更多环境变量声明
}

interface ImportMeta {
  readonly env: ImportMetaEnv
}

