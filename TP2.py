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


def validar_patente(patente):

    letras = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numeros = '0123456789'

    contL = 0
    contN = 0
    caracteres = 0
    msj = 0
    long = len(patente)

    if long == 6:
        for i in patente:
            if patente != '.':
                caracteres += 1
                if i in letras:
                    contL += 1
                    if contL > 3:
                        msj = "error patente ingresada"
                elif i in numeros:
                    contN += 1
                    if contN > 3:
                        msj = "error patente ignresada"
            else:
                break
    elif long == 7:
        pass
    else:
        msj = "Error, patente ingresada incorrecta"

    return msj


def mayor_hora(hora, pases):
    pas1 = 0
    pas2 = 0
    pas3 = 0
    pas4 = 0
    may = 0

    if hora == 10:
        pas1 = pases
    elif hora == 20:
        pas2 = pases
    elif hora == 30:
        pas3 = pases
    elif hora == 40:
        pas4 = pases

    if pas1 > pas2 and pas1 > pas3 and pas1 > pas4:
        may = pas1
    elif pas2 > pas3 and pas2 > pas4 and pas2 > pas1:
        may = pas2
    elif pas3 > pas4 and pas3 > pas1 and pas3 > pas2:
        may = pas3
    else:
        may = pas4

    return may


def carga_random():
    cantMoto = 0
    cantPases = 0
    cantAutos = 0
    cantCamiones = 0
    efectivo = 0
    telepeaje = 0
    cantT = 0
    cantE = 0
    cantPases += 1
    vehiculo = tipo_vehiculo()
    print(vehiculo)
    pago = tipo_pago()
    if vehiculo == 'Moto':
        cantMoto += 1
    elif vehiculo == 'Auto':
        cantAutos += 1
    else:
        cantCamiones += 1
    if pago == 2:
        patente = patentealeatoria()
        print(patente)
    if pago == 1:
        cantT += 1
        if vehiculo == 'Moto':
            efectivo += 20
        elif vehiculo == 'Auto':
            efectivo += 40
        else:
            efectivo += 80
    else:
        cantE += 1
        if vehiculo == 'Moto':
            telepeaje += 20
        elif vehiculo == 'Auto':
            telepeaje += 40
        else:
            telepeaje += 80

    return telepeaje, efectivo, cantCamiones, cantAutos, cantMoto, cantPases, cantE, cantT


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
    cantPases == 0

    while op != 3:
        print("\nOPCIONES: \n1 = Para generar datos de forma automatica \n2 = Para ingresar datos de forma manual "
              "\n3 = Salir")
        op = int(input("\nIngrese una opcion: "))
        if op == 1:  # carga de datos automatica
            inicio = time.time()
            while dif < 40:
                # carga_random()

                vehiculo = tipo_vehiculo()
                print(vehiculo)
                pago = tipo_pago()
                canT = 0
                canE = 0
                if vehiculo == 'Moto':
                    cantMoto += 1
                elif vehiculo == 'Auto':
                    cantAuto += 1
                else:
                    cantCamiones += 1
                if pago == 2:
                    canT += 1
                    patente = patentealeatoria()
                    print(patente)
                    if vehiculo == 'Moto':
                        telepeaje += 20
                    elif vehiculo == 'Auto':
                        telepeaje += 40
                    else:
                        telepeaje += 80
                if pago == 1:
                    canE += 1
                    if vehiculo == 'Moto':
                        efectivo += 20
                    elif vehiculo == 'Auto':
                        efectivo += 40
                    else:
                        efectivo += 80

                final = time.time()
                time.sleep(random.randint(1, 2))
                cantPases += 1
                dif = final - inicio
                mayor = mayor_hora(final, cantPases)
                total = telepeaje + efectivo


            print("\nTotal:", total, "\nTelepeaje:", telepeaje, "\nEfectivo:", efectivo, "\nMotos:", cantMoto,
                  "\nCamiones:", cantCamiones, "\nAutos:", cantAuto, "\nCantidad total de pases:", cantPases,
                  "\nmayor hora:", mayor)
        elif op == 2:  # carga de datos de forma manual
            inicio = time.time()
            while dif < 15:
                patente = input('ingrese una patente: ')
                print(validar_patente(patente))
                final = time.time()
                dif = final - inicio
        elif op == 3:
            msj = "salir"
            break
        else:
            msj = "ERROR! opcion seleccionada no valida \nPorfavor elija de nuevo:"
    print(msj)


menu()
