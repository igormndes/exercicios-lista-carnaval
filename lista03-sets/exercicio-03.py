"""
How Bootcamps - Stone - /código[s]
Data: 04/03/2022
Autor: Igor Gabryell Mendes Melo
Descrição: Exercicio proposto pelo instrutor Henrique Branco.
Lista de exercícios
Tema: Dicionários e sets
Diversão do carnaval \o/

Exercício 3:
Faça um programa que ordene um dicionário por seus valores. Exemplo: dado o dicionário
>>> {“matemática”: 81, “física”: 83, “química”: 87} 
a saída deve ser 
>>> {“química”: 87, “física”: 83, matemática”: 81}

"""

# Definindo matérias e notas
notas = {"Matemática": 81, "Física": 83, "Química": 87, "Biologia" : 98, "Geografia" : 77}

# Ordenando dicionário por valor
notas_decrescente = dict(sorted(notas.items(), key = lambda nota: nota[1], reverse = True))

# Imprimindo notas na ordem solicitada
print (f"\n{notas_decrescente}")
