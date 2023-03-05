import argparse

parser = argparse.ArgumentParser(description='Process some data.')
parser.add_argument('--sort', action='store_true', help='sort the output')
parser.add_argument('key_value_pairs', nargs='+', metavar='key=value', help='list of key-value pairs')

args = parser.parse_args()

data = {}
for arg in args.key_value_pairs:
    key, value = arg.split("=")
    data[key] = value

if args.sort:
    sorted_keys = sorted(data.keys())
    for key in sorted_keys:
        print(f"Key: {key} Value: {data[key]}")
else:
    for key, value in data.items():
        print(f"Key: {key} Value: {value}")
