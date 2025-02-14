import json


#Loading json file
def load_json():
    with open("appdata.json") as jsfile:
        return json.load(jsfile)