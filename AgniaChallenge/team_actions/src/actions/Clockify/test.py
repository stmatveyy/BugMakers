import requests


def workspaceToId(workspaceName):
    response = requests.get(
        f"https://api.clockify.me/api/v1/workspaces",
        headers={"X-Api-Key": "NDU3NDMxY2EtYzY0Yi00MjBiLWFhNDItMzY1ODk1YjlkNmE2"},
    )

    needed_workspace = [sp for sp in response.json() if sp["name"] == workspaceName][0]

    needed_ws_id = needed_workspace
    return needed_ws_id


print(workspaceToId("общее"))
