"""
    Crie um programa que leia o nome de uma pessoa
    e mostre uma mensagem de boas vindas
"""
name = input("Digite seu nome: ")
print("É um prazer te conhecer, {:=^30}!".format(name))
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
div = num1 / num2
print("A divisão de {} com {} é: {:.2f}".format(num1, num2, div), end=" >>> ")
print('O end no final do "print" evita a quebra de linha')
