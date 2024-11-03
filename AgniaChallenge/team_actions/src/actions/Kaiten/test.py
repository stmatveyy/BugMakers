import requests as rq


response = rq.post(
        "https://ramzanhac2005.kaiten.ru/api/latest/spaces",
        headers={"Authorization": f"Bearer a93ac0b1-c4be-42e5-a59e-ff514b0e279b"},
        json={"title": "e", "external_id": None},
    )

response.raise_for_status()
data = response.json()
print(data)