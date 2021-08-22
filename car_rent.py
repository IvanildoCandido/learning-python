"""
    Escreva um programa que pergunte a quantidade de Km percorridos
    por um carro alugado e a quantidade de dias pelos quais ele foi
    alugado. Calcule o preço a pagar, sabendo que o carro custa
    R$ 60,00 por dia e R$ 0,15 por km rodado.
"""
days = int(input("Quantos dias o carro passou alugado? "))
kms = float(input("Qauantos Kms o carro percorreu? "))
total = (days * 60) + (kms * 0.15)
print("O carro passou {} dias alugado!".format(days))
print("O carro rodou {}KMs!".format(kms))
print("O valor total do aluguel é R$ {:.2f} !".format(total))
