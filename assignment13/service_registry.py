from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI(title="Service Registry")

# เก็บ service registry ไว้ใน memory (dict)
services: Dict[str, dict] = {
    "6610301009": {
        "name": "6610301009",
        "url": "http://localhost:8001/weather",
        "city": "Phuket,TH",
        "lat": 7.878978,
        "lon": 98.398392
    }
}


# ------------------------------
# Model
# ------------------------------
class ServiceInfo(BaseModel):
    name: str
    url: str
    city: str
    lat: float
    lon: float


# ------------------------------
# API Endpoints
# ------------------------------

@app.get("/services")
async def list_services():
    """คืนค่ารายการ service ทั้งหมดที่ register แล้ว"""
    return list(services.values())


@app.post("/register")
async def register_service(service: ServiceInfo):
    """ลงทะเบียน service ใหม่"""
    services[service.name] = service.dict()
    return {"message": f"Service {service.name} registered successfully."}


@app.put("/update")
async def update_service(service: ServiceInfo):
    """อัปเดตข้อมูล service ที่มีอยู่"""
    if service.name not in services:
        raise HTTPException(status_code=404, detail="Service not found")
    services[service.name] = service.dict()
    return {"message": f"Service {service.name} updated successfully."}


@app.delete("/unregister/{name}")
async def unregister_service(name: str):
    """ลบ service ออกจาก registry"""
    if name not in services:
        raise HTTPException(status_code=404, detail="Service not found")
    del services[name]
    return {"message": f"Service {name} unregistered successfully."}