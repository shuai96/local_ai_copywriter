from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from ollama_client import generate_text, get_memory_usage, stream_generate_text
from prompts import generate_prompt

app = FastAPI()


class CopyRequest(BaseModel):
    product_name: str
    product_features: str
    style: str
    model: int


@app.post("/ai/total-generate")
async def generate_copy(req: CopyRequest):
    print(f"""内存占用: {get_memory_usage()} GB""")
    prompt = generate_prompt(req.product_name, req.product_features, req.style)
    code, text = await generate_text(prompt, req.model)
    if code == 1:
        return {"success": True, "copy": text}
    else:
        return {"success": False, "error": text}


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
