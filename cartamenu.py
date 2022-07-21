from utils import limpiarpantalla,sn
from lista import validacion,agregar_lista
aux=[]
ruta_archivo="./archivos/carta_menu.txt"
def entrantes():
    limpiarpantalla()
    ruta=open(ruta_archivo,"r")
    print("**************************")
    for linea in ruta:
        parte=linea.split(";")
        if parte[2] == "entrante":
            print("{}\t{} \t ---> {}".format(parte[0],parte[1],parte[3]),end="")

    print("**************************")
    code=input("ingrese codigo: ")
    menu1(code)
    sn()
    ruta.close()


def dato(dni):
    aux.append(dni)


def menu1(code):
    dni=str(aux[0])
    validacion(dni)
    agregar_lista(code)

def principal():
    ruta=open(ruta_archivo,"r")
    print("**************************")
    for linea in ruta:
        parte=linea.split(";")
        if parte[2] == "principal":
            print("{}\t{} \t ---> {}".format(parte[0],parte[1],parte[3]),end="")
    print("**************************")
    code=input("ingrese codigo: ")
    menu1(code)
    sn()
    ruta.close()


def postres():
    ruta=open(ruta_archivo,"r")
    print("**************************")
    for linea in ruta:
        parte=linea.split(";")
        if parte[2] == "postre":
            print("{}\t{} \t ---> {}".format(parte[0],parte[1],parte[3]),end="")
    print("**************************")
    code=input("ingrese codigo: ")
    menu1(code)
    sn()
    ruta.close()

def carta_menu():
    while True:
        limpiarpantalla()
        print("\033[2;1;4;34m"+"| *** CARTA MENU *** |"+"\033[0m")
        print("======================")
        print("1 entrantes principales")
        print("2 platos principales")
        print("3 postres  ")
        print("0 regresar al menu anterior")


        op=int(input("ingrese un opcion "))
        limpiarpantalla()
        match(op):
            case 1:
                entrantes()  
            case 2:
                principal()
            case 3:
                postres()
            case 0: 
                print(">>> espere un momento ...")
                break
            case _: print(">>> opcion invalida...")

