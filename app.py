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

#For running window
App.mainloop()