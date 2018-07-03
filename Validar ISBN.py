#Validar SBN de 10 dígitos


ISBN=input("Dame un número ")
resultado=0
for contador in range(0,10):
    resultado+=(contador+1)*int(ISBN[contador])
if resultado%11==0:
    print("ISBN correcto")
else:
    print("ISBN incorrecto")