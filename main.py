import time

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from ollama_client import generate_text, get_memory_usage, stream_generate_text
from prompts import generate_prompt

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class CopyRequest(BaseModel):
    product_name: str
    product_features: str
    style: str
    model: int


@app.post("/ai/total-generate")
async def generate_copy(req: CopyRequest):
    start_time = time.time()
    print(f"内存占用: {get_memory_usage()} GB")
    prompt = generate_prompt(req.product_name, req.product_features, req.style)
    code, text = await generate_text(prompt, req.model)
    elapsed = time.time() - start_time
    print(f"接口执行耗时: {elapsed:.2f} 秒")
    if code == 1:
        print(f"""生成内容: {text}""")
        return {"success": True, "result": text, "elapsed": elapsed}
    else:
        print(f"""错误信息: {text}""")
        return {"success": False, "result": text, "elapsed": elapsed}


@app.post("/ai/stream-generate")
async def stream_generate_copy(req: CopyRequest):
    print(f"""内存占用: {get_memory_usage()} GB""")
    prompt = generate_prompt(req.product_name, req.product_features, req.style)
    """流式生成API接口"""
    return StreamingResponse(
        stream_generate_text(prompt, req.model, True),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache"}
    )
