import requests
from time import sleep
import asyncio
import aiohttp

# url = f"https://api.telegram.org/bot7892983145:AAHaB6Oy_qcQcyP5CJVlDlOl0TwNo0RVq6c/deleteWebhook"
# res = requests.post(url)
# print(res.json())
# while True:
#     offset = 1
#     url = f"https://api.telegram.org/bot7892983145:AAHaB6Oy_qcQcyP5CJVlDlOl0TwNo0RVq6c/getUpdates?offset={offset}timeout=5&limit=100"
#     response = requests.get(url, timeout=100)
#     print(response.json())
#     sleep(1)
#     offset += 1


async def get_telegram_updates(bot_token, offset=0):
    async with aiohttp.ClientSession() as session:
        while True:
            try:
                url = f"https://api.telegram.org/bot{bot_token}/getUpdates"
                params = {
                    "offset": offset,
                    "limit": "100",
                    "timeout": "30"
                }
                
                async with session.get(url, params=params) as response:
                    data = await response.json()
                    
                    if data['ok']:
                        for update in data['result']:
                            yield update
                        offset += len(data['result'])
                    else:
                        print(f"Ошибка: {data['description']}")
            
            except Exception as e:
                print(f"Произошла ошибка: {e}")
            
            await asyncio.sleep(0.5)  # Ожидание перед следующим запросом

async def main():
    async for update in get_telegram_updates(bot_token="7892983145:AAHaB6Oy_qcQcyP5CJVlDlOl0TwNo0RVq6c"):
        print(update)

asyncio.run(main())