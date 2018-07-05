from datetime import date
import mysql.connector as bd

try:
    bd_conexion = bd.connect(host='localhost', port='3306',
                                       user='root', password='', database='Hospital')
    cursor = bd_conexion.cursor()

    numeroDepartamento=input("Introduce número de departamento: ")
    nombreDepartamento=input("Introduce nombre de departamento: ")
    localizacionDepartamento=input("Introduce localización de departamento: ")

    consultaAlta = ("INSERT INTO dept VALUES (%s, %s, %s)")
    datosDepartamento = (numeroDepartamento,nombreDepartamento,localizacionDepartamento)

    cursor.execute(consultaAlta, datosDepartamento)

    bd_conexion.commit()
    print("Datos grabados")
    cursor.close()
    bd_conexion.close()
except:
    print("Error no se ha podido conectar o escribir en la BD")