import logging

from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from backend.models import GenerateRequest
from backend.services import get_memory_usage, stream_generate_text
from backend.utils import build_prompt

router = APIRouter()

@router.post("/ai/stream-generate")
async def stream_generate_copy(request: GenerateRequest):
    logging.info(f"内存占用: {get_memory_usage()} GB")
    prompt = build_prompt(request.model_dump())
    return StreamingResponse(
        stream_generate_text(prompt, request.model, True),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache"}
    )

