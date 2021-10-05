"""ingresar un texto pot teclado, suponiendo que el texto finaliza con un punto.
informar la cantidad de palabras de la frase y el promedio de letras por palabra"""

txt = input("Ingrese el texto a valuar: ")

contL = 0
contP = 0
acumL = 0

"""
# mi metodo

for i in txt:
    contL += 1
    if i == ' ':
        contL -= 1
        contP +=1
    if i == '.':
        contL -= 1
        contP +=1
        break

print("contador: ", contP)
"""

# metodo del profe

for i in txt:
    if i != " " and i != '.':
        contL += 1
    else:
        if contL > 0:
            contP += 1
            acumL += contL
            contL = 0

prom = acumL / contP

print("Cantidad de Palabras: ", contP, "\nCantidad de Letras:", acumL, "\nPromedio de Letras: ", prom)
