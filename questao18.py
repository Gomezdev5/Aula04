""" Escreva um programa que solicite ao usuário para digitar uma frase e verifique se ela termina com um ponto final. """

frase = input("escreva uma frase")

ponto_final = frase[-1]

tem_paranteses = ponto_final == "."

print(tem_paranteses)
