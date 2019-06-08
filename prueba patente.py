c_c = c_l = c_n = 0

letras = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W', 'X','Y', 'Z')
numeros = '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
patente = input()
patente2 = ""
for car in patente:
    if car == ' ' or car == '.':
        if c_c == 6:
            print(patente2)
    elif car in letras:
        c_l +=1
        c_c +=1
        patente2 += car
        if c_l == 4:
            break
    elif car in numeros:
        if c_l == 3:
            c_n += 1
            c_c += 1
            patente2 += car
        else:
            break


