# Local AI Copywriter - 后端（FastAPI）

本目录为后端核心代码，基于 FastAPI 框架，支持流式文案生成。

## 目录结构

- logging_config.py   # 日志配置
- ollama_client.py   # Ollama API 客户端与流式生成逻辑
- prompts.py         # 提示词构建逻辑
- __init__.py        # 包初始化文件

## 主要功能

- 提供 /ai/stream-generate 接口，支持流式生成文案
- 支持多模型选择、内存监控、异常调试
- 日志级别可通过环境变量 LOG_LEVEL 配置

## 依赖安装

请在项目根目录下执行：

```bash
pip install -r requirements.txt
```

## 启动方式

开发环境：
```bash
python main.py
```

PyInstaller 打包后：
```bash
./main.exe
```

## 说明

- main.py 为后端启动入口，已自动适配源码/打包两种环境
- 静态文件（前端打包产物）默认托管于 dist/ 目录
- 详细接口与参数见 main.py 及 prompts.py

