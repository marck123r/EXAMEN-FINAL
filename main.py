import getpass
from lista import imprimir
from utils import limpiarpantalla
import time
from cartamenu import carta_menu
from gestion import gestion_carta_menu
from usuario import gestion_usuario,acceso_admin,acceso_cliente
from cartamenu import dato

def run():
    while True:
        limpiarpantalla()
        print("\033[4;36m"+"** GESTION DEL RESTAURANT **")
        print("=============================="+"\033[0m")
        print("\033[31m"+"1 gestion de menu  " )
        print("2 Gestion de usuarios  ")
        print("0 Salir "+"\033[0m")
        op=input(">>> digite una opcion: ")
        limpiarpantalla()
        match (op):
            case "1":
                time.sleep(0.5)
                gestion_carta_menu()
            case "2":
                time.sleep(1)
                gestion_usuario()
            case "0": 
                print(">>> saliendo del sistema... ")
                time.sleep(2)
                exit()
            case _:
                print("opcion incorrecta")
                time.sleep(1)
                limpiarpantalla()


def client():    
    while True:
        limpiarpantalla()
        print("\033[4;36m"+"** RESTAURANT EL BUEN SABOR **")
        print("=============================="+"\033[0m")
        print("1 Carta menu " )
        print("2 imprimir ")
        print("0 salir ")
        op=input("digite una opcion ")
        limpiarpantalla()
        match (op):
            case "1":
                carta_menu()
                time.sleep(2)
                limpiarpantalla()

            case "2":
                imprimir()

            case "0": 
                
                limpiarpantalla()
                print("saliendo del sistema")
                time.sleep(2)
                exit()
            case _:
                print("opcion incorrecta")
                time.sleep(2)
                limpiarpantalla()

def admin():
    acumulador=0
    while True and acumulador!=3 :
        acumulador += 1
        limpiarpantalla()
        users=input("ingrese usuario: ")
        password= getpass.getpass("ingrese el password: ")
        if acceso_admin(users,password):
            acumulador=0
            run()
        else :
            print("contraseña incorrecta")
            time.sleep(1)
            limpiarpantalla()



def cliente():
    acumulador=0
    while True and acumulador!=3 :
        acumulador += 1
        limpiarpantalla()
        users=input("ingrese usuario: ")
        password= getpass.getpass("ingrese el password: ")
        if acceso_cliente(users,password):
            dato(users)
            acumulador=0
            client()
        else :
            print("contraseña incorrecta")
            time.sleep(1)
            limpiarpantalla()
        

        
def main():
    limpiarpantalla()
    while True:
        print("1.-USUARIO ADMIN")
        print("2.-USUARIO CLIENTE")
        print("3.-salir ")
        op=input(">>> ")
        match(op):
            case "1": admin()
            case "2": cliente()
            case "3": exit()
            case _:
                print("opcioin invalida")
                limpiarpantalla()




if __name__ == "__main__":
    main()