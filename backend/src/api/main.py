from api.routes.user import router as user_router
from fastapi import FastAPI, APIRouter
import uvicorn

app = FastAPI()


api = APIRouter(prefix="/api/v1")

api.include_router(user_router)

app.include_router(api)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info", access_log=True)
