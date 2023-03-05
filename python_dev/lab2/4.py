import argparse

# Создаем парсер аргументов
parser = argparse.ArgumentParser()

# Определяем аргументы командной строки
parser.add_argument('source_file', help='Имя файла-источника')
parser.add_argument('target_file', help='Имя файла-приемника')
parser.add_argument('--upper', action='store_true', help='Привести все символы к верхнему регистру')
parser.add_argument('--lines', type=int, help='Копировать только первые N строк')

args = parser.parse_args()

try:
    with open(args.source_file, 'r') as f:
        source_lines = f.readlines()
except FileNotFoundError:
    print(f"ERROR: Файл {args.source_file} не найден")
    exit()

if args.lines is None or args.lines > len(source_lines):
    lines_to_copy = len(source_lines)
else:
    lines_to_copy = args.lines

if args.upper:
    source_lines = [line.upper() for line in source_lines]

with open(args.target_file, 'w') as f:
    for line in source_lines[:lines_to_copy]:
        f.write(line)

print(f"Файл {args.source_file} был скопирован в {args.target_file}")
