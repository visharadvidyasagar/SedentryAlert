import json
from os import path

#assests
#SUN_VALLEY_THEME = path.join("venv\Lib\site-packages\sv_ttk\sv.tcl")
SUN_VALLEY_THEME = path.join("SUNVALLEY","sv.tcl")
THEME_MODE = path.join("SUNVALLEY","theme","light.tcl")

APP_ICO = path.join("assets","app.ico")
COFFEE_ICO = path.join("assets","coffe.ico")
DOLPHIN_WAV = path.join("assets","dolphin.wav")

JSDATA: dict

#Loading json file
def load_json():
    with open("appdata.json") as jsfile:
        return json.load(jsfile)
    
#Updating JSON
def update_json(data:dict):
    