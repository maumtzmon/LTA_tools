

def MultiCommandParser(argv):
    #print('parse commands and file funct')
    #devolver diccionario con comandos y archivos
    
    commandDict={\
        'files':[],
        'commands':[]
    }
    
    
    argsCopy=argv
    for i in argsCopy:
        #si i contiene "-", removerlo, separar las letras y hacer una lista con ellas
        if i.startswith('-') == True:
            commandDict['commands']=list(i)
            commandDict['commands'].pop(0)
        else:
            commandDict['files'].append(i)

        if 'S' not in commandDict['commands']:
                commandDict['commands'].append('S')
    return commandDict

