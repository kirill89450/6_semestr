import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('a', type=int, nargs='?', help='first integer parameter')
parser.add_argument('b', type=int, nargs='?', help='second integer parameter')
args = parser.parse_args()

if args.a is None and args.b is None:
    print('NO PARAMS')
elif args.b is None:
    print('TOO FEW PARAMS')
elif len(sys.argv) > 3:
    print('TOO MANY PARAMS')
else:
    print(args.a + args.b)
