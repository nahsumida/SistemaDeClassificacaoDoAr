import cx_Oracle
 
mp10 = mp25 = o3 = co = no2 = so2 = -1

connection = cx_Oracle.connect(
    user="SYSTEM",
    password="projeto",#pw,
    dsn="localhost/xe")

print("Successfully connected to Oracle Database")

cur = connection.cursor()
    
sqlSelect= 'select avg(mp10), avg(mp25), avg(o3), avg(co), avg(no2), avg(so2) from amostras'
cur.execute(sqlSelect)

column_names = [desc[0] for desc in cur.description]
   
print(column_names)

rows = cur.fetchall()

for row in rows:
    mp10=row[0]
    mp25=row[1]
    o3=row[2]
    co=row[3]
    no2=row[4]
    so2=row[5]

    print(row)
    print("media mp10", mp10)
    print("\nmedia mp25", mp25)
    print("\nmedia o3", o3)
    print("\nmedia co", co)
    print("\nmedia so2", so2)

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
elif qldAr == "Moderado": 
	print("\nQualidade do ar:", qldAr, "\nImplicacoes a saude: Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar sintomas como tosse seca e cansaço. A população, em geral, não é afetada.")
elif qldAr == "Ruim": 
	print("\nQualidade do ar:", qldAr, "\nImplicacoes a saude: Toda a população pode apresentar sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta. Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar efeitos mais sérios na saúde.")
elif qldAr == "Muito Ruim":
 	print("\nQualidade do ar:", qldAr, "\nImplicacoes a saude: Toda a população pode apresentar sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta e ainda falta de ar e respiração ofegante. Efeitos mais graves à saúde de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas).")
else: 
	print("\nQualidade do ar:", qldAr, "\nImplicacoes a saude: Toda a população pode apresentar sérios riscos de manifestações de doenças respiratórias e cardiovasculares. Aumento de mortes prematuras em pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas).")


'''
comandos no banco:
CREATE SEQUENCE ID_SEQ START WITH 001 INCREMENT BY 1 MAXVALUE 9999 NOCYCLE NOCACHE

CREATE TABLE AMOSTRAS (
     ID NUMBER NOT NULL,
     MP10 NUMBER NOT NULL,
     MP25 NUMBER NOT NULL,
     O3 NUMBER NOT NULL,
     CO NUMBER NOT NULL,
     NO2 NUMBER NOT NULL, 
     SO2 NUMBER NOT NULL,
     CONSTRAINT pk_id PRIMARY KEY (ID)
);

INSERT INTO AMOSTRAS VALUES(ID_SEQ.NEXTVAL, 10, 10, 10, 10, 10,10)
'''
