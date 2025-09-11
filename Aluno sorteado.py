import random
al1=str(input("nome do aluno: "))
al2=str(input("outro aluno: "))
al3=str(input("outro aluno: "))
al4=str(input("outro aluno: "))
als=[al1,al2,al3,al4]
sor=random.choice(als)
print("o aluno sorteado foi: {}".format(sor))
