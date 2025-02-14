import json
from os import path

#assests
#SUN_VALLEY_THEME = path.join("venv\Lib\site-packages\sv_ttk\sv.tcl")
SUN_VALLEY_THEME = path.join("SUNVALLEY\sv.tcl")

JSDATA: dict

#Loading json file
def load_json():
    with open("appdata.json") as jsfile:
        return json.load(jsfile)