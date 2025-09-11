import math
num1=float(input("digite o cateto adjacente: "))
num2=float(input("digite o cateto oposto: "))
hip=math.hypot(num1,num2)
print("Cateto Oposto: {}\nCateto Abjacente: {}\nHipotenusa: {:.2f}".format(num1,num2,hip))