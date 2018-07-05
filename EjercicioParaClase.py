import mysql.connector as bd

bd_conexion = bd.connect(host='localhost', port='3306',
                                   user='root', password='', database='Hospital')
cursor = bd_conexion.cursor()
try:
    departamento=input("Introduce Nombre del Departamento:")
    consulta= "SELECT emp.apellido FROM emp, dept WHERE emp.DEPT_NO=dept.DEPT_NO && dept.dnombre=%s"
    cursor.execute(consulta,(departamento,))
    # Si en un único parámetro tenemos que poner ',' a continuación del valor de la variable
    resultado=False
    for apellido in cursor:
        print("Apellido: ", apellido)
        #print("departamento", caca)
        resultado=True
    if not resultado:
        print("Sin resultados para el departamento ",departamento)
except bd_conexion.Error as error:
    print("Error: ",error)

bd_conexion.close()

