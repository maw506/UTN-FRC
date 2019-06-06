
import time
import random

def menu():
    op = 0
    while op != 3:
        print("\nOPCIONES: \n1 = Para generar datos de forma automatica \n2 = Para ingresar datos de forma manual \n3 = Salir")
        op = int(input("\nIngrese una opcion: "))
        if op == 1:
            msj = "eligio 1"
        elif op == 2:
            msj = "eligio 2"
        elif op == 3:
            msj = "salir"
            break
        else:
            msj = "ERROR! opcion seleccionada no valida \nPorfavor elija de nuevo:"
    print(msj)


""" la siguientes funciones devuelven el tiempo trancurrido
    *instanteInicial = datetime.now()
    *instanteFinal = datetime.now() 
    *tiempo = instanteFinal - instanteInicial # Devuelve un objeto timedelta
    *segundos = tiempo.seconds """

vehiculo = 'Moto', 'Auto', 'Camion'
letras = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numeros = '0123456789'

<<<<<<< HEAD
inicio = time.time()
menu()
final = time.time()

tiempo = inicio - final

print('tiempo:', tiempo)
=======
instanteInicial = datetime.now()
op = 0
while op != 3:
    print("\nOPCIONES: \n1 = Para generar datos de forma automatica \n2 = Para ingresar datos de forma manual \n3 = Salir")
    op = int(input("\nIngrese una opcion: "))
    if op == 1:
        print("eligio 1")
    elif op == 2:
        print("eligio 2")
    elif op == 3:
        print("salir")
        break
    else:
        print("ERROR! opcion seleccionada no valida \nPorfavor elija de nuevo:")

instanteFinal = datetime.now()
tiempo = instanteFinal - instanteInicial # Devuelve un objeto timedelta
segundos = tiempo.seconds

print("segundos:", segundos)

if op = 1:
    print('Ingrese tipo de vehiculo')
>>>>>>> f61996f04da64e32d0833afd526688878389fa81
