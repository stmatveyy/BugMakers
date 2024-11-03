import requests

res = requests.get(
    "https://todoist://labels",
)

# Проверьте статус ответа
print("Status Code:", res.status_code)
print("Response Text:", res.text)  # Выводим текст ответа

try:
    print(res.json())
except ValueError:
    print("Response is not in JSON format.")
