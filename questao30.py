""" Escreva um programa que peça ao usuário para digitar seu nome completo e, 
em seguida, imprima apenas o sobrenome. """

nome = input("Digite seu nome").split()

separa = nome[1::]

print(separa)