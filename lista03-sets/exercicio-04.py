"""
How Bootcamps - Stone - /código[s]
Data: 04/03/2022
Autor: Igor Gabryell Mendes Melo
Descrição: Exercicio proposto pelo instrutor Henrique Branco.
Lista de exercícios
Tema: Dicionários e sets
Diversão do carnaval \o/

Exercício 4:
Escreva um programa para encontrar o tamanho do comprimento das strings nos valores de dicionário. Exemplo: dada o dicionário
>>> {1: “vermelho”, 2: “azul”, 3: “marrom”}
A saída deverá ser
>>> {1: 8, 2: 4, 3: 6}

"""
# Definindo dicionario
dicionario = {1: "Vermelho", 2: "Azul", 3: "Marrom", 4: "Violeta", 5: "Rosa", 6: "Verde"}

# Definindo dicionario vazio
dicionario_vazio = {}

# Varrendo todo o dicionario
for i,j in dicionario.items():
    # Adicionando no dicionario_vazio o comprimento de cada valor (len(j)) para cada item no dicionario(i)
    dicionario_vazio[i] = len(j)

# Imprimindo dicionario conforme solicitado
print (dicionario_vazio)
