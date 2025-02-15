import json
from os import path
from time import sleep

import winsound
from win10toast import ToastNotifier

toaster = ToastNotifier()

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
    with open("appdata.json","w") as jsfile:
        json.dump(data, jsfile, indent=2)

#notifier funtion
def _notify(
        msg, icon=COFFEE_ICO, title=None, soundfile=DOLPHIN_WAV
):
    toaster.show_toast(
        title=title if title else "Notification",
        msg=msg,
        icon_path=icon,
        threaded=True #for not interupting python or main thread
    )

    if soundfile:
        winsound.PlaySound(soundfile, flags=winsound.SND_FILENAME)

def sed_alert():
    dt=load_json()
    if dt['sedentary_alert']:
        interval_secs = dt['interval'] * 60
        sleep(interval_secs)

        _notify(
            msg="Have a Break, Have a KitKat"
        )

        sed_alert()
