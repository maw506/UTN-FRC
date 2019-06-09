import time
import random

def patentealeatoria():
    t_p = 1,2  #se define los tipos de: 1 = LLLNNN, 2 = LLNNNLL
    t_p_a = random.choice(t_p) #elije un tipo de patente
    if t_p_a == 1: #se elije la patente de tipo LLLNNN
        # se definen las letras y numeros
        letras = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
        numeros = '0','1','2','3','4','5','6','7','8','9'
        # se crean 3 variables con letras aleatorias
        letra1 = random.choice(letras)
        letra2 = random.choice(letras)
        letra3 = random.choice(letras)
        # se crean 3 variables con numeros aleatorios
        numero1 = random.choice(numeros)
        numero2 = random.choice(numeros)
        numero3 = random.choice(numeros)
        # se suman las variables para formar la patente
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
    #esta funcion elije un tipo de vehiculo aleatorio
    vehiculo = 'Moto', 'Auto', 'Camion'

    pase = random.choice(vehiculo)
    return pase


def tipo_pago():
    #esta funcion elije un tipo de pago aleatorio,ya sea en efectivo o con telepeaje
    pago = 1,2 #1 efectivo,2 telepeaje
    pago_elejido = random.choice(pago)
    return pago_elejido


def validar_patente(patente):

    contador_caracteres = contador_letras = contador_numeros = 0

    letras = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
    numeros = '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
    long = len(patente)
    validar = True
    banderaParaLLNNNLL = True
    for car in patente:
        if long == 6:
            if car == ' ' or car == '.':
                if contador_caracteres == 6:
                    break
            elif car in letras:
                contador_letras +=1
                contador_caracteres +=1
                if contador_letras == 4:
                    validar = False
                    break
            elif car in numeros:
                if contador_letras == 3:
                    contador_numeros += 1
                    contador_caracteres += 1
                else:
                    validar = False
                    break
            elif car not in letras and car not in numeros:
                validar = False
                break
        elif long == 7:

            if car == ' ' or car == '.':
                if contador_caracteres == 7:
                    break
            elif car in letras:
                contador_letras += 1
                contador_caracteres += 1
                if banderaParaLLNNNLL == True:
                    if contador_letras == 3:
                        validar = False
                        break

            elif car in numeros:
                if contador_letras == 2:
                    contador_numeros += 1
                    contador_caracteres += 1
                    if contador_letras == 2:
                        banderaParaLLNNNLL = False
                else:
                    validar = False
                    break

        else:
            validar = False
    return validar


