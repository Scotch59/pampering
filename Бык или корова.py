import random
import progressbar
from string import digits



print("""Приветствую!
Игра “БЫКИ–КОРОВЫ” - замечательная логическая игра, она развивает умение сравнивать и анализировать.
Суть игры:
Компьютер загадывает число из четырех неповторяющихся цифр (ноль в игре используется, но на первом месте
стоять не может. Ваша задача отгадать это число с 10 попыток.
Вы пишите  любое 4-х значное число, у которого цифры также не повторяются. При совпадении цифр написанного
числа с загаданным говорится “БЫК”. Бык означает, что цифра отгадана и стоит в нужной позиции (например,
в задуманном числе первая цифра 3 и в названном противником – тоже первая 3 – это бык.). Корова означает,
что цифра отгадана, но она стоит не в своей позиции. Путем логических рассуждений и проверки ответов
необходимо угадать все 4 цифры числа и их порядок. Вы выигрываете если угадаете число загаданное компьютером
число. Например, загадано 3749 и Вы пишите 3749
""")


def getSecNum():
    list_num = list(digits)
    secret = random.sample(list_num, num_digits)
    if secret[0] == str(0):
        getSecNum()
    return "".join(secret)


def getClues(guess, secret_num):
    clues = []
    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            clues.append("Бык")
        elif guess[i] in secret_num:
            clues.append("Корова")
    if len(clues) == 0:
        return ("\nНет совпадений!")

    else:
        return ",".join(clues)


attempt = 1
num_digits = 4
max_guesses = 10
secret_num = getSecNum()


while attempt <= max_guesses:
    print("-" * 40, "\n" "Попытка №", attempt)
    guess = input("\nВведите четырехзначное число:")
    if not guess.isdecimal():
        print("\nВы ввели буквы!")
        continue
    if len(guess) != num_digits:
        print("\nВы ввели неверное количество цифр!")
        continue
    if guess[0] == str(0):
        print("\nНа первом месте не может стоять 0")
        continue
    repeat_digits = False
    for i in set(guess):
        if guess.count(i) > 1:
            print("\nВы ввели число с повторяющимися цифрами!")
            repeat_digits = True
            break
    if repeat_digits:
        continue


    clues = getClues(guess, secret_num)
    print("Проверяю совпадения...")
    progressbar.prog()
    print("\nПодсказка:", clues)
    if guess != secret_num:
        attempt += 1
    else:
        print("Вы угадали число, с", attempt, "попыток!")
        break
else:
    print("-" * 40)
    print("Вы проиграли!", "\nЗагаданное число:", secret_num)





