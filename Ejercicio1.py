#Pedir número por teclado al usuario. Hay que mostrar opr pantalla si es par o impar
print("Dame un número: ")
num=int(input())
if num==0:
    print("El cero también es par")
elif (num%2)==0:
    print("El número ",num," es par")
else:
    print("El número ",num," no es par")
