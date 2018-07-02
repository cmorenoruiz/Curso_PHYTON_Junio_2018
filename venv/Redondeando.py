print("-----------Redondeando--------------")
# Comentario de una línea
# Ejemplo de redondeo inferior y superior, floor y ceil
num1=20
num2=3
resultado=num1/num2
print("resultado sin redondear", resultado)
resultado=round(num1/num2,3)
print("resultado redondeado con la función round a tres decimales", resultado)

"""Comentario de varias líneas entre tres comillas dobles"""

"""Importamos librerías"""

from math import floor,ceil

resultado=floor(num1/num2)
print("Resultdo de redondeo al número entero inferior con la función floor", resultado)


resultado=ceil(num1/num2)
print("Resultdo de redondeo al número entero superior con la función ceil", resultado)