"""Faça um programa que receba a temperatura média
de cada mês do ano e armazene-as em uma lista.
Em seguida, calcule a média anual das temperaturas
e mostre a média calculada juntamente com todas as
temperaturas acima da média anual, e em que mês
elas ocorreram (mostrar o mês por extenso: 1 –
Janeiro, 2 – Fevereiro, . . . )."""

temp_media_mes_ano = []
temp_maiores = []
meses = { 
     1: "Janeiro", 
     2: "Fevereiro",
     3: "Marco", 
     4: "Abril", 
     5: "Maio", 
     6: "Junho", 
     7: "Julho", 
     8: "Agosto", 
     9: "Setembro", 
     10: "Outubro", 
     11: "Novembro", 
     12: "Dezembro",  
} 

for cont in range(0,12):
    temp_media_mes_ano.append(float(input('Digite a temperatura média de '+meses[cont + 1]+":")))

media_anual_temp = sum(temp_media_mes_ano) / len(temp_media_mes_ano)

print("\n")
print("A média dos meses é: " + str(media_anual_temp))
print("\n")

print("Meses com médias superiores a " + str(media_anual_temp) + ":")
print("\n")

for cont, temperatura in enumerate(temp_media_mes_ano):
    if temperatura > media_anual_temp:
        print(f"{temperatura} - {meses[cont + 1]}")

