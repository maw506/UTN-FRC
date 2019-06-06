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



