import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'


export default defineConfig({
    build: {
    outDir: '../dist',
    emptyOutDir: true,
  },
  plugins: [
    vue(),
    vueDevTools(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    },
  },
  server: {
    port: 5174, // 修改前端启动端口为5174
    proxy: {
      '/generate': {
        target: 'http://0.0.0.0:8000/ai/stream-generate',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/generate/, ''),
      },
    },
  },
})
