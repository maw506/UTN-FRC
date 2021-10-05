patente2 = "AB123CD."
patente1 = "ABC123."


def validarPatente(patente):

    letras = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numeros = '0123456789'

    contL = 0
    contN = 0
    caracteres = 0

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

    elif long == 7:
        pass
    else:
        msj = "Error, patente ingresada incorrecta"

    return msj



