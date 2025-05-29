from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# 导入路由
from app.routers.files import router as files_router
from app.routers.submissions import router as submissions_router

app = FastAPI(title="试题自动批改系统", version="1.0")

# 允许跨域请求（开发阶段）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 注册路由
app.include_router(files_router)
app.include_router(submissions_router)

@app.get("/")
def read_root():
    return {"message": "欢迎使用试题自动批改系统 API"}