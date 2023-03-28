mp10 = -1
while mp10 < 0: 
	mp10 = float(input("Digite a quantidade de particulas inalaveis: "))
mp2.5 = -1
while mp2.5 < 0: 
	mp2.5 = float(input("Digite a quantidade de particulas inalaveis finas: "))
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

if qldAr == "Bom": 
	print("Qualidade do ar:", qldAr, "\nImplicacoes a saude: Nenhuma"
elif qldAr == "Moderada": 
	print("Qualidade do ar:", qldAr, "\nImplicacoes a saude: Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar sintomas como tosse seca e cansaço. A população, em geral, não é afetada.")
elif qldAr == "Ruim": 
	print("Qualidade do ar:", qldAr, "\nImplicacoes a saude: Toda a população pode apresentar sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta. Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar efeitos mais sérios na saúde.")
elif qldAr == "Muito Ruim":
 	print("Qualidade do ar:", qldAr, "\nImplicacoes a saude: Toda a população pode apresentar sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta e ainda falta de ar e respiração ofegante. Efeitos mais graves à saúde de grupos sensíveis.")
else: 
	print("Qualidade do ar:", qldAr, "\nImplicacoes a saude: Toda a população pode apresentar sérios riscos de manifestações de doenças respiratórias e cardiovasculares. Aumento de mortes prematuras em pessoas de grupos sensíveis."
