import random

def patentealeatoriatipo33():
    letras = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
    numeros = '0','1','2','3','4','5','6','7','8','9'

    letra1 = random.choice(letras)
    letra2 = random.choice(letras)
    letra3 = random.choice(letras)

    numero1 = random.choice(numeros)
    numero2 = random.choice(numeros)
    numero3 = random.choice(numeros)

    patente = letra1+letra2+letra3+numero1+numero2+numero3

    return patente

def patentealeatoriatipo232():
    letras = (
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
    'X', 'Y', 'Z')
    numeros = '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'

    letra1 = random.choice(letras)
    letra2 = random.choice(letras)
    letra3 = random.choice(letras)
    letra4 = random.choice(letras)

    numero1 = random.choice(numeros)
    numero2 = random.choice(numeros)
    numero3 = random.choice(numeros)

    patente = letra1+letra2+numero1+numero2+numero3+letra3+letra4

    return patente

t_p = patentealeatoriatipo33(),patentealeatoriatipo232()

patentealeatoria = random.choice(t_p)

print(patentealeatoria)

