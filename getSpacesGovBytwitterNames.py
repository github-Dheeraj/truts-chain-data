from operator import countOf
import requests
import json
import time

# get list of 
twitterNames = []
spaceListFromTwitter = []
dataToFile = []
with open("twitterNames.json", "r") as file:
    data = json.load(file)
    for line in range(0,len(data)):
        twitterNames.append(data[line])

    print("Twitter names done")

with open("allSpacesSnapshot.json", "r") as tokenfile:
    data = json.load(tokenfile)
    space = data['data']['spaces']
    # print('len spaces', space[1]['twitter'])
    for count in range(0,len(space)):
        try:
            if space[count]['twitter'] != None:
                spaceListFromTwitter.append(space[count])
        except Exception as e:
            continue
    
    print('length of total space',spaceListFromTwitter[5]['twitter'])
    print('Token list done')
       



with open("spacesListFinal.json", "w") as file:
    for name in twitterNames:
        # print('name', name)
        for token in spaceListFromTwitter:
            # print('token', token['links']['twitter_screen_name'])
            if ( token['twitter'] != ""):
                if(name == token['twitter']):
                    dataToFile.append(token)

    print(len(twitterNames))
    print(len(dataToFile))
    json.dump(dataToFile,file)

