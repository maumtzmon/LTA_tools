###
#programa checkNoise V2.0
###

#imports, libraries
import sys
from myLibs.noise import noise

#import my libraries
from myLibs.commandParse import MultiCommandParser

# -S	Standar dev
# -M	Mean
# -m	median
    # -a	all OHDU
    # -c	choose which OHDU
    # -s	save .txt and .csv files

def main(argv):

    commandDict = MultiCommandParser(argv)
    exitcode=1

    while len(commandDict['commands'])>0 and len(commandDict['files'])>0:
        
        #option=commandDict['commands'].pop()
        
        if 'S' or 'M' or 'm' in commandDict['commands']:
            #haga algo y despues...
            print('do the S thing')
            noise(commandDict['files'],commandDict['commands'])
            commandDict['commands'].clear()
            continue
        
        # elif 'a' == option:
        #     print('do the a thing')
        #     continue 

        # elif 'c' == option:
        #     print('do the c thing')
        #     continue

        # elif 's' == option:
        #     print('do the s thing')
        #     continue

    exitcode=0
    
if __name__ == "__main__":
    argv = sys.argv
    exitcode = main(argv)
    exit(code=exitcode)
