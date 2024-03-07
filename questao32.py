"""Escreva um programa para ler uma frase, imprima esta frase com as palavras ordenadas em ordem 
crescente de comprimento das strings."""

def ordenar_palavras_por_comprimento(frase):
    palavras = frase.split()
    
    palavras_ordenadas = sorted(palavras, key=len)
    
    return palavras_ordenadas


frase = input("Digite uma frase: ")


palavras_ordenadas = ordenar_palavras_por_comprimento(frase)

print("Palavras ordenadas por comprimento:")
for palavra in palavras_ordenadas:
    print(palavra)