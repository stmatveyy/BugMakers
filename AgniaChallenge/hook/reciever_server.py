from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import httpx
import uvicorn

app = FastAPI()

TOKEN = "7892983145:AAHaB6Oy_qcQcyP5CJVlDlOl0TwNo0RVq6c"


@app.post(f"/hook/recieve")
async def hook_get(request: Request):
    update = await request.json()
    print(update)


if __name__ == "__main__":
    uvicorn.run("reciever_server:app", host="0.0.0.0", port=8080, reload=True)
