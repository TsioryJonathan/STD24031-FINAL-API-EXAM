import json
from fastapi import FastAPI, Request
from starlette.responses import Response
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List

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

phoneList: List[PhoneModel] = []

def serializedPhoneList():
    phones_converted = []
    for phone in phoneList:
       toAdd = {
              "id": phone.id,
              "brand": phone.brand,
              "model": phone.model,
              "characteristics": {
                "ram_memory": phone.characteristics.ram_memory,
                "rom_memory": phone.characteristics.rom_memory
              }
       }
       phones_converted.append(toAdd)
    return phones_converted



@app.post("/phones")
def create_phone(payload: List[PhoneModel]):
    for phone in payload:
        phoneList.append(phone)
    return JSONResponse(
        content={"phones": serializedPhoneList()},
        status_code=200
    )

@app.get("/phones")
def list_phones():
    return JSONResponse(
        content={"phones": serializedPhoneList()},
        status_code=200
    )

@app.get("/phones/{id}")
def get_phone(id: str):
    for phone in phoneList:
        if phone.id == id:
            return JSONResponse(
                content={"phone": phone.model_dump()},
                status_code=200
            )
    return JSONResponse(
        content={"message": "Phone not found"},
        status_code=404
    )
    
@app.put("/phones/{id}/characteristics")
def modify_characteristics(newCharacteristics: Characteristics, id: str):
    for phone in phoneList:
        if phone.id == id:
            phone.characteristics = newCharacteristics
            return JSONResponse(
                content={"phone": phone.model_dump()},
                status_code=200
            )
    return JSONResponse(
        content={"message": "Phone not found"},
        status_code=404
    )