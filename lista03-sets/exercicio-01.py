"""
How Bootcamps - Stone - /código[s]
Data: 04/03/2022
Autor: Igor Gabryell Mendes Melo
Descrição: Exercicio proposto pelo instrutor Henrique Branco.
Lista de exercícios
Tema: Dicionários e sets
Diversão do carnaval \o/

Exercício 1:
Digamos que existam 2 cursos de idiomas em uma escola, inglês e francês, e que existam alunos matriculados conforme abaixo:
Alunos matriculados em inglês:
João Alves dos Santos
Maria Magalhães
Antônio da Silva Ferreira
José Júnior Jarbas
Henrique da Silva Sauro
Joaquina Ferreira da Silva
Fabiana Aparecida Bianco
Marrone Gutierres
Carlos Magno Farad
Antônio da Silva Júnior Amaral

Alunos matriculados em francês:
João Alves dos Santos
Antônio da Silva Ferreira
Fernanda Abdala Mohamed
Abner Mignon Alib
Alisson Figueiredo
Henrique da Silva Sauro
Maria Magalhães
Marrone Gutierres
Joaquina Ferreira da Silva

Faça um programa que responda as seguintes perguntas:

Quantos alunos estão matriculados na escola, no total?
Quantos e quais estão matriculados APENAS em INGLES?
Quantos e quais estão matriculados APENAS em FRANCES?
Quantos e quais estão matriculados EM AMBOS os cursos?
Quantos alunos estão matriculados somente em francês ou somente em inglês, mas não em ambos os cursos?
 todos os elementos para int.

"""
# Definindo alunos
alunos_ingles = {
    "João Alves dos Santos",
    "Maria Magalhães",
    "Antônio da Silva Ferreira",
    "José Júnior Jarbas",
    "Henrique da Silva Sauro",
    "Joaquina Ferreira da Silva",
    "Fabiana Aparecida Bianco",
    "Marrone Gutierres",
    "Carlos Magno Farad",
    "Antônio da Silva Júnior Amaral"}

print (f"Alunos matriculados na aula de Inglês: {alunos_ingles}\n")

alunos_frances = {
    "João Alves dos Santos",
    "Antônio da Silva Ferreira",
    "Fernanda Abdala Mohamed",
    "Abner Mignon Alib",
    "Alisson Figueiredo",
    "Henrique da Silva Sauro",
    "Maria Magalhães",
    "Marrone Gutierres",
    "Joaquina Ferreira da Silva"}

print (f"Alunos matriculados na aula de Francês: {alunos_frances}\n")

# Quantos alunos estão matriculados na escola, no total?
alunos_totais = alunos_ingles.union(alunos_frances)
print (f"A escola possui no total {len(alunos_totais)} alunos matriculados\n")

# Quantos e quais estão matriculados APENAS em INGLES?
apenas_ingles = alunos_totais - alunos_frances
print (f"Existem {len(apenas_ingles)} alunos estudando apenas Inglês, eles são: {apenas_ingles}\n")

# Quantos e quais estão matriculados APENAS em FRANCES?
apenas_frances = alunos_totais - alunos_ingles
print (f"Exsitem {len(apenas_frances)} alunos estudando apenas Francês,eles são: {apenas_frances}\n")

# Quantos e quais estão matriculados EM AMBOS os cursos?
ambos = alunos_ingles.intersection(alunos_frances)
print (f"Existem {len(ambos)} alunos estudando ambos os cursos, eles são: {ambos}\n")

# Quantos alunos estão matriculados somente em francês ou somente em inglês, mas não em ambos os cursos?
um_ou_outro = apenas_ingles.union(apenas_frances)
print (f"Existem {len(um_ou_outro)} alunos estudando somente Inglês ou somente Francês\n")
