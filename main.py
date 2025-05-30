from typing import Optional
import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from ollama_client import get_memory_usage, stream_generate_text
from prompts import build_prompt
from logging_config import setup_logging

setup_logging()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "https://local-ai-copywriter-web.onrender.com"],
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
    import os
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)

