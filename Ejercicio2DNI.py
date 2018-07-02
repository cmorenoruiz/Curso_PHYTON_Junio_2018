#Introduce el DNI y te damos la letra
dni=int(input("dame tu DNI"))
num_letra=dni%23
print("Numero de letra", num_letra)
tabla={0:'T',1:'R',2:'W',3: 'A', 4: 'G', 5: 'M', 6: 'Y',
     7: 'F', 8: 'P', 9: 'D', 10: 'X', 11: 'B', 12: 'N',
       13: 'J', 14:'Z',15:'S',16:'Q',17:'V',18:'H',19:'L',
       20:'C', 21:'K', 22:'E', 23:'T'}
print("Letra del DNI",tabla[num_letra])