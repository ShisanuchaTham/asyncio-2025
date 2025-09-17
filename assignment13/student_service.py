import os
import httpx
import asyncio
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# อ่านค่าจาก .env
OWM_API_KEY = os.getenv("OWM_API_KEY")
CITY = os.getenv("CITY")
LAT = os.getenv("LAT")
LON = os.getenv("LON")
SERVICE_REGISTRY_URL = os.getenv("SERVICE_REGISTRY_URL")
STUDENT_NAME = os.getenv("STUDENT_NAME")
SELF_URL = os.getenv("SELF_URL")

# ------------------------------
# Models
# ------------------------------
class ServiceInfo(BaseModel):
    name: str
    url: str
    city: str
    lat: float
    lon: float

# ------------------------------
# Endpoints
# ------------------------------
@app.get("/weather")
async def get_weather():
    async with httpx.AsyncClient() as client:
        url = f"http://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={OWM_API_KEY}&units=metric"
        resp = await client.get(url)
        return resp.json()

@app.get("/aggregate")
async def aggregate_weather():
    async with httpx.AsyncClient() as client:
        services = (await client.get(f"{SERVICE_REGISTRY_URL}/services")).json()
        tasks = [client.get(f"{s['url']}") for s in services]
        responses = await asyncio.gather(*tasks, return_exceptions=True)
        return [r.json() if hasattr(r, "json") else str(r) for r in responses]

@app.post("/register_self")
async def register_self():
    info = {
        "name": STUDENT_NAME,
        "url": SELF_URL,
        "city": CITY,
        "lat": LAT,
        "lon": LON
    }
    async with httpx.AsyncClient() as client:
        return (await client.post(f"{SERVICE_REGISTRY_URL}/register", json=info)).json()

@app.put("/update_self")
async def update_self():
    info = {"url": SELF_URL}
    async with httpx.AsyncClient() as client:
        return (await client.put(f"{SERVICE_REGISTRY_URL}/update", json=info)).json()

@app.delete("/unregister_self")
async def unregister_self():
    async with httpx.AsyncClient() as client:
        return (await client.delete(f"{SERVICE_REGISTRY_URL}/unregister/{STUDENT_NAME}")).json()
