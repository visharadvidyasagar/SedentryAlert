from tkinter import Tk, ttk, StringVar, IntVar

from _app import *

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
sed_check = ttk.Checkbutton(
    frame, variable = sedentary_alert,
    text = "Sedentary Alert"
)
sed_check.grid(row=0, column=0, pady=10)

#For running window
App.mainloop()