
from pydoc import cram
from utils import limpiarpantalla,sn
from models import Producto
import time

ruta_de_archivo="./archivos/carta_menu.txt"

def crearplato():
    codigo =input("codigo: ")
    nombre =input("nombre: ")
    detalle =input("detalle: ")
    precio =input("precio: ")

    plt= Producto(codigo,nombre,detalle,precio)
    archivoplt= open(ruta_de_archivo, "a")
    archivoplt.write(str(plt))
    archivoplt.close()

def mostrarplato():
    #print(ruta.read())
    ruta= open(ruta_de_archivo, "r") 
    print("CODIGO \t NOMBRE \t\t DETALLE \t PRECIO")
    for linea in ruta.readlines():
        atributo = linea.split(";")
        #aux.append(linea)
        print("{} \t {} \t\t {} \t{}".format(atributo[0],atributo[1],atributo[2],atributo[3]), end="")
 
    ruta.close() 

def validar_codigo(codigo):
    ruta= open(ruta_de_archivo, "r") 
    for linea in ruta.readlines():
        atributo = linea.split(";")
        if codigo == atributo[0]:
            print("{} {} {} {}".format(atributo[0],atributo[1],atributo[2],atributo[3]))
    sn()
    ruta.close()




def gestion_carta_menu():
    while True:
        limpiarpantalla()
        print("\033[2;1;4;34m"+"SUBMENU: GESTION CARTA DE MENU "+"\033[0m")
        print("\033[3;2m"+"1 ingresar plato ")
        print("2 mostrar plato ")
        print("3 buscar plato ")
        print("0 regresar menu anterior "+"\033[0m")

        op=input(">>> opcion: ")
        limpiarpantalla()
        match(op):
            case "1":
                crearplato()
            case "2":
                mostrarplato()
            case "3":
                codigo=input("ingrese el codigo : ")
                fila= str(validar_codigo(codigo))
            case "0": 
                print(">>> regresando al menu anterior...")
                break
            case _: print(">>> opcion invalida...")

