"""
    Faça um programa que leia um ângilo qualquer e mostre
    na tela o valor do seno do cosseno e da tangente.
"""
import math

angle = float(input("Digite o angulo desejado: "))
sin = math.sin(math.radians(angle))
cos = math.cos(math.radians(angle))
tang = math.tan(math.radians(angle))
print("O seno de {} é {:.2f}".format(angle, sin))
print("O cosseno de {} é {:.2f}".format(angle, cos))
print("A tangente de {} é {:.2f}".format(angle, tang))
