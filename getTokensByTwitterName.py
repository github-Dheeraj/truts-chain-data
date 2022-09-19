from operator import countOf
import requests
import json
import time

# get list of 
twitterNames = []
tokenListFromTwitter = []
dataToFile = []
with open("twitterNames.json", "r") as file:
    data = json.load(file)
    for line in range(0,len(data)):
        twitterNames.append(data[line])

    print("Twitter names done")

with open("coinDataFromId.json", "r") as tokenfile:
    data = json.load(tokenfile)
    for line in range(0,len(data)):
        try:
            # print('tokedetails',data[line]['links']['twitter_screen_name'])
            if data[line]['links']['twitter_screen_name'] != "":
                tokenListFromTwitter.append(data[line])
        except Exception as e:
            continue

    print('Token list done')
       



with open("tokenListFinal.json", "w") as file:
    for name in twitterNames:
        # print('name', name)
        for token in tokenListFromTwitter:
            # print('token', token['links']['twitter_screen_name'])
            if(name == token['links']['twitter_screen_name']):
                print('ok')
                dataToFile.append(token)

    print(len(twitterNames))
    print(len(tokenListFromTwitter))
    json.dump(dataToFile,file)

