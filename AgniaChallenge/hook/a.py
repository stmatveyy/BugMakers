import requests
from time import sleep
# url = f"https://api.telegram.org/bot7892983145:AAHaB6Oy_qcQcyP5CJVlDlOl0TwNo0RVq6c/deleteWebhook"
# res = requests.post(url)
# print(res.json())
while True:
    offset = 1
    url = f"https://api.telegram.org/bot7892983145:AAHaB6Oy_qcQcyP5CJVlDlOl0TwNo0RVq6c/getUpdates?offset={offset}timeout=1&limit=100"
    response = requests.get(url)
    print(response.json())
    sleep(1)
    offset += 1
