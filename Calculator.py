from tkinter import *


def button_press(text):
    global input_text
    input_text = input_text + str(text)
    input_label.set(input_text)


def equals():
    global input_text
    try:
        result = str(eval(input_text))
        input_label.set(result)
        input_text = result
    except ZeroDivisionError:
        input_label.set("Arithmetic Error")
        input_text = ""
    except SyntaxError:
        input_label.set("Syntax Error")
        input_text = ""


def clear():
    global input_text
    input_text = ""
    input_label.set("")


window = Tk()
window.title("Calculator program")
window.geometry("500x500")

input_text = ""
input_label = StringVar()

label = Label(window, textvariable=input_label, font=("Helvetica", 30), bg="white", width=19, height=2)
label.pack()

frame = Frame(window)
frame.pack()

button1 = Button(frame, text=1, height=2, width=9, font=35, command=lambda: button_press(1))
button1.grid(row=0, column=0)

button2 = Button(frame, text=2, height=2, width=9, font=35, command=lambda: button_press(2))
button2.grid(row=0, column=1)

button3 = Button(frame, text=3, height=2, width=9, font=35, command=lambda: button_press(3))
button3.grid(row=0, column=2)

button4 = Button(frame, text=4, height=2, width=9, font=35, command=lambda: button_press(4))
button4.grid(row=1, column=0)

button5 = Button(frame, text=5, height=2, width=9, font=35, command=lambda: button_press(5))
button5.grid(row=1, column=1)

button6 = Button(frame, text=6, height=2, width=9, font=35, command=lambda: button_press(6))
button6.grid(row=1, column=2)

button7 = Button(frame, text=7, height=2, width=9, font=35, command=lambda: button_press(7))
button7.grid(row=2, column=0)

button8 = Button(frame, text=8, height=2, width=9, font=35, command=lambda: button_press(8))
button8.grid(row=2, column=1)

button0 = Button(frame, text=0, height=2, width=9, font=35, command=lambda: button_press(0))
button0.grid(row=3, column=0)

button9 = Button(frame, text=9, height=2, width=9, font=35, command=lambda: button_press(9))
button9.grid(row=2, column=2)

plus = Button(frame, text="+", height=2, width=9, font=35, command=lambda: button_press("+"))
plus.grid(row=0, column=3)

subtract = Button(frame, text="-", height=2, width=9, font=35, command=lambda: button_press("-"))
subtract.grid(row=1, column=3)

multiply = Button(frame, text="*", height=2, width=9, font=35, command=lambda: button_press("*"))
multiply.grid(row=2, column=3)

divide = Button(frame, text="/", height=2, width=9, font=35, command=lambda: button_press("/"))
divide.grid(row=3, column=3)

equal = Button(frame, text="=", height=2, width=9, font=35, command=equals)
equal.grid(row=3, column=2)

mod = Button(frame, text="%", height=2, width=9, font=35, command=lambda: button_press("%"))
mod.grid(row=3, column=1)

decimal = Button(frame, text=".", height=2, width=9, font=35, command=lambda: button_press("."))
decimal.grid(row=4, column=0)

clear = Button(frame, text="clear", height=2, width=29, font=35, command=clear)
clear.grid(row=4, column=1, columnspan=3)

window.mainloop()
