from cProfile import label
import tkinter

window = tkinter.Tk()
window.title("Miles to Kilometer Converter")
# window.minsize(width=350,height=100)
window.config(padx=20,pady=20)

# Labels
Miles = tkinter.Label(text="Miles")
Miles.grid(row=0,column=2)

Text = tkinter.Label(text="is equal to")
Text.grid(row=1,column=0)

Km = tkinter.Label(text="Km")
Km.grid(row=1,column=2)

KmOp = tkinter.Label(text="0")
KmOp.grid(row=1,column=1)

def calculate():
    mile = input.get()
    KmOp["text"] = int(mile)*1.609
    pass

# Entry 
input = tkinter.Entry(width=7)
input.grid(row=0,column=1)

# Button
button = tkinter.Button(text="Calculate", command=calculate)
button.grid(row=2,column=1)
window.mainloop()