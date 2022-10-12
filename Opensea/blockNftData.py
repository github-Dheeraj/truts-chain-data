import time
import ubiquity
from ubiquity.api import blocks_api

conf = ubiquity.Configuration(
    access_token="<token>"
)

with ubiquity.ApiClient(conf) as client:
    blocks_api_instance = blocks_api.BlocksApi(client)
    platform = "ethereum"
    network = "mainnet"

    block = blocks_api_instance.get_block(platform, network, "current")

from pprint import pprint
