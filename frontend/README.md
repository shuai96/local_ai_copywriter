# Local AI Copywriter - 前端（Vue3）

本目录为前端项目，基于 Vue3 + Vite 构建。

## 目录结构

- src/                # 源码目录
- public/             # 公共资源
- index.html          # 入口 HTML
- env.d.ts            # 类型声明
- tsconfig.app.json   # 前端 ts 配置
- vite.config.ts      # Vite 配置

## 常用命令

```bash
npm install         # 安装依赖
npm run dev         # 启动开发服务器（默认端口 5174）
npm run build       # 打包，产物输出到 ../dist/
```

## 代理与后端联调

开发环境下，/generate 接口已代理到 FastAPI 后端（见 vite.config.ts）。

## 说明

- 产物打包后会输出到项目根目录 dist/，由后端托管静态文件。
- 其余前端配置文件已提取到项目根目录。

