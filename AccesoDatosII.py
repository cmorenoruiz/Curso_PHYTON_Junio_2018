import mysql.connector as bd

bd_conexion = bd.connect(host='localhost', port='3306',
                                   user='root', password='', database='Hospital')
cursor = bd_conexion.cursor()
try:
    cursor.execute("SELECT apellido as 'Apellido Doctora', nombre as 'Hospital' from doctor, hospital where doctor.hospital_cod=hospital.hospital_cod")

    for apellido, nombre in cursor:
        print(f"Apellido: {apellido}",end=" ")
        print("Hospital: " + nombre)

except bd_conexion.Error as error:
    print("Error: ",error)

bd_conexion.close()
