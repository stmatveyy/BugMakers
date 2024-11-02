from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import httpx
import uvicorn

app = FastAPI()

PROXY_URL = "http://158.160.10.254:9000/proxy/recieve" 

TOKEN = "7892983145:AAHaB6Oy_qcQcyP5CJVlDlOl0TwNo0RVq6c"

@app.post(f"/{TOKEN}/")
async def hook_send(request: Request):
    update = await request.json()

    async with httpx.AsyncClient() as client:
        response = await client.post(PROXY_URL, json=update)
    
    return JSONResponse(status_code=200, content={"response": response.json()})

if __name__ == '__main__':
    uvicorn.run("proxy_server:app",
                host="0.0.0.0",
                port=443,
                reload=True,
                ssl_keyfile="/etc/letsencrypt/live/mlbuy.ru/privkey.pem", 
                ssl_certfile="/etc/letsencrypt/live/mlbuy.ru/fullchain.pem"
                )
