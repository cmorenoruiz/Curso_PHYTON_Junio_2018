class Bicicleta:
    color = ""
    tamanio = ""
    velMax=15
    def __init__(self):
        self.velocidad = 0
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