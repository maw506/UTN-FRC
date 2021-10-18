-- Consigna 1) implementar las siguientes funciones en haskell
-- cant_km_capsula_organica
-- cant_km_capsula_inorganica

cant_km_capsula_organica:: Float -> Int -> Float
cant_km_capsula_organica peso vencida = if vencida == 1 && peso >= 0 then peso * 0.05 else -1

cant_km_capsula_inorganica:: Float -> Int -> Float
cant_km_capsula_inorganica peso tipo | tipo == 1 = if peso >= 0 then peso * 0.10 else -1
                                     | tipo == 2 = if peso >= 0 then peso * 0.25 else -1
                                     | tipo == 3 = if peso >= 0 then peso * 0.15 else -1
                                     | otherwise = -1

--Consigna 2) implementar la funcion cant_km
-- reutilizar las funciones creadas en la consigna 1)

cant_km:: String -> Float -> Int -> Float
cant_km cap peso x | cap == "o" = cant_km_capsula_organica peso x
                   | cap == "O" = cant_km_capsula_organica peso x
                   | cap == "i" = cant_km_capsula_inorganica peso x
                   | cap == "I" = cant_km_capsula_inorganica peso x
                   | otherwise = -1

-- Consigna 3) implemetar la funcion lista_cant_km
lista_cant_km:: [String] -> [Float] -> [Int] -> [Float]
lista_cant_km [] [] [] = []
lista_cant_km (c:cl) (p:pl) (x:xl) = cant_km c p x : lista_cant_km cl pl xl

-- Consigna 4) Implementar la funcion lista_tuplas_capsulas

{-descripcion:: Char -> String
descripcion x | x == 'o' = "Organica"
              | x == 'O' = "Organica"
              | x == 'i' = "Inorganica"
              | x == 'I' = "Inorganica"
              | otherwise = "Indefinido"


lista_tuplas_capsulas:: [Char] -> [(Int, Int)] -> [(String, Int, Int, Float)]
lista_tuplas_capsulas [] [] = []
lista_tuplas_capsulas (h_cod_cap:t_cod_cap) (h_cap, t_cap) = (descripcion (h_cod_cap), fst h_cap, snd h_cap, cant_km (h_cod_cap fst h_cap snd h_cap)) : lista_tuplas_capsulas t_cod_cap t_cap
-}

--consigna 5) implementar la funcion prom_cant_km
--contar:: [Float] -> Int

contar_lista [] = 0
contar_lista (h:t) = 1 + contar_lista (t)

sumar_lista:: [Float] -> Float
sumar_lista [] = 0
sumar_lista (h:t) = h + sumar_lista(t)

prom_cant_km:: [String] -> [Float] -> [Int] -> Float
prom_cant_km [] [] [] = 0
prom_cant_km (c:cl) (p:pl) (x:xl) = sumar_lista (lista_cant_km (c:cl) (p:pl) (x:xl)) / contar_lista (lista_cant_km (c:cl) (p:pl) (x:xl))


-- consigna 6) calcular e^x siendo x un valor dado y n un valor secundario de tope
factorial:: Int -> Int
factorial 0 = 1
factorial n = n * factorial(n-1)
funcion6:: Int -> Int -> Float
funcion6 x n |n == 0 = 1
             |otherwise = fromIntegral((x^n)) / fromIntegral(factorial n) + funcion6 x (n-1)
