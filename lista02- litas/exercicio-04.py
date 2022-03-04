"""
How Bootcamps - Stone - /código[s]
Data: 04/03/2022
Autor: Igor Gabryell Mendes Melo
Descrição: Exercicio proposto pelo instrutor Henrique Branco.
Lista de exercícios
Tema: Listas
Diversão do carnaval \o/

Exercício 4: 
Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista.
Em seguida, calcule a média anual das temperaturas e mostre a média calculada juntamente com todas as temperaturas acima da média anual,
e em que mês elas ocorreram (mostrar o mês por extenso: Exemplo de saída:
>>> Meses com temperatura acima da média anual de 35,5°:
>>> 1 – janeiro
>>> 3 – março
>>> 6 – junho


"""
# Criando lista vazia 
temperaturas_2022 = []

# Meses do ano
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

# Recebendo temperatura média de cada mês do ano
for i in meses:
    temperaturas_2022.append(float(input(f"Digite a temperatura do mês de {i}: ")))

# Calculando a temperatura média anual
temperatura_media = sum(temperaturas_2022) / len(meses)
print (f"\nA temperatura média anual foi de: {temperatura_media:.1f}ºC\n")

# Meses acima da média anual
print("Meses com temperatura acima da média: ")
for temperatura in temperaturas_2022:
    if temperatura > temperatura_media:
        print(f"{meses[temperaturas_2022.index(temperatura)]} - {temperatura}ºC\n")
