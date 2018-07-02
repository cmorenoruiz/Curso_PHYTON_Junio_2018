print("---------------Sentencia IF--------------------")
edad=20
if edad==20:
    print("Tienes 20 años")
if edad==10:
    print("Tienes 10 años")

print("---------------Sentencia IF-ELSE--------------------")
edad=20
if edad<18:
    print("Eres menor de edad")
else:
    print("Eres mayor de edad")
print("Esto se imprime siempre, está fuera del else")

print("---------------Sentencia IF-ELIF-ELSE--------------------")
edad=20
if edad<18:
    print("Eres menor de edad")
elif edad==20:
    print("Tienes justo 20 años, dentro del elif")
else:
    print("Ni menor de 18, ni 20. Sentencia else")