import argparse
import cowsay
import sys



parser = argparse.ArgumentParser(prog='cow_say', description='Set the parameters')

parser.add_argument("message", nargs='*', default=[' '])

parser.add_argument('-n', action='store_false')
parser.add_argument('-W', default=40)

parser.add_argument('-b', action='store_true')
parser.add_argument('-d', action='store_true')
parser.add_argument('-g', action='store_true')
parser.add_argument('-p', action='store_true')
parser.add_argument('-t', action='store_true')
parser.add_argument('-w', action='store_true')
parser.add_argument('-y', action='store_true')

parser.add_argument('-e', dest='eye_string', default="oo")
parser.add_argument('-T', dest='tongue_string', default="")
parser.add_argument('-f', dest='cowfile')
parser.add_argument('-l', action='store_true')

parser.add_argument("-bdgptwye", dest="preset")

args = parser.parse_args()


if args.l:
    print(cowsay.list_cows())
else:
    cows = cowsay.cowsay(args.message, preset=args.preset, eyes=args.e, tongue=args.T, width=args.W, wrap_text=args.n, cowfile=args.f)
    print(cows)


print(cow("Ha-ha-not-so-much"))
