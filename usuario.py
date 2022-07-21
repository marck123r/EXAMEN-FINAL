
from models import Usuario
from utils import limpiarpantalla,sn
import time

ruta_de_archivo="./archivos/usuario.txt"
def registrar_cliente():
        dni=input("DNI: ")
        pasword=input("Password: ")
        tipo=input("tipo: ")
        nombre_apellido=input("Nombres y apellidos: ")
        dirreccion=input("dirrecion: ")
        gmail=input("Gmail: ")

        plt=Usuario(dni,pasword,tipo,nombre_apellido,dirreccion,gmail)
        archivoplt= open(ruta_de_archivo, "a")
        archivoplt.write(str(plt))
        archivoplt.close()

def mostrar_usuarios():
    ruta= open(ruta_de_archivo, "r") 
    print("DNI \t\t PASSWORD \t TIPO \t\t NOMBREY APELLIDO \t DIRECCION \t\t \t GMAIL")
    for linea in ruta.readlines():
        atributo = linea.split(";")
        print("{} \t{} \t {} \t {} \t\t {} \t{}".format(
            atributo[0],atributo[1],atributo[2],atributo[3],atributo[4],atributo[5]),end="")
    sn()
    ruta.close()

def buscar_usuario(codigo):
    ruta= open(ruta_de_archivo, "r") 
    for linea in ruta.readlines():
        atributo = linea.split(";")
        if codigo == atributo[0]:
            print("{}\t{}\t{}\t{}\t{}\t{}".format(atributo[0],atributo[1],atributo[2],atributo[3],atributo[4],atributo[5]))
    sn()
    ruta.close()

def acceso_admin(dni, password):
    ruta= open(ruta_de_archivo, "r") 
    for linea in ruta.readlines():
        atributo = linea.split(";")
        if dni == atributo[0] and password==atributo[1] and atributo[2]=="admin  ":
            return True
    ruta.close()
    return False

def acceso_cliente(dni,password):
    ruta= open(ruta_de_archivo, "r") 
    for linea in ruta.readlines():
        atributo = linea.split(";")
        if dni == atributo[0] and password==atributo[1] and atributo[2]=="cliente":
            return True
    ruta.close()
    return False


def gestion_usuario():
    while True:
        limpiarpantalla()
        print("\033[2;1;4;34m"+"|SUBMENU: GESTION DE USUARIOS |"+"\033[0m")
        print("\033[3;2m"+"1 Ingresar usuario ")
        print("2 Mostrar usuario ")
        print("3 buscar usuario por DNI")
        print("0 Regresar menu principal")

        op =input("Opcion: "+"\033[0m")
        limpiarpantalla()
        match(op):
            case "1":
                registrar_cliente()
            case "2":
                mostrar_usuarios()
            case "3":
                dni=input("ingrese el DNI: ")
                buscar_usuario(dni)
            case "0":
                print(">>> regresando al menu principal ...")
                break
            case _:
                time.sleep(1)
                print(">>> opcion invalida... ")
