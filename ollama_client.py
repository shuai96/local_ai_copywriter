import json
import socket
import logging
from typing import Literal, AsyncGenerator, Any

import httpx
import psutil
from pydantic import BaseModel, Field

# 常量定义增强
OLLAMA_URL = "http://localhost:11434/api/generate"
# 明确定义可选的模型类型
ModelType = Literal[1, 2]
# 模型映射配置
model_mapping = {
    "1": "deepseek-r1:7b",
    "2": "mistral"
}

# 配置日志输出
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# 使用Pydantic模型验证请求参数
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
    """流式文本生成核心逻辑

    Args:
        prompt: 输入提示词
        model: 模型选择（1=deepseek-r1:7b, 2=mistral）
        timeout: 超时时间（秒）
        temperature: 控制生成效果;低值（接近0）：确定性高，适合事实性问题 / 高值（接近1）：创造性更强，适合故事生成
        is_stream: 是否启用流式传输

    Yields:
        实时生成的文本片段（UTF-8编码）
    """

    try:
        # 获取模型名称，使用映射配置
        model_name = model_mapping.get(model, "deepseek-r1:7b")

        payload = GenerationConfig(
            model=model_name,
            prompt=prompt,
            stream=is_stream,
            temperature=temperature  # 使用传入值或默认值
        ).model_dump()

        async with httpx.AsyncClient(timeout=timeout) as client:
            async with client.stream('POST', OLLAMA_URL, json=payload) as response:
                response.raise_for_status()
                # 逐行解析流式数据
                async for chunk in response.aiter_lines():
                    if chunk.strip():
                        # 直接解析 chunk 为 JSON，无需创建 Response 对象
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
