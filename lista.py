import imp
from utils import limpiarpantalla,sn
#from pago import comp

ruta_usuarios="./archivos/usuario.txt"
ruta_menu="./archivos/carta_menu.txt"
cadena=''
#aux=['76772797','contraseña']
ran=[]
aux=[]

newc=''

#dni=str(aux[0])
#entre=str(entr[0])
name=[]

def validacion(dni):
    cadena=''
    ruta= open(ruta_usuarios, "r") 
    for linea in ruta.readlines():
        atributo = linea.split(";")
        if dni == atributo[0]:
            print("{} {} {} {}".format(atributo[0],atributo[1],atributo[2],atributo[3]))
            name=str(atributo[3])
            print(name)
    ruta.close()


    newc="./archivos/"+name+".txt"
    ran.append(newc)   

#validacion(dni)
def imprimir(cadena):
    archivo=open(cadena)
    print(archivo.read)

def agregar_lista(entre):
    cadena=''
    ruta= open(ruta_menu, "r") 
    for i in ran:
        cadena += str(i)
    for linea in ruta.readlines():
        atributo = linea.split(";")
        if entre == atributo[0]:
            print("{}\t {}\t {}".format(atributo[0],atributo[1],atributo[3]))
            case= atributo[0]+'\t'+atributo[1]+'\t'+atributo[3]
            with open(cadena,"a") as f:
                f.write(str(case))
    ruta.close()

