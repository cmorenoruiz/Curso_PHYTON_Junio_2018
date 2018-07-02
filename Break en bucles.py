#Dado un número, imprime su tabla de multiplicar,
# si el número es mayor de 100, solo imprime la tabla hasta el 5,
# nunca imprime el producto por el 7

numero=int(input("Dame un número "))
contador=1
while contador<=10:
    if contador==7:
        contador += 1
        continue
    print(f"{numero} * {contador} ={numero*contador}")
    if numero>100 and contador==5:
        break
    contador+=1


