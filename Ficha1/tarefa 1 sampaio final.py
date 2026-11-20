from time import sleep
from math import pi
num1 = float(input("Escolhe um numero: "))
num2 = float(input("Escolhe outro numero: "))
soma = num1 + num2
produto = num1 * num2
print(f"A soma é {soma} e o produto é {produto}")
sleep(2)

raio = float(input("Qual o raio: ")) 
area = pi * raio**2
perimetro = 2 * pi * raio
print(f"A área da circunferência é {area} e o perímetro é {perimetro}")
sleep(2)

compra=input("Qual o produto: ")
iva=("Qual o iva: ")
preço_sem_iva=int(input("Qual o preço sem iva: "))
preço_iva=preço_sem_iva+(preço_sem_iva*(iva/100))
print(f"{compra} custa {preço_iva} euros")
sleep(2)

base=int(input("Quanto mede a base do triangulo: "))
altura=int(input("Quanto mede a altura do triangulo: "))
area_triangulo=(base*altura)/2
print(f"A area do triangulo é {area_triangulo}")