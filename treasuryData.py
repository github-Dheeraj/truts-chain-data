from asyncio import constants
import requests
import json

protocolData = requests.get('https://api.boardroom.info/v1/protocols/aave')

fileName = 'aave.json'
 
with open(fileName, 'w') as file_object:
    json.dump([protocolData.json()["data"]], file_object)

def save_to_file(user_data):
    with open('aave.json', 'w+') as jfile:
        okdata = json.load(jfile)     #Read content
        okdata.append(user_data)
        print("take me to uniswap: ",okdata) 
        # jfile.seek(0)
        json.dump(okdata, jfile, indent=4)      #Append 
#   #  with open('aave.json', 'w') as jfile:
#   #      json.dump(data, jfile, indent=2)     #Write back



# y = {"emp_name":"Nikhil",
#      "email": "nikhil@geeksforgeeks.org",
#      "job_profile": "Full Time"
#     }
protocolDataUni = requests.get('https://api.boardroom.info/v1/protocols/uniswap')
#json.dumps(protocolData.json())
save_to_file(protocolDataUni.json()["data"])
# print(protocolData.json())
# print(protocolDataUni.json())


