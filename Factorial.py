#Dado un número, imprime su factorial

numero=int(input("Dame un número "))
contador=1
factorial=1
print(f"{numero}!=", end="")
while contador<numero:
    print(f"{contador} * ", end="")
    factorial*=contador
    contador+=1
factorial*=contador
print(f"{contador}= {factorial}")