"""
    Um professor quer sortear um de seus alunos para
    apagar o quadro. Faça um programa que ajude ele
    lendo o node deles e escrevendo o nome escolhido.
"""
import random

n1 = str(input("Primeiro aluno: "))
n2 = str(input("Segundo aluno: "))
n3 = str(input("Terceiro aluno: "))
n4 = str(input("Quarto aluno: "))
students_list = [n1, n2, n3, n4]
selected = random.choice(students_list)
print("O aluno escolhido foi: {}".format(selected))
