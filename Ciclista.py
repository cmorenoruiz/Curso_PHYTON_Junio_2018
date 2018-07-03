from ClaseBicicleta import Bicicleta

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