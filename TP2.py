
import time
import random


def menu():
    op = 0
    dif = 0
    while op != 3:
        print("\nOPCIONES: \n1 = Para generar datos de forma automatica \n2 = Para ingresar datos de forma manual \n3 = Salir")
        op = int(input("\nIngrese una opcion: "))
        if op == 1: # carga de datos automatica
            inicio = time.time()
            while dif < 240:
                auto = input("ingrese auto: ")
                pause = time.sleep(1)
                final = time.time()
                dif = final - inicio
        elif op == 2: # carga de datos de forma manual
            inicio = time.time()
            while dif < 240:
                auto = input("ingrese auto: ")
                pause = time.sleep(1)
                final = time.time()
                dif = final - inicio
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

menu()
