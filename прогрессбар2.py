from time import sleep

anim = "|/-\\"
for i in range(20):
    element = anim[i % len(anim)]
    print(element, end="\r")
    sleep(0.1)
print("\b\bfsssf")