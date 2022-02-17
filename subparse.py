import argparse
from math import sqrt as sqrt
import sys

# sub-command functions
def foo(args):
    print(args.x * args.y)

def bar(args):
    print('((%s))' % args.z)

# create the top-level parser
parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

# create the parser for the "foo" command
parser_foo = subparsers.add_parser('foo')
parser_foo.add_argument('-x', type=int, default=1)
parser_foo.add_argument('y', type=float)
parser_foo.set_defaults(func=foo)



# create the parser for the "bar" command
parser_bar = subparsers.add_parser('bar')
parser_bar.add_argument('z')
parser_bar.set_defaults(func=bar)

# parse the args and call whatever function was selected
args_1 = parser.parse_args('foo 1 -x 2'.split())
args_1.func(args_1)

# parse the args and call whatever function was selected
args_2 = parser.parse_args('bar XYZYX'.split())
args_2.func(args_2)

print("___")