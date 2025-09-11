import math
num1=float(input("digite um angulo: "))
se=math.sin(math.radians(num1))
co=math.cos(math.radians(num1))
ta=math.tan(math.radians(num1))
print("Angulo: {}\nSeno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}".format(num1,se,co,ta))
