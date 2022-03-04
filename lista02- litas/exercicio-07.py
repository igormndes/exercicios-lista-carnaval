"""
How Bootcamps - Stone - /código[s]
Data: 04/03/2022
Autor: Igor Gabryell Mendes Melo
Descrição: Exercicio proposto pelo instrutor Henrique Branco.
Lista de exercícios
Tema: Listas
Diversão do carnaval \o/

Exercício 7: 
Dada a lista de strings [“1”, “7”, “99”, “15”] construa um programa que converte todos os elementos desta lista para inteiro.

Faça também o inverso, dada a mesma lista só que agora de elementos inteiros, converta todos os elementos para int.

"""

# Definindo a lista
lista = ["1", "7", "99", "15"]
print (f"\nLista original: {lista}\n")

# Convertendo os elementos para int
for i,j in enumerate(lista):
    lista[i] = int(j)

print (f"\nLista como inteiro: {lista}\n")

# Convertendo de volta para string
for i,j in enumerate(lista):
    lista[i] = str(j)

print (f"\nLista como string: {lista}\n")
