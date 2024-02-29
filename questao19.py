""" Escreva um programa que solicite ao usuário para digitar uma frase e verifique se ela contém a palavra "Python". """

frase = input("escreva uma frase").upper()



tem = frase.find("PYTHON")



print(f"Tem a palavra Python ? {tem != -1}")