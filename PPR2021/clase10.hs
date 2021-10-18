generar_lista_pares:: [Int] -> [Int]
-- caso base
generar_lista_pares [] = []
-- definicion recursiva
generar_lista_pares (h:t) = if even h then h : generar_lista_pares t else generar_lista_pares t
