from tkinter import *

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500,height=300)
window.config(padx=50,pady=50)

# Label
my_label = Label(text="Label",font=("Arial",24,"bold"))
my_label.grid(row=0,column=0)

# my_label["text"] = "New Text"
# my_label.config(text="New Text")


# Entry
input = Entry(width=10)
input.grid(row=2,column=3)


# Button

def button_clicked():
    new_text = input.get()
    if len(new_text) !=0:
        my_label["text"] = new_text
    

button = Button(text="Click Me", command=button_clicked)
button.grid(row=1,column=1)

button2 = Button(text="Click Me2", command=button_clicked)
button2.grid(row=0,column=2)

window.mainloop()