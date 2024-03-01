""" Escreva um programa que solicite ao usuário para digitar seu endereço de e-mail e extraia o nome de usuário (parte antes do "@") e o domínio (parte depois do "@"). """

email = input("Escreva seu Email")

res = email.split("@")

ususario = res[0]

dominio_completo = res[1]
dominio_nome = dominio_completo.split(".") [0]

print("Usuario: ", ususario, "Dominio: ", dominio_nome)


