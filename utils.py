import os
from unicodedata import name 

def limpiarpantalla():
    if os.name =="posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name =="dos":
        os.system("cls")

def sn():
    while True:
        op=input("Regresar S/N >>> ")
        if op == "s" or op == "S":
            break
        else:
            continue