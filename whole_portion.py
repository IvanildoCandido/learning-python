"""
    Crie um programa que leia um número real qualquer
    e mostre na tela a sua porção inteira.
"""
from math import floor

number = float(input("Digite um número real qualquer! "))
print("A parte inteira do número {} é {}.".format(number, floor(number)))
