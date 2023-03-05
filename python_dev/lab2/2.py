import sys
import os

args = sys.argv[1:]

if len(args) < 1:
    print("ERROR")
    sys.exit()

filename = args[0]

if not os.path.isfile(filename):
    print("ERROR")
    sys.exit()

with open(filename, 'r') as file:
    content = file.readlines()
    if "--sort" in args:
        content.sort()
    if "--num" in args:
        content = [str(i) + " " + line for i, line in enumerate(content)]
    if "--count" in args:
        print(f"Строк всего: {len(content)}")

    # Выводим содержимое
    print("".join(content).strip())
