from pyowm import OWM
from tkinter import *
from tkinter.messagebox import *

owm = OWM("6ca70320000d09d03e148b22d081710b")# key_API
place = input("Введите название города: ")
mgr = owm.weather_manager()
observation = mgr.weather_at_place(place)
w = observation.weather

t = w.temperature("celsius")
t1 = t["temp"]


root = Tk()
btn1 = Button(root,text="Проверить погоду", command=lambda: showinfo(place, int(t1)))
btn1.grid(row=0, column=0, sticky="ew")


root.mainloop()