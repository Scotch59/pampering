from tkinter import *


root = Tk()
a = 320
b = 250
c = 1300
d = 200
photo = PhotoImage(file="png.png")
root.iconphoto(False, photo)
root.config(bg="#000000")
root.title("Калькулятор")
root.geometry(f"{a}x{b}+{c}+{d}")
root.resizable(False, False)

calc = Entry(root, justify=RIGHT, font=("Arial", 20))
calc.insert(0, "0")
calc.grid(row=0, column=0, columnspan=4, sticky="we", padx=7, pady=2)

root.grid_columnconfigure(0, minsize=50)
root.grid_columnconfigure(1, minsize=50)
root.grid_columnconfigure(2, minsize=50)
root.grid_columnconfigure(3, minsize=50)


root.grid_rowconfigure(1, minsize=50)
root.grid_rowconfigure(2, minsize=50)
root.grid_rowconfigure(3, minsize=50)
root.grid_rowconfigure(4, minsize=50)




def digit_Button(digit):
    return Button(text=digit, bg="#708090", bd=5, font=("Arial", 15), command=lambda: get_digit(digit))


def get_digit(digit):
    value = calc.get()
    if value[0] == "0":
        value = value[1:]
    calc.delete(0, END)
    calc.insert(0, value + digit)



digit_Button("1").grid(row=1, column=0, sticky="wens", padx=3, pady=3)
digit_Button("2").grid(row=1, column=1, sticky="wens", padx=3, pady=3)
digit_Button("3").grid(row=1, column=2, sticky="wens", padx=3, pady=3)
digit_Button("4").grid(row=2, column=0, sticky="wens", padx=3, pady=3)
digit_Button("5").grid(row=2, column=1, sticky="wens", padx=3, pady=3)
digit_Button("6").grid(row=2, column=2, sticky="wens", padx=3, pady=3)
digit_Button("7").grid(row=3, column=0, sticky="wens", padx=3, pady=3)
digit_Button("8").grid(row=3, column=1, sticky="wens", padx=3, pady=3)
digit_Button("9").grid(row=3, column=2, sticky="wens", padx=3, pady=3)
digit_Button("0").grid(row=4, column=0, sticky="wens", padx=3, pady=3)



def operation_Button(operation):
    return Button(text=operation, bg="#40E0D0", bd=5, font=("Bold", 15), command=lambda: app_operation(operation))

def app_operation(operation):
    value = calc.get()
    if value[-1] in "+-/*":
        value = value[:-1]
    calc.delete(0, END)
    calc.insert(0, value + operation)


operation_Button("+").grid(row=1, column=3, sticky="wens", padx=3, pady=3)
operation_Button("-").grid(row=2, column=3, sticky="wens", padx=3, pady=3)
operation_Button("/").grid(row=3, column=3, sticky="wens", padx=3, pady=3)
operation_Button("*").grid(row=4, column=3, sticky="wens", padx=3, pady=3)



def calc_button (operation):
    return Button(text=operation, bg="#40E0D0", bd=5, font=("Bold", 15), command=calculate)


def calculate():
    value = calc.get()
    calc.delete(0, END)
    calc.insert(0, eval(value))


calc_button("=").grid(row=4, column=2, sticky="wens", padx=3, pady=3)



def calc_clear(operation):
    return Button(text=operation, bg="#FF8C00", bd=5, font=("Bold", 15), command=clear)

def clear():
    calc.delete(0, END)
    calc.insert(0, "0")


calc_clear("C").grid(row=4, column=1, sticky="wens", padx=3, pady=3)


root.mainloop()