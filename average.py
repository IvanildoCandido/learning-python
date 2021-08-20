"""
    Escreva um programa que leia duas notas de um aluno
    e mostre a média aritmética
"""
note1 = float(input("Primeira nota do aluno: "))
note2 = float(input("Segunda nota do aluno: "))
print(
    "A média entre {:.1f} e {:.1f} é : {:.1f}".format(
        note1, note2, (note1 + note2) / 2
    )
)
