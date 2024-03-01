""" Escreva um programa que solicite ao usuário para digitar uma palavra e verifique se ela é um palíndromo. """

frase = input("escreva um Palindromo")

inverter = frase[::-1]

palindromo = frase == inverter

print(frase, inverter,"Essa frase é um Palindromo? ", palindromo)