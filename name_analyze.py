"""
    Crie um programa que leia o nome completo de uma pessoa
    e mostre:
    - O nome completo com todas as letras maiúscula e minúsculas
    - Quantas letras ao todo sem considerar espaços
    - Quantas letras tem o primeiro nome
"""
name = str(input("Digite o seu nome completo: ")).strip()
print("Seu nome em maiúsculas é {}".format(name.upper()))
print("Seu nome em minúsculas é {}".format(name.lower()))
print("Seu nome tem ao todo {} letras.".format(len(name) - name.count(" ")))
print(
    "Seu primeiro nome é {} e ele tem {} letras.".format(
        name[: name.find(" ")], name.find(" ")
    )
)
