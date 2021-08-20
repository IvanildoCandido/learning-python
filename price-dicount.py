"""
    Faça um programa que leia o preço de um produto
    e mostre o novo preço com 5% de desconto
"""
price = float(input("Qual o preço do produto? R$ "))
discount = price * 0.05
print("O produto custava R$ {:.2f}".format(price))
print("Desconto de 5%: R$ {:.2f}".format(discount))
print("O novo preço é: R$ {:.2f}".format(price - discount))
