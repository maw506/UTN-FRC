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
