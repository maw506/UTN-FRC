patente = input()
def validar_patente_LLLNNN(patente):

    contador_caracteres = contador_letras = contador_numeros = 0

    letras = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W', 'X','Y', 'Z')
    numeros = '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
    patente2 = ""
    validar = True
    for car in patente:

        if car == ' ' or car == '.':
            if contador_caracteres == 6:
                break
        elif car in letras:
            contador_letras +=1
            contador_caracteres +=1
            patente2 += car
            if contador_letras == 4:
                validar = False
                break
        elif car in numeros:
            if contador_letras == 3:
                contador_numeros += 1
                contador_caracteres += 1
                patente2 += car
            else:
                validar = False
                break

    return validar

print(validar_patente_LLLNNN(patente))