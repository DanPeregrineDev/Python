"""
    Faça um programa que leia o nome e a média de um aluno,
    guardando também a sua situação (APROVADO/REPROVADO) num dicionário.
    No final, mostre o conteúdo da estrutura no ecrã
"""

dicionario = {}

nome = input("Escreva o nome do aluno: ").capitalize()

media = float(input("Escreva a média do aluno: "))

dicionario['nome'] = nome
dicionario['media'] = media

if media >= 10:
    dicionario['situacao'] = "Aprovado"
elif media < 10:
    dicionario['situacao'] = "Reprovado"

print(dicionario)