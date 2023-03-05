import sys

args = sys.argv[1:]
sort_output = "--sort" in args

if sort_output:
    args.remove("--sort")

data = {}
for arg in args:
    key, value = arg.split("=")
    data[key] = value

if sort_output:
    sorted_keys = sorted(data.keys())
    for key in sorted_keys:
        print(f"Key: {key} Value: {data[key]}")
else:
    for key, value in data.items():
        print(f"Key: {key} Value: {value}")
