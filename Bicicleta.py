class Bicicleta:
    color = "roja"
    tamanio = "25"
    velMax=15
    def __init__(self):
        self.velocidad = 0
    def __str__(self):
        return "Color: "+str(self.color)+ ", Tamaño: "+str(self.tamanio)+", Velocidad actual: "+str(self.velocidad)+" y Velocidad Máxima: "+str(self.velMax)

    def subirMarcha (self):
        self.velocidad = self.velocidad+1
    def bajarMarcha(self):
        self.velocidad = self.velocidad - 1
    def cambiarVelMax(self,maxVel):
        self.velMax = maxVel

mibici = Bicicleta()
print (mibici.velocidad)
mibici.subirMarcha()
mibici.subirMarcha()
print (mibici.velocidad)
mibici.bajarMarcha()
print (mibici.velocidad)
mibici.cambiarVelMax(25)
print (mibici.velMax)

print(mibici)
