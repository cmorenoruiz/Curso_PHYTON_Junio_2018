#Mostrar la conjeturade Collatz dado un número
#Si el número es par, se divide entre 2.
#Si el número es impar, se multiplica por 3 y se suma 1.

numero=int(input("Dame un número "))

while numero>1:
    if numero%2==0:
        numero/=2
    else: numero=numero*3+1
    print(numero)

