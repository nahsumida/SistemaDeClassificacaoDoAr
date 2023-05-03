# Entrada de dados - Solicitação dos valores das amostras
mp10 = -1
while mp10 < 0: 
	mp10 = float(input("Digite a quantidade de particulas inaláveis: "))
mp25 = -1
while mp25 < 0: 
	mp25 = float(input("Digite a quantidade de particulas inaláveis finas: "))
o3 = -1
while o3 < 0: 
	o3 = float(input("Digite o nível de ozônio: "))
co = -1
while co < 0: 
	co = float(input("Digite o nível de monóxido de carbono: "))
no2 = -1
while no2 < 0: 
	no2 = float(input("Digite o nível de dióxido de nitrogênio: "))
so2 = -1
while so2 < 0: 
	so2 = float(input("Digite o nível de dióxido de enxofre: "))

# Análise da qualidade das amostras
qldAr = "" 
if 50 >= mp10 and 25 >= mp25 and 100 >= o3 and 9 >= co and 200 >= no2 and 20 >= so2:
	qldAr = "Bom"
elif mp10 > 50 and mp10 <= 100 or mp25 > 25 and mp25 <= 50 or 100 < o3 and o3 < 130 or 9 < co and co < 11 or 200 < no2 and no2 < 240 or 20 < so2 and so2 < 40:
	qldAr = "Moderado"
elif 100 < mp10 and mp10 <= 150 or 50 < mp25 and mp25 <= 75 or 130 < o3 and o3 <= 160 or 11 < co and co <= 13 or 240 < no2 and no2 <= 320 or 40 < so2 and so2 <= 365:
	qldAr = "Ruim"
elif 150 < mp10 and mp10 <= 250 or 75 < mp25 and mp25 < 125 or 160 < o3 and o3 < 200 or 13 < co and co < 15  or 320 < no2 and no2 < 1130 or 365 < so2 and so2 < 800: 
	qldAr = "Muito Ruim"
else:
	qldAr = "Pessima" 

# Saída de dados - Informações sobre a classificação do ar e as implicações a saúde
if qldAr == "Bom": 
	print("\nQualidade do ar:", qldAr, "\nImplicacoes a saude: Nenhuma")
elif qldAr == "Moderada": 
	print("\nQualidade do ar:", qldAr, "\nImplicacoes a saude: Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar sintomas como tosse seca e cansaço. A população, em geral, não é afetada.")
elif qldAr == "Ruim": 
	print("\nQualidade do ar:", qldAr, "\nImplicacoes a saude: Toda a população pode apresentar sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta. Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar efeitos mais sérios na saúde.")
elif qldAr == "Muito Ruim":
 	print("\nQualidade do ar:", qldAr, "\nImplicacoes a saude: Toda a população pode apresentar sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta e ainda falta de ar e respiração ofegante. Efeitos mais graves à saúde de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas).")
else: 
	print("\nQualidade do ar:", qldAr, "\nImplicacoes a saude: Toda a população pode apresentar sérios riscos de manifestações de doenças respiratórias e cardiovasculares. Aumento de mortes prematuras em pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas).")
