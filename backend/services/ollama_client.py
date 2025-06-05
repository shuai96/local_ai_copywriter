import json
import socket
import logging
from typing import Literal, AsyncGenerator, Any

import httpx
import psutil
from pydantic import BaseModel, Field

OLLAMA_URL = "http://localhost:11434/api/generate"
ModelType = Literal[1, 2]
model_mapping = {
    "1": "deepseek-r1:7b",
    "2": "mistral"
}

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class GenerationConfig(BaseModel):
    model: str = Field(..., min_length=2)
    prompt: str = Field(..., min_length=1)
    stream: bool = Field(False)
    temperature: float = Field(0.7, ge=0.0, le=1.0)

async def stream_generate_text(
        prompt: str,
        model: str = "1",
        is_stream: bool = False,
        timeout: float = 300.0,
        temperature: float = 0.7) -> AsyncGenerator[bytes | Any, None]:
    try:
        model_name = model_mapping.get(model, "deepseek-r1:7b")
        payload = GenerationConfig(
            model=model_name,
            prompt=prompt,
            stream=is_stream,
            temperature=temperature
        ).model_dump()
        async with httpx.AsyncClient(timeout=timeout) as client:
            async with client.stream('POST', OLLAMA_URL, json=payload) as response:
                response.raise_for_status()
                async for chunk in response.aiter_lines():
                    if chunk.strip():
                        data = json.loads(chunk)
                        if text := data.get("response", ""):
                            yield text.encode('utf-8')
    except Exception as e:
        logging.error(f"""
               ||======== 深度调试信息 ========||
               错误类型: {type(e).__name__}
               详细信息: {str(e)}
               服务器状态: {"运行中" if is_port_open(11434) else "未响应"}
               内存占用: {get_memory_usage()} MB
               ||==============================||
               """)
        yield f"❌ 生成中断：{str(e)}".encode('utf-8')

def is_port_open(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0

def get_memory_usage():
    return psutil.virtual_memory().used // 1024 // 1024 // 1024

