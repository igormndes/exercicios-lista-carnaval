"""
How Bootcamps - Stone - /código[s]
Data: 04/03/2022
Autor: Igor Gabryell Mendes Melo
Descrição: Exercicio proposto pelo instrutor Henrique Branco.
Lista de exercícios
Tema: Listas
Diversão do carnaval \o/

Exercício 1:
Crie uma variável do tipo lista com 5 elementos (você escolhe quais serão). 
Imprima na tela o elemento e sua respectiva posição na lista. 
Exemplo: para a lista [1, 3, 6, “H”, [7,7,7]] a saída deve ser:
>>> Elemento 1 na posição 0
>>> Elemento 3 na posição 1
>>> Elemento 6 na posição 2
>>> Elemento “H” na posição 3

"""

# Definindo Lista
lista = ["Igor", 25, "M", 1996, [8,8,8]]

# iterando a lista e imprimindo o resultado
for i,j in enumerate(lista):
    print(f"Elemento {j} na posição {i}")
