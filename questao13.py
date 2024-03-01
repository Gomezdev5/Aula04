""" Escreva um programa que solicite ao usuário um número decimal e imprima uma mensagem formatada mostrando o número com duas casas decimais. """

num = float(input("digite o numero?"))

formato = "{:.2f}".format(num)
print(formato)