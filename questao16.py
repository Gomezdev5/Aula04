""" Escreva um programa que peça ao usuário para digitar seu nome completo e imprima apenas o primeiro nome. """

nome = input("Nome completo ? ").split()

primeira_palavra = nome[0]

print(primeira_palavra)