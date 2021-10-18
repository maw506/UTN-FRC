estado_academico:: Float -> Flaot -> Float -> String
estado_academico n1 n2 n3 | hay_nota_menor4 n1 n2 n3 = "libre"
                          | hay_nota_menor7 n1 n2 n3 || promedio n1 n2 n3 < 8 "regular"
                          | otherwise = "Promocion"

hay_nota_menor4 n1 n2 n3 = n1 < 4 || n2 < 4 || n3 < 4

hay_nota_menor7 n1 n2 n3 = n1 < 7 || n2 < 7 || n3 < 7

promedio n1 n2 n3 = (n1 + n2 + n3) / 3
