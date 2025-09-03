from fastapi import FastAPI , Response
from starlette.responses import JSONResponse
from pydantic import BaseModel
from typing import List

from starlette.requests import Request

app = FastAPI()

@app.get("/health")
def get_health():
    return Response(content="Ok", status_code=200, media_type="text/plain")

class Characteristics(BaseModel):
    ram_memory: int
    rom_memory: int
class PhoneModel(BaseModel):
    id: str
    brand: str
    model: str
    characteristics: Characteristics

phoneList: List[PhoneModel] = [{
        "id":1,
        "brand":"Apple",
        "model":"iPhone 13",
        "characteristics":{
            "ram_memory:" : 4,
            "rom_memory:" : 128,
        }
    }]

def serializedPhoneList():
    phones_converted = []
    for phone in phoneList:
        phones_converted.append(phone.model_dump())
    return phones_converted

@app.post("/phones")
def create_phone(phones: List[PhoneModel]):
    for phone in phones:
        phoneList.append(phone)
    return JSONResponse(
        content={"phones": serializedPhoneList()},
        status_code=200
    )
    