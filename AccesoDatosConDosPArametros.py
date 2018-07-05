import mysql.connector as bd

bd_conexion = bd.connect(host='localhost', port='3306',
                                   user='root', password='', database='Hospital')
cursor = bd_conexion.cursor()
try:
    limiteInferior=input("Introduce límite inferior del salario:")
    limiteSuperior=input("Introduce límite inferior del salario:")

    consulta=("SELECT apellido,salario FROM emp where salario>=%s and salario<%s")
    cursor.execute(consulta,(limiteInferior,limiteSuperior))
    # Si en un único parámetro tenemos que poner ',' a continuación del valor de la variable
    resultado=False
    for apellido, salario in cursor:
        print("Apellido: ", apellido)
        print("Salario: " , str(salario))
        resultado=True
    if not resultado:
        print("Sin resultados")
except bd_conexion.Error as error:
    print("Error: ",error)

bd_conexion.close()

