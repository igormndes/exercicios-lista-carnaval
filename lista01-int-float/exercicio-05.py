"""
How Bootcamps - Stone - /código[s]
Data: 02/03/2022
Autor: Igor Gabryell Mendes Melo
Descrição: Exercicio proposto pelo instrutor Henrique Branco.
Lista de exercícios
Tema: Tipos numéricos
Diversão do carnaval \o/

Exercício 5: 
Escreva um programa que leia do usuário um número de 4 dígitos e imprima a soma destes dígitos. Exemplo, se o usuário digitar 3141 seu programa deverá imprimir na tela .

"""
# Recebendo do usuário um número de 4 dígitos

num = input("Digite um número de 04 dígitos: ")

# Criando uma lista vazia que recebera os numeros digitados

numeros = []

# separando e convertendo os numeros recebidos de str para int

separando = [numeros.append(int(num[i])) for i in range(len(num))]

# somando os valores

soma = sum(numeros[0:3])

# imprimindo o resultado
print(f'\n{numeros[0]} + {numeros[1]} + {numeros[2]} + {numeros[3]} = {soma}')
