""" Escreva um programa que solicite ao usuário para digitar uma frase e substitua todas as ocorrências da letra "a" por "@". """

import re 


nome = input("Escreva um nome")

substituicao = re.sub("[a]", "@", nome)

print(substituicao)