def menu():
    dif = 0
    cantMoto = 0
    cantPases = 0
    cantAuto = 0
    cantCamiones = 0
    efectivo = 0
    telepeaje = 0
    mayor = 0
    op = 0
    canT = 0
    canE = 0
    patente = 0
    hora = 0
    mayPass1 =0
    mayPass2 = 0
    mayPass3 = 0
    mayPass4 = 0
    corteCargaManual = True
    while op != 3:
        print("\nOPCIONES: \n1 = Para generar datos de forma automatica \n2 = Para ingresar datos de forma manual "
              "\n3 = Procesar Datos \n4 = salir")
        op = int(input("\nIngrese una opcion: "))
        if op == 1:  # carga de datos automatica

            inicio = time.time()
            while dif < 240:
                vehiculo = tipo_vehiculo()
                pago = tipo_pago()

                if vehiculo == 'Moto':
                    cantMoto += 1
                elif vehiculo == 'Auto':
                    cantAuto += 1
                else:
                    cantCamiones += 1
                if pago == 2:
                    canT += 1
                    patente = patentealeatoria()
                    if vehiculo == 'Moto':
                        telepeaje += 20
                    elif vehiculo == 'Auto':
                        telepeaje += 40
                    else:
                        telepeaje += 80
                if pago == 1:
                    canE += 1
                    patente = 0
                    if vehiculo == 'Moto':
                        efectivo += 20
                    elif vehiculo == 'Auto':
                        efectivo += 40
                    else:
                        efectivo += 80

                print("\nVehiculo:", vehiculo, "\nPatente:", patente)

                final = time.time()
                time.sleep(random.randint(1, 2))
                cantPases += 1
                dif = final - inicio

                if 59 < dif < 61:
                    mayPass1 = cantPases
                elif 119 < dif < 121:
                    mayPass2 = cantPases
                elif 179 < dif < 181:
                    mayPass3 = cantPases
                elif 238 < dif < 240:
                    mayPass4 = cantPases

                if mayPass1 > mayPass2 and mayPass1 > mayPass3 and mayPass1 > mayPass4:
                    hora = 1
                elif mayPass2 > mayPass3 and mayPass2 > mayPass4 and mayPass2 > mayPass1:
                    hora = 2
                elif mayPass3 > mayPass4 and mayPass3 > mayPass1 and mayPass3 > mayPass2:
                    hora = 3
                else:
                    hora = 4

        elif op == 2:  # carga de datos de forma manual

            inicio = time.time()
            while dif < 240:
                op2 = -1
                while op2 != 2:
                    print("\nOPCIONES: \n1 = Pago en efectivo \n2 = Telepeaje \n3 = Salir")
                    op2 = int(input("Ingrese forma de pago: "))
                    if op2 == 1:
                        canE += 1
                        cantPases += 1
                        print("\nOPCIONES: \n1 = Auto \n2 = Moto \n3 = camion")
                        vehiculo = int(input("ingrese tipo de vehiculo: "))
                        if vehiculo == 1:
                            cantAuto += 1
                            efectivo += 40
                        elif vehiculo == 2:
                            cantMoto += 1
                            efectivo += 20
                        elif vehiculo == 3:
                            cantCamiones += 1
                            efectivo += 80
                        else:
                            print("opcion ingresada es invalida")
                    elif op2 == 2:
                        canT += 1
                        cantPases += 1
                        print("\nOPCIONES: \n1 = Auto \n2 = Moto \n3 = camion")
                        vehiculo = int(input("ingrese tipo de vehiculo: "))
                        patente = input("ingrese la patente del vehiculo: ").upper()
                        if validar_patente(patente) == True:
                            if vehiculo == 1:
                                telepeaje += 40
                            elif vehiculo == 2:
                                telepeaje += 20
                            elif vehiculo == 3:
                                telepeaje += 80
                        else:
                            print("La Patente ingresada es incorrecta, por favor ingresela de nuevo")
                    elif op2 == 3:
                        print("salir")
                        corteCargaManual = False
                        break
                    else:
                        print("opcion ingresada es invalida")
                final = time.time()
                dif = final - inicio
                if 59 < dif < 61:
                    mayPass1 = cantPases
                elif 119 < dif < 121:
                    mayPass2 = cantPases
                elif 179 < dif < 181:
                    mayPass3 = cantPases
                elif 238 < dif < 239:
                    mayPass4 = cantPases

                if mayPass1 > mayPass2 and mayPass1 > mayPass3 and mayPass1 > mayPass4:
                    hora = 1
                elif mayPass2 > mayPass3 and mayPass2 > mayPass4 and mayPass2 > mayPass1:
                    hora = 2
                elif mayPass3 > mayPass4 and mayPass3 > mayPass1 and mayPass3 > mayPass2:
                    hora = 3
                else:
                    hora = 4
                if corteCargaManual == False:
                    break

        elif op == 3:
            total = telepeaje + efectivo
            prom = (canE + canT) / 4
            if canT > canE:
                masUsado = "telepeaje"
            else:
                masUsado = "efectivo"

            print("\nTotal: $",total, "\nTelepeaje: $",telepeaje, "\nEfectivo: $",efectivo, "\nMotos:", cantMoto,
                  "\nCamiones:", cantCamiones, "\nAutos:", cantAuto, "\nCantidad total de pases:", cantPases,
                  "\nMetodo de pago mas usado:", masUsado, "\nPromedio de pases por hora: ",
                  prom, "\nLa hora pico fue:", hora,"º")
            input()
        elif op == 4:
            print("salir")
            break
        else:
            print("ERROR! opcion seleccionada no valida \nPorfavor elija de nuevo:")

x = "*" * 25

print("\n" ,x, "\n\tSistema de Peaje\n", x, "\n\tA continuacion se le muestran las\n"
                                            "\topciones que puede poner en funcionamiento")
menu()
