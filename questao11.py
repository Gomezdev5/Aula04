""" Escreva um programa que solicite ao usuário uma quantidade de horas, minutos e segundos, e imprima uma mensagem formatada mostrando o total de segundos.
Por exemplo: "O total de segundos é {total_segundos}." """

hora = int(input("São quantas horas?"))
minuto = int(input("São quantos minutos?"))
segundo = int(input("São quantos segundos?"))

horas = hora * 60 * 60
minutos = minuto * 60

segundos = segundo * 60

total_segundos = horas + minutos + segundos

print("O total de segundos é ", total_segundos)