import path from 'node:path'
import {defineConfig} from 'vite'
import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'

export default defineConfig({
  root: __dirname,
  plugins: [
    vue(),
    vueDevTools(),
  ],
  build: {
    outDir: '../dist',
    emptyOutDir: true,
  },
  resolve: {
    alias: {
      '@': path.resolve(__dirname, 'src')
    },
  },
  server: {
    port: 5174,
    proxy: {
      '/ai/stream-generate': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true
      },
    },
  },
})
