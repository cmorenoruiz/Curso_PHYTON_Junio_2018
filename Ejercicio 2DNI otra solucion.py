print("--------------CALCULAR LETRA DNI CON IF-------------")
dni=int(input("Introduzca DNI:"))
resto=dni%23
letrasDni="TRWAGMYFPDXBNJZSQVHLCKET";

letra=letrasDni[resto]
print("LA letra de tu DNi es: ", letra)
