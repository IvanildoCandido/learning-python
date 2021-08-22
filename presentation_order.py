"""
    Faça um programa que leia o nome de quatro alunos
    e mostre a ordem sorteada.
"""
import random

n1 = str(input("Primeiro aluno: "))
n2 = str(input("Segundo aluno: "))
n3 = str(input("Terceiro aluno: "))
n4 = str(input("Quarto aluno: "))
students_list = [n1, n2, n3, n4]
random.shuffle(students_list)
print("A ordem de apresentação será:")
print(students_list)
