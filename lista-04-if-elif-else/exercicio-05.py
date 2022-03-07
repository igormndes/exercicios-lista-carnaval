# Importando Regular Expression RegEx
import re
"""
How Bootcamps - Stone - /código[s]
Data: 07/03/2022
Autor: Igor Gabryell Mendes Melo
Descrição: Exercicio proposto pelo instrutor Henrique Branco.
Lista de exercícios
Tema: Condicionais
Diversão do carnaval \o/

Exercício 5:
Escreva um programa que receba uma string e diga se ela tem o formato de uma placa veicular brasileira (no formato antigo) com três letras, um traço e quatro números. Exemplos: 
Dada a entrada ABT-1234 o programa deveria exibir True
Dada a entrada JKL9999 o programa deveria exibir False
Qualquer outra entrada que fuja do padrão de 3 letras, um traço e quatro números, o programa deverá exibir False 

"""

# Recebendo placa do usuário 
placa = str(input("Digite a placa: ")).upper()

# Definindo o formato padrão de um placa veicular brasileira
padrao = re.compile("[\w]{3}[-][\d]{4}")

# Verificando se a placa informada está no padrão
placa_valida = padrao.search(placa)

# Imprimindo
if placa_valida:
    print(f"\nA placa {placa} é válida!\n")
else:
    print(f"\nA placa informada não é válida!\n")
    
