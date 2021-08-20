"""
    Faça um programa que leia o salário de um funcionário
    e mostre seu novo salário com 15% de aumento
"""
salary = float(input("Qual o salário do funcionário? R$ "))
increment = salary * 0.15
print("O funcionário recebia R$ {:.2f}".format(salary))
print("Obteve um aumento de 15%: R$ {:.2f}".format(increment))
print("O novo salário é: R$ {:.2f}".format(salary + increment))
