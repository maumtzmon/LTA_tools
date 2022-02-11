import argparse
from math import sqrt as sqrt
import sys

def Parse(argv):
    parser = argparse.ArgumentParser(prog='Check_Noise',description='analisis imagenes fits.')
    group=parser.add_mutually_exclusive_group() # -i | -j | -k, una unica opcion, no es posible combinarlas
    group.add_argument('-i', action='store_true', help='opcion area')       #bool
    group.add_argument('-j',action='store_true', help='opcion perimetro')
    group.add_argument('-k',action='store_true',help='opcion centro')

    parser.add_argument('-x',nargs=4, type=int, help='coordenadas x1, x2, x3 ,x4')  #List
    parser.add_argument('-y',nargs=4, type=int, help='coordenadas y1, y2, y3 ,y4')

    args = parser.parse_args() #objeto

    
    if (args.i == True) or (args.j== True) or (args.k == True):
        if (args.x == None) or (args.y == None):
            parser.print_help()
            exit()
    

    return args #devuelve un objeto y llamamos a los elementos del objeto como args.
    

def main(args):
    
    resultado={
            "Area":float(),
            "Perimetro":int()
        }

    if args.i:
        #area del rectangulo
        #Area= Base x Altura
        Lado_1=sqrt(((args.x[1]-args.x[0])**2) + ((args.y[1]-args.y[0]**2)))
        Lado_2=sqrt((args.x[2]-args.x[1])**2+(args.y[2]-args.y[1])**2)
        
        Area=Lado_1*Lado_2
        resultado={
            "Area":Area,"Perimetro":0
        }
    
    elif args.j:
        #perimetro dl poligono
        #Perimetro=Lado+Lado+Lado+Lado
        Lado_1=sqrt((args.x[1]-args.x[0])**2+(args.y[1]-args.y[0])**2)
        Lado_2=sqrt((args.x[2]-args.x[1])**2+(args.y[2]-args.y[1])**2)
        Lado_3=sqrt((args.x[3]-args.x[2])**2+(args.y[3]-args.y[2])**2)
        Lado_4=sqrt((args.x[0]-args.x[3])**2+(args.y[0]-args.y[3])**2)
        
        Perimetro=Lado_1+Lado_2+Lado_3+Lado_4
        Area=Lado_1*Lado_2
        resultado={
            "Area":0,"Perimetro":Perimetro
        }
        
    elif args.k:
        #area y perimetro del poligono
        Lado_1=sqrt((args.x[1]-args.x[0])**2+(args.y[1]-args.y[0])**2)
        Lado_2=sqrt((args.x[2]-args.x[1])**2+(args.y[2]-args.y[1])**2)
        Lado_3=sqrt((args.x[3]-args.x[2])**2+(args.y[3]-args.y[2])**2)
        Lado_4=sqrt((args.x[0]-args.x[3])**2+(args.y[0]-args.y[3])**2)
        
        Area=Lado_1*Lado_2
        Perimetro=Lado_1+Lado_2+Lado_3+Lado_4

        resultado={
            "Area":Area,"Perimetro":Perimetro
        }

    else:
        print("no hubo opcion")

        resultado={
            Area:[],Perimetro:[]
        }
    
    if resultado["Area"]:
        print("\n"+"Area="+str(resultado["Area"]))
    if resultado["Perimetro"]:
        print("Perimetro="+str(resultado["Perimetro"])+"\n")
    

    exitcode=0

    return exitcode




if __name__ == "__main__":
    argv = sys.argv
    args=Parse(argv)
    exitcode = main(args)
    exit(code=exitcode)