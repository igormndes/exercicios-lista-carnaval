from cmath import log
from math import log10
"""
How Bootcamps - Stone - /código[s]
Data: 02/03/2022
Autor: Igor Gabryell Mendes Melo
Descrição: Exercicio proposto pelo instrutor Henrique Branco.
Lista de exercícios
Tema: Tipos numéricos
Diversão do carnaval \o/

Exercício 1: 
Faça um programa que receba dois números inteiros do usuário, A e B e imprima na tela as seguintes operações: 
A soma de A e B; 
A diferença quando se subtrai B de A; 
O produto (multiplicação) entre A e B; 
O quociente (parte inteira da divisão) quando se divide A por B; 
O resto da divisão entre A e B; 
O resultado de log10 de A; 
O resultado de A elevado a B; 

"""
# Solicitando entrada de dados - números inteiros

A = int(input("Digite o primeiro número inteiro: "))

B = int(input("Digite o segundo número interiro: "))


# A soma de A e B

soma = A + B
print (f"\nA soma de A e B é : {soma}\n")


# A diferença quando se subtrai B de A

diferenca = B - A
print (f"A diferença quando se subtrai B de A é: {diferenca}\n")


# O produto (multiplicação) entre A e B

multiplicacao = A * B
print (f"O produto entre A e B é: {multiplicacao}\n")


# O quociente (parte inteira da divisão) quando se divide A por B

quociente = (A / B)
quociente_int = round(quociente, 0)
print (f"O quociente quando se divide A por B é: {quociente_int}\n")


# O resto da divisão entre A e B
resto = A // B
print (f"O resto da divisão entre A e B é: {resto}\n")


# O resultado de log10 de A
log10 = log10(A)
print (f"O resultado de log10 de A é: {log10}\n")


# O resultado de A elevado a B
exponecial = A ** B
print (f"O resultado de A elevado a B é: {exponecial}\n")
