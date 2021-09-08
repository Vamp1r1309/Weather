from tkinter import *
from tkinter import messagebox
from pyowm import OWM
from pyowm.utils import config as cfg

color_bg_root = "#A2E0E1"
FS = "Calibri"



# def clicked():  
#     messagebox.showinfo('Ошибка', 'Вы допустили ошибку')

class weather():
    def delet(event):
        entry_1.delete(0, END)

    def get_weather(event):  
        try:
            if len(entry_1.get()) > 0 or len(entry_1.get()) == 0:   
                config = cfg.get_default_config()
                config['language'] = 'ru'
                owm = OWM("6ca70320000d09d03e148b22d081710b", config)
                mgr = owm.weather_manager()
                observation = mgr.weather_at_place(entry_1.get())
                w = observation.weather
                t = w.temperature("celsius")
                t1 = int(t["temp"])
                label_1 = Label(root, text=entry_1.get().title(), font=(FS, 25), width=15, bg=color_bg_root)
                label_2 = Label(root, font=(FS, 50), width=5, bg=color_bg_root)
                if t1 > 0:label_2["text"] = "+" + str(t1) + "°"
                else:label_2["text"] = str(t1) + "°"
                label_1.grid(row=3, pady=20)
                label_2.grid(row=4)
                entry_1.delete(0, END)
        except:
            if len(entry_1.get()) > 0:
                messagebox.showerror("Ошибка", "Вы допустили ошибку!")
                # entry_1.delete(0, END)
            else:
                messagebox.showwarning("Ошибка", "Вы ничего не ввели")

root = Tk()
root["bg"] = color_bg_root
root.title("Погода")
main = weather()

label_1 = Label(root, text="Ваш город ", font=(FS, 25), width=10, bg=color_bg_root)
entry_1 = Entry(root,font=(FS, 20), width=19)
btn_1 = Button(root, text="Показать",font=(FS, 10),bg="white",activebackground="#1b755b", command=lambda: main.get_weather())
btn_2 = Button(root, text="Стереть", font=(FS, 10), foreground="#57677D", bg="white", command=lambda: main.delet())

label_1.grid(row=0, pady=20)
entry_1.grid(padx=13)
entry_1.focus()
btn_1.grid(row=2,column=0,padx=10, ipadx=40, pady=20,sticky=W)
btn_2.grid(row=2, column=0,padx=abs(10),ipadx=40, sticky=E)

root.resizable(width=False, height=False)
root.geometry("300x370")

root.mainloop()
