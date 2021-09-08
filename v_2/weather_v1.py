from pyowm import OWM
from tkinter import *
from tkinter.messagebox import *


# очищаем Label
# def gopass():
#     label_2["text"] = ""
#     label_2["text"] = "".join(choice(sy) for i in range(5))


def city(event):
    owm = OWM("6ca70320000d09d03e148b22d081710b")
    place = entry_1.get()
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(place)
    w = observation.weather
    t = w.temperature("celsius")
    t1 = int(t["temp"])
    label_2 = Label(root, text=place, font=("Ubuntu", 20))
    label_3 = Label(root, text=str(t1) + "°c", font=("Ubuntu", 40))
    label_2.grid(row=2, column=2)
    label_3.grid(row=3, column=2)


root = Tk()

label_1 = Label(root, text="Город", font=("Ubuntu", 12), width=10, height=10)
btn1 = Button(root, text="Проверить погоду", width=20, bg="#A2E0E1")

entry_1 = Entry(root, font=("Ubuntu", 12), width=20)

label_1.grid(row=0, column=0, sticky=E)

entry_1.grid(row=0, column=2)
btn1.grid(row=0, column=3, sticky="ew")

root.geometry("450x500")
# btn1.config(command=gopass)
btn1.bind("<Button-1>", city)
root.mainloop()