#Dado un número, imprime su tabla de multiplicar
numero=int(input("Dame un número: "))

for contador in range(11):
    print(numero,"*",contador,"=",numero*contador)

