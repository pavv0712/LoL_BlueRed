import json


def LoadJson():
    with open('BlueRed.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        print(data) 


LoadJson()
