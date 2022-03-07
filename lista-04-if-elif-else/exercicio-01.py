"""
How Bootcamps - Stone - /código[s]
Data: 07/03/2022
Autor: Igor Gabryell Mendes Melo
Descrição: Exercicio proposto pelo instrutor Henrique Branco.
Lista de exercícios
Tema: Condicionais
Diversão do carnaval \o/

Exercício 1:
Escreva um programa que diga se um número dado pelo usuário é par ou ímpar

"""
# Pegando número
numero = int(input("Digite um número inteiro: "))

# condicao para ser par ou ímpar 
condicao = numero % 2

# Imprimindo na tela se número é par ou impar
if condicao == 0:
    print(f"O número '{numero}' é par!")
else:
    print (f"O número '{numero}' é impar!")
