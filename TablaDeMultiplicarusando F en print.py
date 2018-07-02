#Dado un número, imprime su tabla de multiplicar
numero=int(input("Dame un número "))
contador=1
while contador<=10:
    print(f"{numero} * {contador} ={numero*contador}")
    contador+=1

