# Local AI Copywriter - 后端（FastAPI）

本目录为后端核心代码，基于 FastAPI 框架，支持流式文案生成。

## 目录结构

- models/           # 数据模型
- routes/           # 路由
- services/         # 业务逻辑/服务（如 ollama_client.py）
- utils/            # 工具函数、日志配置（如 prompts.py, logging_config.py）
- README.md         # 本说明文件

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
详见根目录 README.md
