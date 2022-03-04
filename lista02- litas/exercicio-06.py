"""
How Bootcamps - Stone - /código[s]
Data: 04/03/2022
Autor: Igor Gabryell Mendes Melo
Descrição: Exercicio proposto pelo instrutor Henrique Branco.
Lista de exercícios
Tema: Listas
Diversão do carnaval \o/

Exercício 6: 
Faça um programa que remova strings vazias de uma lista de strings. Exemplo: dada a lista [“Olá”, “”, “meu”, “nome”, “”, “é”, “facilitador”, “”] a saída deve ser
>>> [“Olá”, “meu”, “nome”, “é”, “facilitador”]

"""
# Definindo a lista
lst = ["Olá",",","meu","","nome","","é","","Igor","."]

# Definindo o loop pra varrer todos os elementos da lista
for i in lst:
    # Definindo a condição
    if i == '':
        # Excluindo os elementos que atendem a condição
        lst.pop(lst.index(i))
        
# Imprimindo o resultado
print(f'\n{lst}\n')

# Imprimido a lista como frase
print(' '.join(lst))
