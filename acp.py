from tkinter import *

window = Tk()
window.title("Inch to CM Converter")
window.geometry("250x150")

def convert():
    try:
        inch = float(entry.get())
        cm = inch * 2.54
        result.config(text=str(cm) + " cm")
    except:
        result.config(text="Invalid input")

Label(window, text="Enter inches:").pack()

entry = Entry(window)
entry.pack()

Button(window, text="Convert", command=convert).pack()

result = Label(window, text="")
result.pack()

window.mainloop()
