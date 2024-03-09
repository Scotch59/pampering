from tkinter import *


# Функция для выполнения операции
def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operator = operator_var.get()

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error"

        label_result.config(text="Результат: {}".format(result))

    except ValueError:
        label_result.config(text="Ошибка: Некорректные данные")


# Создаем окно
window = Tk()
window.title("Калькулятор")

# Создаем элементы интерфейса
label1 = Label(window, text="Число 1:")
label1.pack()

entry1 = Entry(window)
entry1.pack()

label2 = Label(window, text="Число 2:")
label2.pack()

entry2 = Entry(window)
entry2.pack()

operator_var = StringVar(window)
operator_var.set("+")

operator_dropdown = OptionMenu(window, operator_var, "+", "-", "*", "/")
operator_dropdown.pack()

calculate_button = Button(window, text="Вычислить", command=calculate)
calculate_button.pack()

label_result = Label(window, text="Результат: ")
label_result.pack()

# Запускаем главный цикл событий
window.mainloop()