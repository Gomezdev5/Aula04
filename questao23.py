""" Escreva um programa que solicite ao usuário para digitar uma frase e verifique se todas as palavras estão em letras maiúsculas. """

frase = input("Escreva uma frase")

minusculas = frase.lower() == frase

print("só tem minusculas ?", minusculas)