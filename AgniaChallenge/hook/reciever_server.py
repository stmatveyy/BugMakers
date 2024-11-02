from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import httpx

app = FastAPI()

TOKEN = "7892983145:AAHaB6Oy_qcQcyP5CJVlDlOl0TwNo0RVq6c"

@app.post(f"/proxy/recieve")
async def hook_get(request: Request):
    update = await request.json()
    
