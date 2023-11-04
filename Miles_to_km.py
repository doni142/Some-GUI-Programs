from tkinter import *


def miles_to_km():
    miles = float(miles_entry.get())
    km = miles * 1.609
    km_label.config(text=f"{km}")


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

miles_entry = Entry(width=5)
miles_entry.grid(row=0, column=1)

miles_label = Label()
miles_label.grid(row=0, column=2)
miles_label.config(text="Miles")

_is_equal_label = Label()
_is_equal_label.grid(row=1, column=0)
_is_equal_label.config(text="is equal to")

km_label = Label(text="0")
km_label.grid(row=1, column=1)
print(miles_entry.get())

your_label = Label()
your_label.grid(row=1, column=2)
your_label.config(text="Km")

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()
