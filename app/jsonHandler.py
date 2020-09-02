from flask import json

dictKeys = ["labels",
            "Overall",
            "Attack",
            "Defense",
            "Strength",
            "Hitpoints",
            "Ranged",
            "Prayer",
            "Magic",
            "Cooking",
            "Woodcutting",
            "Fletching",
            "Fishing",
            "Firemaking",
            "Crafting",
            "Smithing",
            "Mining",
            "Herblore",
            "Agility",
            "Thieving",
            "Slayer",
            "Farming",
            "Runecrafting",
            "Hunter",
            "Construction"]

keyColours = [
    "75,192,192",
    "140,38,30",
    "99,121,193",
    "13,138,88",
    "193,32,19",
    "78,99,32",
    "202,188,190",
    "21,26,191",
    "73,36,87",
    "54,124,12",
    "46,106,112",
    "130,153,176",
    "201,115,19",
    "107,80,56",
    "95,95,73",
    "87,85,68",
    "11,115,35",
    "45,50,151",
    "121,64,102",
    "77,72,70",
    "126,149,79",
    "200,143,16",
    "123,115,81",
    "143,124,92"
]


# takes a set of records, reformats them as a dictionary containing json more suitable for chartJS
def create_datasets(xpRecords):

    xpDict = {}

    for key in dictKeys:
        xpDict[key] = []

    for record in xpRecords:
        index = 0
        for key in dictKeys:
            index = index + 1

            xpDict[key].append(record[index])

    jsonList = []

    for key in xpDict:
        jsonList.append(json.dumps(xpDict[key]))

    return jsonList

def create_json_export(xpRecords):
    return json.dumps(xpRecords)