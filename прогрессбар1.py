import time

print('....Запуск....')
progressbar = ["▒▒▒▒▒▒▒▒▒▒",  # 0-10%[0]
               "█▒▒▒▒▒▒▒▒▒",  # 10-20%[1]
               "██▒▒▒▒▒▒▒▒",  # 20-30%[2]
               "███▒▒▒▒▒▒▒",  # 30-40%[3]
               "████▒▒▒▒▒▒",  # 40-50%[4]
               "█████▒▒▒▒▒",  # 50-60%[5]
               "██████▒▒▒▒",  # 60-704[6]
               "███████▒▒▒",  # 70-80%[7]
               "████████▒▒",  # 80-90%[8]
               "█████████▒",  # 90-99%[9]
               "██████████"]  # 99-100%[10]

for i in range(101):
    time.sleep(0.01)

    if i < 10:
        print('\r', progressbar[0], str(i), "%", end='')
    if 10 < i < 20:
        print('\r', progressbar[1], str(i), "%", end='')
    if 20 < i < 30:
        print('\r', progressbar[2], str(i), "%", end='')
    if 30 < i < 40:
        print('\r', progressbar[3], str(i), "%", end='')
    if 40 < i < 50:
        print('\r', progressbar[4], str(i), "%", end='')
    if 50 < i < 60:
        print('\r', progressbar[5], str(i), "%", end='')
    if 60 < i < 70:
        print('\r', progressbar[6], str(i), "%", end='')
    if 70 < i < 80:
        print('\r', progressbar[7], str(i), "%", end='')
    if 80 < i < 90:
        print('\r', progressbar[8], str(i), "%", end='')
    if 90 < i < 100:
        print('\r', progressbar[9], str(i), "%", end='')
    if i == 100:
        print('\r', progressbar[10], str(i), "%", end='')

input('\nЗагрузка завершена')