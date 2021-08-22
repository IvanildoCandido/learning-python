"""
    Crie um programa que leia algo e mostre o seu tipo primitivo
    e todas as informações possíveis sobre ele
"""
a = input("Digite algo: ")
print("O tipo primitivo de {} é {}! ".format(a, type(a)))
print("Só tem espaços? ", a.isspace())
print("É um número? ", a.isnumeric())
print("É alfabetico? ", a.isalpha())
print("É alfanumérico? ", a.isalnum())
print("Está em maiúsculas? ", a.isupper())
print("Está em minúsculas? ", a.islower())
print("Está capitalizada? ", a.istitle())
