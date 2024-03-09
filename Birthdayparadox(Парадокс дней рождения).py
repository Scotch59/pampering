import datetime, random              # Если много значений придумать как их переносить на ноаую строку

def getBirthdays(numberOfBirthdays):
    """"Возвращаем список объектов дат для случайных дней рождения."""
    birthdays = []
    for i in range(numberOfBirthdays):
        startOfYear = datetime.date(2001, 1, 1)
        randomNumberOfDays = datetime.timedelta(random.randint(0, 264))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays

def getMatch(birthdays):
    """"Возвращаем объект даты дня рождения встречающегося несколько раз в списке дней рождений"""
    if len(birthdays) == len(set(birthdays)):
        return None

    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1 :]):
            if birthdayA == birthdayB:
                return birthdayA

print(""""Birthday Paradox, by Al Sweigart al@iventwithpython.com""")


MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True:
    print("How many birthday shall I generate? (Max 100)")
    response = input("> ")
    if response.isdecimal() and (0 < int(response) <= 100):
        numBDays = int(response)
        break
print()

print("Here are", numBDays, "birthdays:")
birthdays = getBirthdays(numBDays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        print(", ", end="")
    montName = MONTHS[birthday.month -1]
    dateText = f"{montName} {birthday.day}"
    print(dateText, end="")
print()
print()


match = getMatch(birthdays)

print("In this simulation, ", end='')
if match != None:
    montName = MONTHS[match.month - 1]
    dateText = f"{montName} {match.day}"
    print("miltiple people have a birthday on", dateText)
else:
    print("there are no match birthdays.")
print()


print("Generating", numBDays, "random birthday 100,000 times...")
input("Press Enter to begin...")
simMatch = 0
for i in range(100_000):
    if i % 10_000 == 0:
        print(i, "simulations run...")
    birthdays = getBirthdays(numBDays)
    if getMatch(birthdays) != None:
        simMatch += 1
print("100,000 simulations run.")

probability = round(simMatch / 100_000 * 100, 2)
print("Out of 100,000 simulations of", numBDays, "people, there was a")
print("matching birthday in that group", simMatch, "times. This means")
print("that", numBDays, "people have a", probability, "% chance of")
print("having a matching birthday in their group.")
print("That\'s probaliti more that yiu would think!")