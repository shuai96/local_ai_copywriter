# Local AI Copywriter 项目总览

本项目为前后端分离的 AI 文案生成工具，后端基于 FastAPI，前端基于 Vue3 + Vite。

---

## 目录结构

```
local_ai_copywriter/
├── backend/           # 后端核心代码（FastAPI）
│   ├── logging_config.py
│   ├── ollama_client.py
│   ├── prompts.py
│   └── README.md
├── frontend/          # 前端核心代码（Vue3 + Vite）
│   ├── src/
│   ├── public/
│   ├── index.html
│   ├── env.d.ts
│   ├── tsconfig.app.json
│   ├── vite.config.ts
│   └── README.md
├── dist/              # 前端打包产物，后端托管静态文件
├── main.py            # FastAPI 启动入口
├── requirements.txt   # Python 依赖
├── package.json       # 前端依赖
├── ...                # 其他配置文件
```

---

## 快速开始

### 1. 后端（FastAPI）

```bash
pip install -r requirements.txt
python main.py
```

### 2. 前端（Vue3 + Vite）

```bash
npm install
npm run dev      # 启动开发服务器，默认端口 5174
npm run build    # 打包产物输出到 dist/
```

---

## 主要功能
- AI 文案流式生成，支持多模型
- 前后端分离，接口联调便捷
- 支持本地和云端部署

---

## 相关文档
- backend/README.md  —— 后端详细说明
- frontend/README.md —— 前端详细说明

---

如有问题请查阅各子目录 README 或联系开发者。

