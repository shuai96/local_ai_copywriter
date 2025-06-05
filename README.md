# Local AI Copywriter

本项目为本地 AI 文案生成工具，包含前端（Vue3）和后端（FastAPI）两部分，支持流式文案生成、多模型选择、内存监控等功能。

## 目录结构

- frontend/         # 前端 Vue3 项目
- backend/          # 后端 FastAPI 项目
- main.py           # 后端启动入口
- requirements.txt  # 后端依赖

## 后端 backend 结构

- models/           # 数据模型
- routes/           # 路由
- services/         # 业务逻辑/服务
- utils/            # 工具函数、日志配置

## 启动方式

1. 安装依赖

```bash
pip install -r requirements.txt
```

2. 启动后端

```bash
python main.py
```

3. 启动前端（进入 frontend 目录）

```bash
npm install
npm run dev
```

## 打包说明

- 后端支持 PyInstaller 打包，详见 backend/README.md
- 前端支持 Vite 构建
