import requests as rq

URL = "https://matvey-22.kaiten.ru/api/latest"

res = rq.post(
    URL + f"/spaces/476816/boards",
    headers={"Authorization": f"Bearer 2adf6abb-5aff-4202-9065-74fbb9ddbef1"},
    json={
        "title": "GGGGGGGGGGGGGGGGGGGGGGGGGGGG",
        "type": "1",
        "columns": [{"col_count": 1, "title": "Очередь", "type": 1, "sort_order": 1}],
        "lanes": [{"row_count": 1, "title": "", "sort_order": 1}],
    },
)

print(res.json())


def SpaceNameToId(auth, spaceName):
    spaces = rq.get(URL + "/spaces", headers={"Authorization": f"Bearer {auth}"}).json()

    try:
        sp_id = [sp for sp in spaces if sp["title"] == spaceName][0]["id"]

    except IndexError:
        return ({"reason": "Space not found"}, None)

    return (None, sp_id)


print(
    SpaceNameToId(
        auth="2adf6abb-5aff-4202-9065-74fbb9ddbef1", spaceName="Первое пространство"
    )
)
