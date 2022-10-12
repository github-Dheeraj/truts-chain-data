
import time
import ubiquity.ubiquity_openapi_client
from ubiquity.ubiquity_openapi_client.api import nft_api
from ubiquity.ubiquity_openapi_client.model.get_collection_response import GetCollectionResponse
from pprint import pprint
import requests
import json



Contractlis = []
dataToFile = []
with open("dataCollection1.json", "r") as file:
    data = json.load(file)
    for line in range(1,2085):
        Contractlis.append(data[line]["contracts"][0])


# for item in Contractlis:
#     print("item", item)

dataToFile = []

#  Gives collecton Info
endpoint = "https://svc.blockdaemon.com/nft/v1/ethereum/mainnet/collection/"
# https://svc.blockdaemon.com/nft/v1/ethereum/mainnet/collections?verified=true&token_type=ERC721&page_size=100

params = {"contract_address" : ""}
headers = {"Authorization": "Bearer wWdleHEnNX5caGWzMW2Z9WoycnegLlrbE9tJhPAHjBQBJ8o2"}

def getcollectionData():
    for item in Contractlis:
        print(item)
        params["contract_address"] = item
        okRequest = requests.get(endpoint, params = params, headers=headers).json()
        dataToFile.append(okRequest)

getcollectionData()


with open("okdokey.json", "w") as file:
    json.dump(dataToFile,file)

print("Done!")

# get Owners of A collection
# import requests

# url = "https://eth-mainnet.g.alchemy.com/nft/v2/demo/getOwnersForCollection"

# headers = {"accept": "application/json"}

# response = requests.get(url, headers=headers)

# print(response.text)


# Get All Nfts of Collection
# import requests

# url = "https://eth-mainnet.g.alchemy.com/nft/v2/demo/getNFTsForCollection"

# headers = {"accept": "application/json"}

# response = requests.get(url, headers=headers)

# print(response.text)
