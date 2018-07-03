class DNI():

    def __init__(self):
        letra = ""
        numero = 0

    def __init__(self,numero):
       self.numero=numero
       self.letra=self.calculaLetra(self.numero)

    def calculaLetra(numero):
        resto = numero % 23
        letrasDni = "TRWAGMYFPDXBNJZSQVHLCKET";
        return letrasDni[resto]

