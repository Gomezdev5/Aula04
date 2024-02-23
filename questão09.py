import re 
"""Escreva um programa que solicite ao usuário uma frase e substitua todas as vogais por asteriscos (*). Em seguida, imprima a frase formatada."""

nome = input()

substituicao = re.sub("[aeiou]", "*", nome)

print(substituicao)