import random
li1=str(input("digite o lider do grupo 1: "))
li2=str(input("digite o lider do grupo 2: "))
li3=str(input("digite o lider do grupo 3: "))
li4=str(input("digite o lider do grupo 4: "))
lideres=[li1,li2,li3,li4]
random.shuffle(lideres)
print(lideres)