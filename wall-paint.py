"""
    Escreva um programa que leia a largura e a altura de uma parede
    em metros e calcule a sua área e a quantidade de tinta necessária para
    pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m!
"""
width = float(input("Digite a largura da parede (m): "))
heigth = float(input("Digite a altura da parede (m): "))
area = width * heigth
qtd_print = area / 2
print(40 * "=", "\n")
print("Sua parede tem uma dimensão de {:.2f} x {:.2f}".format(width, heigth))
print("A área da sua parede corresponde a {:.2f}m2".format(area))
print(
    "Para pintar essa parede, você precisará de {}l de tinta\n".format(
        qtd_print
    )
)
print(40 * "=", "\n")
