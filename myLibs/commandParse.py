
import sys
import os

def MultiCommandParser(argv):
    #print('parse commands and file funct')
    #devolver diccionario con comandos y archivos
    
    commandDict={\
        'files':[],
        'commands':[]
    }
    
    argList = sys.argv[1:]
    
    for i in argList:
        #si i contiene "-", removerlo, separar las letras y hacer una lista con ellas
        
        if i.startswith('-') == True:
            commandDict['commands']=list(i)
            commandDict['commands'].pop(0)
        else:
            filesFits=os.listdir(i)
            for j in filesFits:
                if j.startswith('proc'):
                    commandDict['files'].append(argList[0]+j)

        #if 'S' not in commandDict['commands'] and len(commandDict['files'])>0:
        #        commandDict['commands'].append('S')
    return commandDict

