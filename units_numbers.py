"""
    Faça um programa que leia um número de 0 a 9999 e
    mostre na teça cada um dos digitos separados:
    Ex: 1834
    unidades: 4 dezenas: 3 centenas: 8 milhar: 1
"""
number = int(input("Informe um número: "))
unit = number // 1 % 10
ten = number // 10 % 10
hundred = number // 100 % 10
thousand = number // 1000 % 10
print("Analizando o número {}".format(number))
print("Unidades: {}".format(unit))
print("Dezenas: {}".format(ten))
print("Centenas: {}".format(hundred))
print("Milhares: {}".format(thousand))
