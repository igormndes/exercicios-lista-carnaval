"""
How Bootcamps - Stone - /código[s]
Data: 04/03/2022
Autor: Igor Gabryell Mendes Melo
Descrição: Exercicio proposto pelo instrutor Henrique Branco.
Lista de exercícios
Tema: Dicionários e sets
Diversão do carnaval \o/

Exercício 5:
Faça um programa que encontre as notas mínimas e máximas de um dicionário, e imprima-os na tela com as suas respectivas chaves. Exemplo: dado o dicionário
>>> {“Theodoro”: 20, “Márcia”: 50, “Júnior”: 80}
A saída deve ser
>>> Nota máxima -> Júnior : 80
>>> Nota mínima -> Theodoro : 20

"""
# Definindo dicionário

dic = {"Theodoro": 20, "Márcia": 50, "Júnior": 80, "Igor" : 97}

# Encontrando nota máxima
nota_maxima = max(dic.items(), key = lambda nota: nota[1])

# Encontrando nota mínima
nota_minima = min(dic.items(), key = lambda nota: nota[1])

# Imprimindo nota máxima
print (f"Nota máxima -> {nota_maxima[0]} : {nota_maxima[1]}\n")

# Imprimindo nota mínima
print (f"Nota mínima -> {nota_minima[0]} : {nota_minima[1]}\n")
