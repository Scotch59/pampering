import time, sys
indent = 0
indentIncreasing = True

try:
    while True:
        print(" " * indent, end="")
        print("********")
        time.sleep(0.1)

        if indentIncreasing:
            indent += 3
            if indent == 30:
                indentIncreasing = False
        else:
            indent -= 3
            if indent == 0:
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()