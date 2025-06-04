import logging
import os
import sys
from typing import Optional

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from backend.logging_config import setup_logging
from backend.ollama_client import get_memory_usage, stream_generate_text
from backend.prompts import build_prompt

setup_logging()

app = FastAPI()


# 兼容 PyInstaller 打包和源码运行的静态文件路径
def get_dist_path():
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, 'dist')
    return os.path.abspath('dist')




app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5174", "https://local-ai-copywriter-web.onrender.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# 请求模型
class GenerateRequest(BaseModel):
    product_name: str
    product_features: str
    target_audience: Optional[str] = ""
    use_scenarios: Optional[str] = ""
    tone: Optional[str] = ""
    style: Optional[str] = ""
    platform: str = "通用"
    output_format: Optional[str] = "text"
    lang: Optional[str] = "zh"
    model: Optional[str] = None  # 新增模型字段，便于流式接口使用


@app.post("/ai/stream-generate")
async def stream_generate_copy(request: GenerateRequest):
    logging.info(f"内存占用: {get_memory_usage()} GB")
    prompt = build_prompt(request.model_dump())  # 传递 dict 以兼容 prompts.py，修正弃用警告
    """流式生成API接口"""
    return StreamingResponse(
        stream_generate_text(prompt, request.model, True),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache"}
    )


if __name__ == "__main__":
    import uvicorn

    port = int(os.environ.get("PORT", 8000))
    if getattr(sys, 'frozen', False):
        # 挂载前端静态文件
        app.mount("/", StaticFiles(directory=get_dist_path(), html=True), name="static")
        # 打包环境，直接传app对象
        uvicorn.run(app, host="0.0.0.0", port=port, reload=False, log_config=None)
    else:
        # 源码环境，使用字符串
        uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False, log_config=None)
