import argparse

# Создаем парсер аргументов
parser = argparse.ArgumentParser()

parser.add_argument('args', nargs='*', help='Аргументы командной строки')

args = parser.parse_args()

if not args.args:
    print('no args')

else:
    for arg in args.args:
        print(arg)
