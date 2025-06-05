import os
import sys

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from backend.routes.stream_generate import router as ai_router

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

# 挂载 AI 路由
app.include_router(ai_router)

if __name__ == "__main__":
    import uvicorn

    port = int(os.environ.get("PORT", 8000))
    if getattr(sys, 'frozen', False):
        app.mount("/", StaticFiles(directory=get_dist_path(), html=True), name="static")
        uvicorn.run(app, host="0.0.0.0", port=port, reload=False, log_config=None)
    else:
        uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False, log_config=None)
