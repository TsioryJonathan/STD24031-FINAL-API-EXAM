from fastapi import FastAPI
from starlette.responses import JSONResponse
from pydantic import BaseModel

from starlette.requests import Request

app = FastAPI()

@app.get("/ping")
def root():
    return JSONResponse(content={"message": "pong"}, status_code=200)

