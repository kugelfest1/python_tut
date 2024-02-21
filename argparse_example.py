import argparse

parser = argparse.ArgumentParser(description='Optional app description')

# required positional argument
parser.add_argument('pos_arg', type=int, help="mandatory 1st arg")

# optional positional argument
parser.add_argument('opt_pos_arg', type=int, nargs='?',
        help='optional positional arg')

# optional arg
parser.add_argument('-opt_arg', type=int,
        help='optional arg')

# switch
parser.add_argument('--switch', action='store_true',
        help='boolean switch')

args = parser.parse_args()

print('argument values;')
print(args.pos_arg)
print(args.opt_pos_arg)
print(args.opt_arg)
print(args.switch)


