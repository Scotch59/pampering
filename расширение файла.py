file = input("Введите имя файла: ")
ext = file.split(".")[-1]
if len(ext) > 0:
    print("Расширение файла:", ext)
else:
    print("Не удалось определить расширение файла.")