from fastapi import FastAPI , Response
from starlette.responses import JSONResponse
from pydantic import BaseModel

from starlette.requests import Request

app = FastAPI()

@app.get("/health")
def get_health():
    return Response(content="Ok", status_code=200, media_type="text/plain")

