"""
How Bootcamps - Stone - /código[s]
Data: 04/03/2022
Autor: Igor Gabryell Mendes Melo
Descrição: Exercicio proposto pelo instrutor Henrique Branco.
Lista de exercícios
Tema: Listas
Diversão do carnaval \o/

Exercício 3: 
Crie uma lista com 6 números inteiros. Imprima o maior, o menor e suas respectivas posições. Exemplo: para a lista [5,4,6,8,3,4] a saída deve ser
>>> O maior elemento é 8 e está na posição 3
>>> O menor elemento é 3 e está na posição 4

Obs: caso o maior ou o menor número sejam repetidos, trazer a menor posição.


"""

# Definindo lista 
lista = [5, 4, 6, 8, 3, 4 ]

# Encontrando maior elemento:
maior_elemento = max(lista)

# Encontrando posição do maior elemento:
pos_maior = lista.index(maior_elemento)

# Encontrando menor elemento:
menor_elemento = min(lista)

# Encontrando posição do menor elemento:
pos_menor = lista.index(menor_elemento)

# Imprimindo elemento e posição
print (f"O maior elemento é {maior_elemento} e está na posição: {pos_maior}"
       f"\nO menor elemento é {menor_elemento} e está na posição: {pos_menor}")

