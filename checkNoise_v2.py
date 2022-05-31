#!/usr/bin/python3
###
# checkNoise V2.0      Mauricio Martinez, Brenda Cervantes
###

#imports, libraries
import sys
from myLibs.mean import mean
from myLibs.noise import noise
from myLibs.help import help

#import my libraries
from myLibs.commandParse import MultiCommandParser

# -S	Standar dev  (Default)
# -M	Mean
# -m	median
    # To Do
    # -a	all OHDU
    # -c	choose which OHDU
    # -s	save .txt and .csv files

def main(argv):

    commandDict = MultiCommandParser(argv)
    if len(commandDict['files']) == 0 and len(commandDict['commands']) == 0:
        help()
        exitcode=1
    
    elif len(commandDict['commands'])>0 and len(commandDict['files'])>0:
        
        if 'S' in commandDict['commands'] or 'M' in commandDict['commands'] or 'm' in commandDict['commands']:
            noise(commandDict['files'],commandDict['commands'])
            commandDict['commands'].clear()
            
        
        # elif 'a' == option:
        #     print('do the a thing')
        #     continue 

        # elif 'c' == option:
        #     print('do the c thing')
        #     continue

        # elif 's' == option:
        #     print('do the s thing')
        #     continue
        if  'x' in commandDict['commands']:
            mean(commandDict['files'],commandDict['commands'])
            commandDict['commands'].clear()

        else: help()

        exitcode=0
    
if __name__ == "__main__":
    argv = sys.argv
    exitcode = main(argv)
    exit(code=exitcode)
