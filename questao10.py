"""Escreva um programa que solicite ao usuário seu nome completo e imprima as iniciais de cada palavra em letras maiúsculas. 
Por exemplo, se o nome for "Fulano de Tal", o programa deve imprimir "F.D.T." """

nome_completo = input("Digite o seu nome completo?")#anderson Gomes Cunha

#Separa o texto nos espaços: [Anderson, Gomes]
partes_nome = nome_completo.split()

primeiro_nome =  partes_nome[0]
segundo_nome =  partes_nome[1]
terceiro_nome =  partes_nome[2]

incial1 = primeiro_nome[0]
inicial2 = segundo_nome[0]
inicial3 = terceiro_nome[0]

iniciais = incial1 + inicial2 + inicial3

print(iniciais)