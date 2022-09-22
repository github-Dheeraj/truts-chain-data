import json

# # convert into JSON:
# y = json.dumps(x)

# with open("./nfts/nft.json", "w") as file:
#     json.dump(x,file)
# # the result is a JSON string:
# print(y)

def createJson():
    for i in range(1,31):

        # a Python object (dict):
        x = {
        "name": "Happy International NFT day",
        "description": "This NFT Collection is a testament to how far blockchain technology has come, hold the first ever NFT dedicated to the international NFT Day. Let's take a ride across the world and its wonders with our lord pepe. No discord. No utility. Just vibes.",
        "image": "ipfs://bafybeiap6nhqzaoxys476bjeugwvznk5i5yhjaikdiccwfffatz6kxxzja/{}".format(i) + ".png",
        "edition": i
        }

        fileOne = "./nfts/{}.json"
        with open(fileOne.format(i), "w") as file:
            json.dump(x,file)
        # the result is a JSON string:
        # print(y)


def createNFTJson():
    for i in range(1,2010):

        # a Python object (dict):
        y = i %30
        print(y)
        if(y != 0):
            x = {
                "name": "Happy International NFT day",
                "description": "This NFT Collection is a testament to how far blockchain technology has come, hold the first ever NFT dedicated to the international NFT Day. Let's take a ride across the world and its wonders with our lord pepe. No discord. No utility. Just vibes.",
                "image": "ipfs://bafybeiap6nhqzaoxys476bjeugwvznk5i5yhjaikdiccwfffatz6kxxzja/{}".format(y) + ".png",
                "edition": i
            }
            fileOne = "./nftData/{}.json"
            with open(fileOne.format(i), "w") as file:
                json.dump(x,file)
        else :
            x = {
                "name": "Happy International NFT day",
                "description": "This NFT Collection is a testament to how far blockchain technology has come, hold the first ever NFT dedicated to the international NFT Day. Let's take a ride across the world and its wonders with our lord pepe. No discord. No utility. Just vibes.",
                "image": "ipfs://bafybeiap6nhqzaoxys476bjeugwvznk5i5yhjaikdiccwfffatz6kxxzja/{}".format(30) + ".png",
                "edition": i
            }
            fileOne = "./nftData/{}.json"
            with open(fileOne.format(i), "w") as file:
                json.dump(x,file)


        # fileOne = "./nftData/{}.json"
        # with open(fileOne.format(i), "w") as file:
        #     json.dump(x,file)
        # the result is a JSON string:
        # print(y)



# createJson()

createNFTJson()