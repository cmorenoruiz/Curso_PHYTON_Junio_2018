#Definir una función sin y con parámetros y llamrla desde cualquier punto del programa

def calcularIVA():
    #Pide un importe y lo imprime multipliicado por su IVA
    importe = int(input("Precio del producto: "))
    total=importe*1.21
    print(f"IVA incluido (21%) : {total}")
    return

def calcularIVAconParametroNoDevuelve(importe):
    #Recibe un importe y lo imprime multipliicado por su IVA
    total=importe*1.21
    print(f"Precio del importe {importe} IVA incluido (21%) : {total}")
    return

def calcularIVAconParametroQueDevuelve(importe):
    #Recibe un importe y lo imprime multipliicado por su IVA
    total=importe*1.21
    return total

def calcularIVAconParametroQueDevuelveVariosValores(importe):
    #Recibe un importe y lo imprime multipliicado por su IVA
    total=importe*1.21
    return importe,total


print("Llamando  la función sin parámetros")
calcularIVA()

print("Llamando  la función sin parámetros")
calcularIVAconParametroNoDevuelve(500)

print("Llamando  la función con parámetro que devuelve y yo imprimo")
print(f"Me ha devuelto esto: {calcularIVAconParametroQueDevuelve(500)}")

print("Llamando  la función con parámetro que devuelve varios valores y yo imprimo")
print(f"Me ha devuelto esto: {calcularIVAconParametroQueDevuelveVariosValores(500)}")
print("Partido en varias lineas")
precio,resultado=calcularIVAconParametroQueDevuelveVariosValores(500)
print(f"Me ha devuelto esto: {precio} y {resultado}")




