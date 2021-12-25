import requests

def GetEvents():

    url = "https://api.opensea.io/api/v1/events?only_opensea=false&offset=0&limit=20"

    headers = {"Accept": "application/json"}

    response = requests.request("GET", url, headers=headers)
    file = open("sampleevents.txt", 'w')
    print(response.text)

def GetAssets():
    url = "https://api.opensea.io/api/v1/assets?owner=0x047f3853f3d89e5a61344749519de7a66fd4f9c4&asset_contract_address=0x1a2F71468F656E97c2F86541E57189F59951efe7&order_direction=desc&offset=0&limit=20"

    response = requests.request("GET", url)
    test = response.json()["assets"][1]["traits"]
    file = open("sampleassets.txt", 'w')
    file.write(str(response.json()["assets"][1]["traits"]))
    print(response.json())

if __name__ == "__main__":
    GetAssets()
    GetEvents()