
from datetime import datetime

""" la siguientes funciones devuelven el tiempo trancurrido
    *instanteInicial = datetime.now()
    *instanteFinal = datetime.now() 
    *tiempo = instanteFinal - instanteInicial # Devuelve un objeto timedelta
    *segundos = tiempo.seconds """

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