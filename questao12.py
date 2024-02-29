""" Escreva um programa que solicite ao usuário uma frase e imprima uma mensagem formatada mostrando a quantidade de caracteres, palavras e linhas na frase. """

frase = """ Escreva um programa que solicite ao usuário uma frase e 
imprima uma mensagem formatada mostrando a quantidade de caracteres,
palavras e linhas na frase. """


paragrafos = frase.count("\n")
linhas = len(frase)
palavras = frase.count(" ") + 1

print(paragrafos, linhas, palavras)