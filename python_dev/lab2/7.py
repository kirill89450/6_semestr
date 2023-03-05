import argparse
import os

parser = argparse.ArgumentParser(description='*')

parser.add_argument('filename', help='Название файла для чтения')
parser.add_argument('--sort', action='store_true', help='Сортировка контента')
parser.add_argument('--num', action='store_true', help='Кол-во строк')
parser.add_argument('--count', action='store_true', help='Отображение номера строки')

args = parser.parse_args()

if not os.path.isfile(args.filename):
    print("ERROR")
    exit()

with open(args.filename, 'r') as file:
    content = file.readlines()
    if args.sort:
        content.sort()
    if args.num:
        content = [str(i) + " " + line for i, line in enumerate(content)]
    if args.count:
        print(f"Строк всего: {len(content)}")

    print("".join(content).strip())