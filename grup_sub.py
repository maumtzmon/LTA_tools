import argparse
from math import sqrt as sqrt
import sys

parser = argparse.ArgumentParser(prog='Check_Noise',description='analisis imagenes fits.')
group=parser.add_mutually_exclusive_group() # -i | -j | -k, una unica opcion, no es posible combinarlas

group.add_argument('-i', action='store_true', help='opcion area')       #bool
group.add_argument('-j',action='store_true', help='opcion perimetro')
group.add_argument('-k',action='store_true',help='opcion centro')

parser.add_argument('-x',nargs=4, type=int, help='coordenadas x1, x2, x3 ,x4')  #Lis
parser.add_argument('-y',nargs=4, type=int, help='coordenadas y1, y2, y3 ,y4')

subparsers = parser.add_subparsers()

parser_foo = subparsers.add_parser('foo')
parser_foo.add_argument('-e', type=int, default=1)
parser_foo.add_argument('-f', type=float)

parser_fighters = subparsers.add_parser('fig')
parser_fighters.add_argument('-g',type=int)



              #Break point hasta aqui e...
print("____") #...ingresar esta linea en la DEBUG CONSOLE como Test
              #args_1 = parser.parse_args('-i -x 1 2 3 4 -y 5 6 7 8 foo -e 2 -f 3.0'.split())