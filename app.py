from tkinter import Tk, ttk, StringVar, IntVar

from _app import *

#Loading JSDATA
JSDATA= load_json()

App = Tk()
App.title("Sedentary Alert")
App.iconbitmap(APP_ICO)
App.resizable(False, False) #for both x,y axis

App.tk.call("source",SUN_VALLEY_THEME)
#App.tk.call("set_theme",THEME_MODE)

#ussr interface
frame = ttk.Frame(App, padding=10)
frame.grid(row=0, column=0, padx=10, pady=10)

#checkbutton, if checked 1, else 0, in the frame
sedentary_alert = IntVar() #for notifications

sedentary_alert.set(
    1 if JSDATA["sedentary_alert"] else 0
)
def toggle_sed_alert():
    JSDATA["sedentary_alert"] = bool(sedentary_alert.get())
    update_json(JSDATA)

sed_check = ttk.Checkbutton(
    frame, variable = sedentary_alert,
    text = "Sedentary Alert", command=toggle_sed_alert
)
sed_check.grid(row=0, column=0, columnspan=2, pady=5)

#dropdown
sed_lbl = ttk.Label(frame, text="interval")
sed_lbl.grid(row=1, column=0, pady=10)

interval_options=["15 Mins","20 Mins","30 Mins","40 Mins"] #dropdown array
interval_period= StringVar()


#dropdown menu
def intevral_change(interval: str):
    JSDATA["interval"] = int(interval.split()[0])
    update_json(JSDATA)

interval_dropdown=ttk.OptionMenu(
    frame, interval_period, "Select", *interval_options,
    command=intevral_change
)
interval_dropdown.grid(row=1, column=1, pady=5, padx=(10,0))

interval_period.set(
    f"{JSDATA['interval']} Min"
)

#For running window
App.mainloop()