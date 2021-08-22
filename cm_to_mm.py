"""
    Escreva um programa que leia um valor em metros
    e exiba convertido em centimetros e milimetros
"""
measure = float(input("Digite uma distancia em metros: "))
km = measure / 1000
hm = measure / 100
dam = measure / 10
dm = measure * 10
cm = measure * 100
mm = measure * 1000
print("A medida {} equivale a: {:.2f}km".format(measure, km))
print("A medida {} equivale a: {:.2f}hm".format(measure, hm))
print("A medida {} equivale a: {:.2f}dam".format(measure, dam))
print("A medida {} equivale a: {:.0f}dm".format(measure, dm))
print("A medida {} equivale a: {:.0f}cm".format(measure, cm))
print("A medida {} equivale a: {:.0f}mm".format(measure, mm))
