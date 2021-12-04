
import sys

def MultiCommandParser(argv):
    #print('parse commands and file funct')
    #devolver diccionario con comandos y archivos
    
    commandDict={\
        'files':[],
        'commands':[]
    }
    
    files = sys.argv[1:]
    
    for i in files:
        #si i contiene "-", removerlo, separar las letras y hacer una lista con ellas
        
        if i.startswith('-') == True:
            commandDict['commands']=list(i)
            commandDict['commands'].pop(0)
        else:
            if i.endswith('.fits'):
                commandDict['files'].append(i)

        if 'S' not in commandDict['commands'] and len(commandDict['files'])>0:
                commandDict['commands'].append('S')
    return commandDict

