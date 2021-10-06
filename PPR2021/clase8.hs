-- la funcion cuadrado toma un numero y lo eleva al cuadrado

-- signatura o firma de la funcion

cuadrado:: Int -> Int

-- nombre de la funcion + argumentos = implementacion

cuadrado x = x * x

-- funcion cubo toma un numero y lo eleva al cubo

cubo:: Int -> Int

cubo x = x ^ 3


-- Ejercicio
-- Calcular el IMC de una persona
-- es igual al peso dividido el cuadrado de la altura

-- funcion parcializada
imc:: Int -> Float -> Float

imc peso altura = (fromIntegral peso) / altura ^ 2

-- usamos la funcion fromIntegral por que al recibir un int se debe convertir
-- a float para poder operar


--funcion no parcializada
imc2:: (Float, Float) -> Float

imc2 (peso, altura) = peso / altura ^ 2

-- funcionalmente son lo mismo, pero en diferencia que la segunda recibe un par
-- ordenado. No olvidar que esta al llamado se deben de usar tambien los ()
-- en win se escribe el llamado a imc2 (90, 1.8)


menor:: Int -> Int -> Int
menor a b = if a > b then b else a

-- en el then es el valor que retorna o en el else en caso de ser False
-- si se pueden hacer condiciones anidadas

-- recibe un entero y devuelve un booleano
-- se puede hace como
-- esPar a = if mod x 2 == 0 then True else False
-- pero no es correcto dado que estamos haciendo una valuacion siendo que
-- se muestra como retorna bool

esPar:: Int -> Bool
esPar x = mod x 2 == 0

evaluarEntero:: Int -> String
evaluarEntero x = if x > 0 then "Es Positivo" else (if x < 0 then "Es Negativo" else "Es Cero")

-- los parantesis no son necesarios pero contribuyen a lectura del codigo
-- en la llamada siendo negativo se llamaria como (-3)

evaluarEntero2:: Int -> String
evaluarEntero2 x | x > 0 = "Es positivo."
                 | x < 0 = "Es negativo."
                 | x == 0 = "Es cero."

-- esta es otra forma de hacerlo para poder hacer condiciones anidadas


evaluarEntero3:: Int -> String
evaluarEntero3 x | x > 0 = "Es positivo.."
                 | x < 0 = "Es negativo.."
                 | otherwise = "Es cero.."

-- en esta se usa otherwise para cualquier otro caso distinto de los escritos


--ejercicio de la guia 8
evaluarPolinomio:: Int -> String
evaluarPolinomio x | x ^ 2 + 5 * x + 0 > 0 = "Es positivo.."
                   | x ^ 2 + 5 * x + 0 < 0 = "Es negativo.."
                   | otherwise = "Es cero.."


evaluarPolinomio2:: Int -> String
evaluarPolinomio2 x | y > 0 = "Es positivo.."
                    | y < 0 = "Es negativo.."
                    | otherwise = "Es cero.."
                    where y = x ^ 2 + 5 * x + 0

-- where se utiliza para variables temporales

-- si todas las guardas comparan la misma variable con varios valores por igualdad
-- se pued eporgramar un case


diaSemana:: Int -> String
diaSemana d | d == 0 = "Domingo"
            | d == 1 = "Lunes"
            | d == 2 = "Martes"
            | d == 3 = "Miercoles"
            | d == 4 = "Jueves"
            | d == 5 = "Viernes"
            | d == 6 = "Sabado"
            | otherwise = "ERROR!"

diaSemana2:: Int -> String
diaSemana2 d = case d of
           0 -> "Domingo"
           1 -> "Lunes"
           2 -> "Martes"
           3 -> "Miercoles"
           4 -> "Jueves"
           5 -> "Viernes"
           6 -> "Sabado"
           otherwise = "ERROR!"
