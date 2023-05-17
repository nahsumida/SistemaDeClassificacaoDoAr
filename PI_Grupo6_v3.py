import cx_Oracle

def conexao(pw):
    pw = str(pw)
    connection = cx_Oracle.connect(
        user="SYSTEM",
        password="projeto",#pw,
        dsn="localhost/xe")

    print('\t'*3, "\nSuccessfully connected to Oracle Database")
    return (connection)

def addAmostra(connection):
    cur = connection.cursor()

    mp10 = mp25 = o3 = co = no2 = so2 = -1

    while mp10 < 0: 
        mp10 = float(input("Digite a quantidade de particulas inaláveis: "))
    while mp25 < 0: 
        mp25 = float(input("Digite a quantidade de particulas inaláveis finas: "))
    while o3 < 0: 
        o3 = float(input("Digite o nível de ozônio: "))
    while co < 0: 
        co = float(input("Digite o nível de monóxido de carbono: "))
    while no2 < 0: 
        no2 = float(input("Digite o nível de dióxido de nitrogênio: "))
    while so2 < 0: 
        so2 = float(input("Digite o nível de dióxido de enxofre: "))
            
    sqlInsert= "INSERT INTO AMOSTRAS VALUES(ID_SEQ.NEXTVAL, {}, {}, {}, {}, {}, {})".format(mp10, mp25, o3, co, no2, so2)
    print(sqlInsert)
    cur.execute(sqlInsert)

    sqlSelect= 'select mp10, mp25, o3, co, no2, so2 from amostras'
    cur.execute(sqlSelect)
        
    column_names = [desc[0] for desc in cur.description]
    print(column_names)

    rows = cur.fetchall()

    for row in rows: 
        print(row)

    return ('\t'*3, "\nAdicionado com sucesso, Voltando Ao Menu")

def altAmostra(connection):
    cur = connection.cursor()

    return "alterado com sucesso"

def delAmostra(connection):
    cur = connection.cursor()

    return ('\t'*3,"\nDeletado com sucesso, Voltando Ao Menu")

def classAmostra(connection):
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


    return ('\t'*3, ",Classificado com sucesso, Voltando Ao Menu")

menu = True
while menu == True:
    con = conexao("")

    print('\n\n','='*75,'\n\n','\t'*4,'    MENU\n')
    print('\t'*3,' Sistema de Qualidade do Ar *\n')
    print('\t'*3,' [1]   ADICIONAR AMOSTRA')
    print('\t'*3,' [2]   ALTERAR AMOSTRA')
    print('\t'*3,' [3]   EXCLUIR AMOSTRA')
    print('\t'*3,' [4]   CLASSIFICAR AMOSTRA')
    print('\t'*3,' [5]   SAIR\n')

    while True:
        opcao= int(input('>> Digite a opção desejada: '))
        if opcao not in (1,2,3,4,5):
            print('Digite um valor válido.')
        else:
            if opcao == 1:
                print('\n\n','\t'*4,'   Adicionar\n')
                result = addAmostra(con)
                con.commit()

                print(result)
            elif opcao == 2:
                print('\n\n','\t'*4,'   Alterar\n')
                result = altAmostra(con)
                con.commit()

                print(result)
            elif opcao == 3:
                print('\n\n','\t'*4,'   Excluir\n')
                result = delAmostra(con)
                con.commit()

                print(result)
            elif opcao == 4:
                print('\n\n','\t'*4,'   Classificar\n')
                result = classAmostra(con)
                con.commit()

                print(result)
            elif opcao == 5:
                print('\n\n','\t'*3,'Fechando programa...')
                print('\t'*3,'    Até Mais!!!\n')

                menu = False
            break
