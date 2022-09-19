import requests
import json
import time

# get list of 
lis = []
dataToFile = []
with open("totalCoinIds.json", "r") as file:
    data = json.load(file)
    for line in data:
        lis.append(line)

for item in lis:
    resp = requests.get('https://api.coingecko.com/api/v3/coins/'+ item +'?localization=false&tickers=false&market_data=false&community_data=true&developer_data=false&sparkline=false')
    time.sleep(1)
    print(item)
    dataToFile.append(resp.json())


with open("coinDataFromId.json", "w") as file:
    json.dump(dataToFile,file)

