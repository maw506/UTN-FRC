import time
import random

c_m=c_a=c_c=c_p= 0
r_e = r_t = 0


def patentealeatoria():
    t_p = 1,2
    t_p_a = random.choice(t_p)
    if t_p_a == 1:

        letras = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
        numeros = '0','1','2','3','4','5','6','7','8','9'

        letra1 = random.choice(letras)
        letra2 = random.choice(letras)
        letra3 = random.choice(letras)

        numero1 = random.choice(numeros)
        numero2 = random.choice(numeros)
        numero3 = random.choice(numeros)

        patente = letra1+letra2+letra3+numero1+numero2+numero3
    else:

        letras = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
        numeros = '0','1','2','3','4','5','6','7','8','9'

        letra1 = random.choice(letras)
        letra2 = random.choice(letras)
        letra3 = random.choice(letras)
        letra4 = random.choice(letras)

        numero1 = random.choice(numeros)
        numero2 = random.choice(numeros)
        numero3 = random.choice(numeros)

        patente = letra1+letra2+numero1+numero2+numero3+letra3+letra4

    return patente


def tipo_vehiculo():
    vehiculo = 'Moto', 'Auto', 'Camion'

    pase = random.choice(vehiculo)
    return pase


def tipo_pago():

    pago = 1,2 #1 efectivo,2 telepeaje
    pago_elejido = random.choice(pago)
    return pago_elejido


def carga_random():
    c_m = 0
    c_p = 0
    c_a = 0
    c_c = 0
    r_e = 0
    r_t = 0
    c_p += 1
    v_a = tipo_vehiculo()
    print(v_a)
    p_a = tipo_pago()
    if v_a == 'Moto':
        c_m += 1
    elif v_a == 'Auto':
        c_a += 1
    else:
        c_c += 1
    if p_a == 2:
        patente = patentealeatoria()
        print(patente)
    if tipo_pago() == 1:
        if tipo_vehiculo() == 'Moto':
            r_e += 20
        elif tipo_vehiculo() == 'Auto':
            r_e += 40
        else:
            r_e += 80
    else:
        if tipo_vehiculo() == 'Moto':
            r_t += 20
        elif tipo_vehiculo() == 'Auto':
            r_t += 40
        else:
            r_t += 80


def carga_manual():
    c_m = 0
    c_p = 0
    c_a = 0
    c_c = 0
    r_e = 0
    r_t = 0
    c_p += 1
    v_a = int(input("\ntipo de vehiculo: "))
    print(v_a)
    p_a = int(input("tipo de pago: "))
    if v_a == 'Moto':
        c_m += 1
    elif v_a == 'Auto':
        c_a += 1
    else:
        c_c += 1
    if p_a == 2:
        patente = input("Patente: ")
        print(patente)
    if p_a == 1:
        if v_a == 'Moto':
            r_e += 20
        elif v_a == 'Auto':
            r_e += 40
        else:
            r_e += 80
    else:
        if v_a == 'Moto':
            r_t += 20
        elif v_a == 'Auto':
            r_t += 40
        else:
            r_t += 80
    print(p_a, "\n")


def menu():
    op = 0
    dif = 0
    cantMoto = 0
    cantPases = 0
    cantAuto = 0
    cantCamiones = 0
    efectivo = 0
    telepeaje = 0
    cantPases += 1
    while op != 3:
        print("\nOPCIONES: \n1 = Para generar datos de forma automatica \n2 = Para ingresar datos de forma manual "
              "\n3 = Salir")
        op = int(input("\nIngrese una opcion: "))
        if op == 1:  # carga de datos automatica
            inicio = time.time()
            while dif < 15:
                # carga_random()

                vehiculo = tipo_vehiculo()
                print(vehiculo)
                pago = tipo_pago()
                if vehiculo == 'Moto':
                    cantMoto += 1
                elif vehiculo == 'Auto':
                    cantAuto += 1
                else:
                    cantCamiones += 1
                if pago == 2:
                    patente = patentealeatoria()
                    print(patente)
                if pago == 1:
                    if vehiculo == 'Moto':
                        efectivo += 20
                    elif vehiculo == 'Auto':
                        efectivo += 40
                    else:
                        efectivo += 80
                else:
                    if vehiculo == 'Moto':
                        telepeaje += 20
                    elif vehiculo == 'Auto':
                        telepeaje += 40
                    else:
                        telepeaje += 80

                time.sleep(3)
                final = time.time()
                dif = final - inicio
            print("\nTelepeaje: ", telepeaje, "\nEfectivo: ", efectivo, "\nMotos", cantMoto,
                  "\nCamiones", cantCamiones, "\nAutos: ", cantAuto, "\n",)
        elif op == 2:  # carga de datos de forma manual
            inicio = time.time()
            while dif < 15:

                final = time.time()
                dif = final - inicio
        elif op == 3:
            msj = "salir"
            break
        else:
            msj = "ERROR! opcion seleccionada no valida \nPorfavor elija de nuevo:"
    print(msj)


menu()
