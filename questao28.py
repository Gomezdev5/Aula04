"""Escreva um programa que solicite ao usuário para digitar uma frase e, em seguida, 
divida a frase em palavras individuais e as imprima em linhas separadas."""

frase = input("Digite uma frase: ")

print("Palavras na frase:", *frase.split(), sep='\n')