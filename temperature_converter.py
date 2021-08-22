"""
    Escreva um programa que leia uma temperatura em graus Celcius
    e converta a mesma para graus fahrenheit
"""

celcius = float(input("Digite a temperatura em graus Celcius: "))
fahrenheit = ((9 * celcius) / 5) + 32
print("A temperatura de {} °C corresponde a {} °F".format(celcius, fahrenheit))
