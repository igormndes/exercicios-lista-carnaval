from math import pow
"""
How Bootcamps - Stone - /código[s]
Data: 02/03/2022
Autor: Igor Gabryell Mendes Melo
Descrição: Exercicio proposto pelo instrutor Henrique Branco.
Lista de exercícios
Tema: Tipos numéricos
Diversão do carnaval \o/

Exercício 3: 
No exercício 02 você calculou a área de um triângulo a partir da sua base e altura. Faça um programa que receba os 3 lados de um triângulo – s1, s2 e s3 – e calcule sua área. Compare a resposta com o exercício acima, dada das mesmas entradas. Os resultados devem ser idênticos.

"""
# Recebendo comprimento dos lados do triângulo: 

s1 = float(input("Digite o comprimento do primeiro lado do triângulo: "))

s2 = float(input("Digite o comprimento do segundo lado do triângulo: "))

s3 = float(input("Digite o compirmento do terceiro lado do triângulo: "))


# Calculando área do triãngulo
s = (s1 + s2 + s3) / 2 
print (f"\nSoma dos lados divido por 2: {s}\n")

ss1 = s - s1
print (f"Soma dos lados menos lado s1: {ss1}\n")

ss2 = s - s2
print (f"Soma dos lados menos lado s2: {ss2}\n")

ss3 = s - s3
print (f"Soma dos lados menos lado s3: {ss3}\n")

area_ao_quadrado = s * ss1 * ss2 * ss3
print (f"Área do triângulo sem tirar raiz quadrada: {area_ao_quadrado}\n")

area = pow(area_ao_quadrado, 0.5)
print (f"Área do triângulo: {area}\n")
