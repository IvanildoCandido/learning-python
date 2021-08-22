"""
    Escreva um programa que leia o valor de dinheiro
    que uma pessoa tem na carteira e mostre quantos
    dolares essa pessoa pode comprar
"""
brl = float(input("Quanto dinheiro você tem na carteira? R$ "))
usd = 5.39
print("Com R$ {:.2f} você pode comprar US$ {:.2f}".format(brl, brl / usd))
