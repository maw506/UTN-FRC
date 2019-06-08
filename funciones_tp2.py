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


def validarPatente(patente):

    letras = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numeros = '0123456789'

    contL = 0
    contN = 0
    caracteres = 0
    msj = 0
    long = len(patente)

    if long == 6:
        for i in patente:
            caracteres += 1
            if i in letras:
                contL += 1
                if contL > 3:
                    msj = "error patente ingresada"
            elif i in numeros:
                contN += 1
                if contN > 3:
                    msj = "error patente ignresada"
        print('patente')
    elif long == 7:
        pass
    else:
        msj = "Error, patente ingresada incorrecta"

    return msj


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
