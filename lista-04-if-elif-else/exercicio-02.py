"""
How Bootcamps - Stone - /código[s]
Data: 07/03/2022
Autor: Igor Gabryell Mendes Melo
Descrição: Exercicio proposto pelo instrutor Henrique Branco.
Lista de exercícios
Tema: Condicionais
Diversão do carnaval \o/

Exercício 2:
Escreva um programa que receba dois números e imprima na tela se o primeiro é divisível pelo segundo.

"""

# Recebendo números
num_1 = int(input("Digite o primeiro número: "))

num_2 = int(input("Digite o segunda número: "))

# Condição para o primeiro ser divisível pelo segundo
condicao = num_1 % num_2

# Imprimindo na tela
if condicao == 0:
    print(f"O número {num_1} é divisível pelo número {num_2}!")
else:
    print(f"O número {num_1} não é divisível pelo número {num_2}!")
