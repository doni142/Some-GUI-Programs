from tkinter import *

window = Tk()  # tkinter itt nem kell, csak siman a TK()
window.title('My First GUI Program')
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)  # egésznek adja a margót // margin full

# Label címke
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
# miles_label.pack()  #side = left, right, bottom, top, expand=True
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)  # címkének adja a margót label
# turtle
'''import turtle
tim = turtle.Turtle()
tim.write("Some Text", font=("Arial", 10, 'italic'))
'''


# Button
def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)
# button.pack()

# Entry
in_put = Entry(width=10)
# input.pack()
print(in_put.get())
in_put.grid(column=3, row=2)

# new button
new_button = Button(text="Click me", command=button_clicked)
new_button.grid(column=2, row=0)

'''while True:
    listening'''
window.mainloop()  # this will open the window
