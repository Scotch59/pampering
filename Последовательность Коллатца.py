n = int(input("Введите целое число:"))

stec = 0
max_num = -1

while n > 1:
    if n > max_num:
        max_num = n
    print(n)
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    stec += 1
print(n)
print("Bottom line:", stec)
print("MAXIMUM:", max_num)

