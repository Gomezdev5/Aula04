""" Escreva um programa que substitua todas as ocorrências de uma determinada palavra em 
uma frase por outra palavra fornecida pelo usuário. """

palavra = input("Digite uma palavra")

frase = "Hoje é domingo e há possibilidade de chover"

nova_frase = frase.replace("domingo", palavra)

print(nova_frase)