import argparse
from cowsay import cowsay
from cowsay import list_cows


parser = argparse.ArgumentParser(prog='cow_say', description='Set the parameters')

parser.add_argument('-n', action='store_false')
parser.add_argument('-W', type = int, default = 40)

parser.add_argument('-b', action='store_true')
parser.add_argument('-d', action='store_true')
parser.add_argument('-g', action='store_true')
parser.add_argument('-p', action='store_true')
parser.add_argument('-t', action='store_true')
parser.add_argument('-w', action='store_true')
parser.add_argument('-y', action='store_true')

parser.add_argument('-e', dest='eye_string', default = "oo")
parser.add_argument('-T', dest='tongue_string', default = "")
parser.add_argument('-f', dest='cowfile')
parser.add_argument('-l', action='store_true')



print(cowsay("Ha-ha-not-so-much"))


