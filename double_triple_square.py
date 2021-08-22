"""
    Escreva um programa que leia um número e mostre
    o dobro o triplo e a raiz quadrada
"""
num = int(input("Digite um número: "))
double = num * 2
triple = num * 3
square = num ** (1 / 2)
print("Número digitado: {}".format(num))
print("O dobro é : {}".format(double))
print("O triplo é : {}".format(triple))
print("A raiz quadrada é : {:.2f}".format(square))
