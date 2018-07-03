def controlErrores():
    try:
        dividendo = int(input("Introduce dividendo:"))
        divisor = int(input("Introduce divisor:"))
        resultado=dividendo/divisor
        print(f"Resultado división: {resultado}")
    except ValueError:
        print("Error debes introducir un número")
        controlErrores()
    except ZeroDivisionError:
        print("Error no puedes dividir por cero")
        controlErrores()
    except:
        print("Error general. ¡Sabe dios qué habrá pasado!")
    finally:
        print("Lo que quiera ejecutar de todas maneras")

controlErrores()