# ---- 基于 Ollama 官方镜像 ----
#FROM ollama/ollama:latest AS ollama

# 拉取 deepseek-r1:7b 模型
# RUN ollama pull deepseek-r1:7b

# ---- 构建后端镜像 ----
FROM python:3.11-slim AS backend

WORKDIR /app

# 安装依赖
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制后端代码
COPY main.py .
COPY backend ./backend

# ---- 构建前端静态文件----
FROM node:20 AS frontend
WORKDIR /frontend
COPY package.json package-lock.json* tsconfig.json* tsconfig.node.json* postcss.config.js tailwind.config.js ./
COPY frontend/. ./
RUN npm install && npm run build-only --workspace-root -- --config vite.config.ts

# ---- 生产镜像 ----
FROM python:3.11-slim

WORKDIR /app

# 安装ollama和curl
#RUN apt-get update && apt-get install -y curl \
#    && curl --retry 5 --retry-delay 5 -fsSL -o /tmp/ollama_install.sh https://ollama.com/install.sh \
#    && sh /tmp/ollama_install.sh
# 用pip安装supervisor
RUN pip install supervisor

# 拷贝后端
COPY --from=backend /app /app

# 拷贝前端静态文件
COPY --from=frontend /dist ./dist

# 拷贝supervisord配置
COPY supervisord.conf /etc/supervisord.conf

EXPOSE 8000
# EXPOSE 11434  # 11434 端口仅容器内部使用，无需暴露到外部

CMD ["supervisord", "-c", "/etc/supervisord.conf"]

