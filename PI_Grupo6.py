mp10 = -1
while mp10 < 0: 
	mp10 = float(input("Digite a quantidade de particulas inalaveis: "))
mp25 = -1
while mp25 < 0: 
	mp25 = float(input("Digite a quantidade de particulas inalaveis finas: "))
o3 = -1
while o3 < 0: 
	o3 = float(input("Digite o nivel de ozonio: "))
co = -1
while co < 0: 
	co = float(input("Digite o nivel de monoxido de carbono: "))
no2 = -1
while no2 < 0: 
	no2 = float(input("Digite o nivel de dioxido de nitrogenio: "))
so2 = -1
while so2 < 0: 
	so2 = float(input("Digite o nivel de dioxido de enxofre: "))
	
qldAr = "" 

if mp10 > 250 or mp25 > 125 or o3 > 200 or co > 15 or no2 > 1130 or so2 > 800: 
	qldAr = "Pessima" 
elif mp10 > 150 and mp10 < 250 or mp25 > 75 and mp25 < 125 or o3 > 160 and o3 < 200 or co > 13 and co < 15  or no2 > 320 and no2 < 1130 or so2 > 365 and so2 < 800: 
	qldAr = "Muito Ruim"
elif mp10 > 100 and mp10 < 150 or mp25 > 50 and mp25 < 75 or o3 > 130 and o3 < 160 or co > 11 and co < 13  or no2 > 240 and no2 < 320 or so2 > 40 and so2 < 365: 
	qldAr = "Ruim"
elif mp10 > 50 and mp10 < 100 or mp25 > 25 and mp25 < 50 or o3 > 100 and o3 < 130 or co > 9 and co < 11 or no2 > 200 and no2 < 240 or so2 > 20 and so2 < 40:  
	qldAr =	"Moderado"
else: 
	qldAr = "Bom"

if qldAr == "Bom": 
	print("Qualidade do ar:", qldAr, "\nImplicacoes a saude: Nenhuma")
elif qldAr == "Moderada": 
	print("Qualidade do ar:", qldAr, "\nImplicacoes a saude: Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar sintomas como tosse seca e cansaço. A população, em geral, não é afetada.")
elif qldAr == "Ruim": 
	print("Qualidade do ar:", qldAr, "\nImplicacoes a saude: Toda a população pode apresentar sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta. Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar efeitos mais sérios na saúde.")
elif qldAr == "Muito Ruim":
 	print("Qualidade do ar:", qldAr, "\nImplicacoes a saude: Toda a população pode apresentar sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta e ainda falta de ar e respiração ofegante. Efeitos mais graves à saúde de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas).")
else: 
	print("Qualidade do ar:", qldAr, "\nImplicacoes a saude: Toda a população pode apresentar sérios riscos de manifestações de doenças respiratórias e cardiovasculares. Aumento de mortes prematuras em pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas).")
