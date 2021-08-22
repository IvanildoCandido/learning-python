"""
    Faça um programa que leia o comprimento do cateto oposto
    e do cateto adjacente de um triangulo retângulo e calcule
    e mostre o comprimento da hipotenusa.
"""
from math import pow, sqrt

opposite_leg = float(input("Digite o comprimento do cateto oposto: "))
adjacent_leg = float(input("Digite o comprimento do cateto adjacente: "))
hypotenuse = pow(opposite_leg, 2) + pow(adjacent_leg, 2)

# hypotenuse = math.hypot(opposite_leg, adjacent_leg)

print(
    "O comprimento da hipotenusa do triangulo é {:.2f}".format(
        sqrt(hypotenuse)
    )
)
