
class DNI:

    def __init__(self, numero=None):
       if numero==None:
           self.letra = ""
           self.numero = 0
       else:
           self.numero=numero
           self.letra=self.calculaLetra(numero)

    def calculaLetra(self,numero):
        devolver="error"
        try:
            if isinstance(numero,int):
                resto = numero % 23
                letrasDni = "TRWAGMYFPDXBNJZSQVHLCKET"
                devolver=letrasDni[resto]
            else:
                devolver="error"
        except:
            devolver="error"
        finally:
            return devolver
    def __str__(self):
        return "Número: "+str(self.numero) +", Letra: " + self.letra