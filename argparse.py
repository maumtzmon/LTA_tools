import argparse

parser = argparse.ArgumentParser(prog="FITSanlyzer", description='High particle FITS images analyzer. \n Aqui un breve comentario sobre el proposito y objetivo de este codigo')
# parser.add_argument('integers', metavar='N', type=int, nargs='+',
#                     help='an integer for the accumulator')

parser.add_argument('-f','--pdf',action='store_true',help="Save results in PDF file.")

subparsers=parser.add_subparsers(help="sub command Help")

###
# Positional Arguments
###
sub_action_1 = subparsers.add_parser('skp', help = 'skipping tool help \n Creates an regurlar CCD image using a skipped image')
sub_action_1.add_argument('file', type=str, nargs = '+',help='file or path of FITS images')
sub_action_1.add_argument('n', type=int, nargs = 1, help = 'number of skipping cycles of the images' )
#run skipped to regular imege function

sub_action_2 = subparsers.add_parser('other_subOPT', help = 'help')
sub_action_2.add_argument('Variable_PATH', type=int, help='help')
#run function

###
# Optional arguments
###
group = parser.add_mutually_exclusive_group()
group.add_argument('-i','--histogram',type=str, # action='append',
                   help='Makes the histogram of charge in the active region (AA) and in overscan regions (OSX, OSY, OSXY).')
group.add_argument('-c','--charge',type=str,nargs='+',# action='store_true',
                    help='Estimates the charge in the active region (AA) and in overscan regions (OSX, OSY, OSXY).')
group.add_argument('-d','--dCurrent', type=str,nargs='+', # Corriente obscura
                    help='Estimates Dark Current in the region selected')

group.add_argument('-e','--eventDet', type=str,nargs='+',# Detección de eventos
                    help='')

# subparsers = parser.add_subparsers()
# parser_x = subparsers.add_parser("-x",help="x coordinates x1 x2 x3 x4.")
parser.add_argument('-x',type=int,nargs=4,help="x coordinates x1 x2 x3 x4.")
parser.add_argument('-y',type=int,nargs=4,help="y coordinates y1 y2 y3 y4.")
parser.add_argument('-b','--baseline',action='store_true',help="enable option Baseline substraction.") #va a llevar algun otro argumento adicional


#salvar en PDF el resultado
parser.add_argument('-p','--pdf',action='store_true',help="enable option to create a report of the analysis.") #va a llevar algun otro argumento adicional

#output option



#EXAMPLE
#bjeto=parser.parse_args('-i /home/datosFits/file -x 10 10 10 10 -y 10 10 10 10 -b'.split())
print("______")






# parser.add_argument()