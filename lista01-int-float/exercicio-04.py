"""
How Bootcamps - Stone - /código[s]
Data: 02/03/2022
Autor: Igor Gabryell Mendes Melo
Descrição: Exercicio proposto pelo instrutor Henrique Branco.
Lista de exercícios
Tema: Tipos numéricos
Diversão do carnaval \o/


Exercício 4: 
Faça um programa que receba do usuário seu peso em kg e altura em metros e imprima o Índice de Massa Corporal (IMC) do usuário.

"""
# Recebendo peso e altura
peso = float(input("Digite o seu peso: "))

altura = float(input("Digite a sua altura: "))


# Calculando o Índice de Massa Corporal (IMC)
IMC = peso / (altura ** 2)
print (f"O IMC do usuário é: {IMC}\n")
