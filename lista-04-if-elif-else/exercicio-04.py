"""
How Bootcamps - Stone - /código[s]
Data: 07/03/2022
Autor: Igor Gabryell Mendes Melo
Descrição: Exercicio proposto pelo instrutor Henrique Branco.
Lista de exercícios
Tema: Condicionais
Diversão do carnaval \o/

Exercício 4:
Faça um programa que imprima na tela se um dado ano é bissexto ou não de acordo com as regras na ordem abaixo:

Um ano que é divisível por 400 é bissexto.
Dos anos que não entram na regra 1, se o ano for divisível por 100 então ele não é bissexto.
Dos anos que não entram na regra 2, se o ano for divisível por 4 então ele é um ano bissexto.
Todos os outros anos não são bissextos

"""

# Recebendo o ano do usuário
ano = int(input("Digite o ano no formato'YYYY': "))

# Definindo condições
if (ano % 400) == 0:
    print(f"\nO ano {ano} é bissexto.\n")
elif (ano % 100) == 0:
    print(f"O ano {ano} não é bissexto\n")
elif (ano % 4) == 0:
    print(f"O ano {ano} é bissexto.\n")
else:
    print(f"O ano {ano} não é bissexto.\n")
