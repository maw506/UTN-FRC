patente1 = "ABC123"
patente2 = "AB123CD"

letras = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numeros = '0123456789'

contL = 0
contN = 0
caracteres = 0

for i in patente2:
    caracteres += 1
    if i in letras:
        contL += 1
        if contL > 3:
            print("error de patente")
    elif i in numeros:
        pass

    print(caracteres)
