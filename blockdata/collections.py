
import time
import ubiquity.ubiquity_openapi_client
from ubiquity.ubiquity_openapi_client.api import nft_api
from ubiquity.ubiquity_openapi_client.model.get_collection_response import GetCollectionResponse
from pprint import pprint
import requests
import json

configuration = ubiquity.ubiquity_openapi_client.Configuration(
    host = "https://ubiquity.api.blockdaemon.com/v1"
)

# Configure Bearer authorization (Opaque): bearerAuth
configuration = ubiquity.ubiquity_openapi_client.Configuration(
    access_token = 'wWdleHEnNX5caGWzMW2Z9WoycnegLlrbE9tJhPAHjBQBJ8o2'
)

# # Enter a context with an instance of the API client
# with ubiquity.ubiquity_openapi_client.ApiClient(configuration) as api_client:
#     # Create an instance of the API class
#     api_instance = nft_api.NFTApi(api_client)
#     protocol = "ethereum" # str | Coin platform handle
#     network = "mainnet" # str | Which network to target
#     contract_address = [
#         "contractAddress_example",
#     ] # [str] | Mapped to URL query parameter 'contract_address' (optional)
#     collection_name = [
#         "collectionName_example",
#     ] # [str] | Mapped to URL query parameter 'collection_name' (optional)
#     sort_by = "sort_by_example" # str | Sort by one of: name (optional)
#     order = "order_example" # str | Mapped to URL query parameter `order` One of: asc, desc (optional)
#     page_size = 1 # int | Mapped to URL query parameter `page_size` (optional)
#     page_token = "page_token_example" # str | Mapped to URL query parameter `page_token` base64 encoded cursor (optional)
#     verified = True 
#     # example passing only required values which don't have defaults set
#     try:
#         api_response = api_instance.explorer_list_collections(protocol, network)
#         pprint(api_response)
#     except ubiquity.ubiquity_openapi_client.ApiException as e:
#         print("Exception when calling NFTApi->explorer_list_collections: %s\n" % e)

#     # example passing only required values which don't have defaults set
#     # and optional values

#     try:
#         # api_response = api_instance.explorer_list_collections(protocol, network, contract_address=contract_address, collection_name=collection_name, sort_by=sort_by, order=order, page_size=page_size, page_token=page_token,verified=verified)
#         api_response = api_instance.explorer_list_collections(protocol, network,  page_size=page_size,verified=verified)
#         pprint(api_response)
#     except ubiquity.ubiquity_openapi_client.ApiException as e:
#         print("Exception when calling NFTApi->explorer_list_collections: %s\n" % e)


dataToFile = []

endpoint = "https://svc.blockdaemon.com/nft/v1/ethereum/mainnet/collections"
# https://svc.blockdaemon.com/nft/v1/ethereum/mainnet/collections?verified=true&token_type=ERC721&page_size=100

params = {"verified": "True", "token_type": "ERC721", "page_size": "100", "page_token": ""}
headers = {"Authorization": "Bearer wWdleHEnNX5caGWzMW2Z9WoycnegLlrbE9tJhPAHjBQBJ8o2"}



okRequest = requests.get(endpoint, params = params, headers=headers).json()

for item in okRequest["data"]:
    dataToFile.append(item)
params["page_token"] = okRequest["meta"]["paging"]["next_page_token"]

def getcollectionData():
    okRequest = requests.get(endpoint, params = params, headers=headers).json()
    for item in okRequest["data"]:
        dataToFile.append(item)
    params["page_token"] = okRequest["meta"]["paging"]["next_page_token"]
    print (okRequest["meta"]["paging"]["next_page_token"])


while params["page_token"] != "":
    getcollectionData()



with open("dataCollection1.json", "w") as file:
    json.dump(dataToFile,file)

