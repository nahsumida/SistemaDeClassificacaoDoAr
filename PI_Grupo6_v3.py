import cx_Oracle

def conexao():
    pw = ""
    while pw != "Ahftk7":
        pw = input("Digite a senha do banco de dados para acessar o sistema: ")

    connection = cx_Oracle.connect(
        user="bd2402231104",
        password=pw,
        dsn="172.16.12.14/xe")

    print('\t'*3, "\nSuccessfully connected to Oracle Database")
    return (connection)

def leitura(prompt, msgerro='Erro: Digite numero ', tipo = 'int'):
    while True:
        try: 
            var = int(input(prompt)) if tipo =='int' else float(input(prompt))
            return var
        except ValueError:
            print(msgerro + tipo)

def addAmostra(connection):
    cur = connection.cursor()

    mp10 = mp25 = o3 = co = no2 = so2 = -1

    while mp10 < 0: 
        mp10 = leitura("Digite a quantidade de particulas inaláveis: ",tipo='float')
    while mp25 < 0: 
        mp25 = leitura("Digite a quantidade de particulas inaláveis finas: ", tipo='float')
    while o3 < 0: 
        o3 = leitura("Digite o nível de ozônio: ", tipo='float')
    while co < 0: 
        co = leitura("Digite o nível de monóxido de carbono: ", tipo='float')
    while no2 < 0: 
        no2 = leitura("Digite o nível de dióxido de nitrogênio: ", tipo='float')
    while so2 < 0: 
        so2 = leitura("Digite o nível de dióxido de enxofre: ", tipo='float')
            
    sqlInsert= "INSERT INTO AMOSTRAS VALUES(ID_SEQ.NEXTVAL, {}, {}, {}, {}, {}, {})".format(mp10, mp25, o3, co, no2, so2)
    cur.execute(sqlInsert)
    con.commit()


    exibirTab(connection)
    return ('\t\t\t\nAdicionado com sucesso, Voltando Ao Menu')

def altAmostra(connection, id, str, val):
    id = int(id)
    str = str
    val = float(val)

    cur = connection.cursor()

    sqlUpdate = "update AMOSTRAS set {}={} where id={}".format( str, val,id)
    cur.execute(sqlUpdate)
    con.commit()
    
    return 

def menuAlt(connection):
    exibirTab(connection)
    cur = connection.cursor()
    mp10 = mp25 = o3 = co = no2 = so2 = -1

    id = leitura("\nDigite a o id da amostra que deseja alterar: ")
    #criar verificação para ver se existe no banco
    sqlSelect= "Select mp10, mp25, o3, co, no2, so2 from AMOSTRAS where id={}".format(id)
    cur.execute(sqlSelect)
    
    rows = cur.fetchall()

    for row in rows:
        mp10=row[0]
        mp25=row[1]
        o3=row[2]
        co=row[3]
        no2=row[4]
        so2=row[5]
        #print(row)    
    
    while True:
        print()
        print('*'*75)
        print(f'{"Alterar":^90}')
        print()
        print(f'{"[1]":^12} . {"[2]":^12} . {"[3]":^12} . {"[4]":^12} . {"[5]":^12} . {"[6]":^12}')
        print(f'{"MP 10":^12} | {"MP 2.5":^12} | {"O3":^12} | {"CO":^12} | {"NO2":^12} | {"SO2":^12}')
        print('{0:^12} | {1:^12} | {2:^12} | {3:^12} | {4:^12} | {5:^12}'.format(mp10,mp25,o3,co,no2,so2))
        print()
        alteracao = leitura("\n" "Digite o índice do valor que deseja alterar ou 0 para sair: ")
        novovalor = -1
        print()
        if alteracao == 1:
            str = "mp10"
            print("\t\t" "Alterar o valor de MP 10")
            print("\t\t" " > Valor atual: ",mp10)
            while True:
                    novovalor = leitura("\t\t" " > Digite o novo valor: ", tipo='float')
                    if novovalor < 0:
                        print("\t\t" ">> Valor inválido!")
                    else:
                        conf = confirmacao()
                        antigovalor = mp10
                        if conf == True:
                            mp10 = novovalor
                            altAmostra(connection, id, str, mp10)
                            print("\n\t\t" "Valor alterado!")
                        else:
                            mp10 = antigovalor
                            print("\n\t\t > O valor NÃO foi alterado.")
                        break
        if alteracao == 2:
            str = "mp25"
            print("\t\t" "Alterar o valor de MP 2.5")
            print("\t\t" " > Valor atual: ",mp25)
            while True:
                novovalor = leitura("\t\t" " > Digite o novo valor: ",  tipo='float')
                if novovalor < 0:
                    print("\t\t" ">> Valor inválido!")
                else:
                    conf = confirmacao()
                    antigovalor = mp25
                    if conf == True:
                        mp25 = novovalor
                        altAmostra(connection, id, str, mp25)
                        print("\n\t\t" "Valor alterado!")
                    else:
                        mp25 = antigovalor
                        print("\n\t\t > O valor NÃO foi alterado.")
                    break
        if alteracao == 3:
            str = "o3"
            print("\t\t" "Alterar o valor de O3")
            print("\t\t" " > Valor atual: ",o3)
            while True:
                novovalor = leitura("\t\t" " > Digite o novo valor: ",  tipo='float')
                if novovalor < 0:
                    print("\t\t" ">> Valor inválido!")
                else:
                    conf = confirmacao()
                    antigovalor = o3
                    if conf == True:
                        o3 = novovalor
                        altAmostra(connection, id, str, o3)
                        print("\n\t\t" "Valor alterado!")
                    else:
                        o3 = antigovalor
                        print("\n\t\t\n > O valor NÃO foi alterado.")
                    break
        if alteracao == 4:
            str = "co"
            print("\t\t" "Alterar o valor de CO")
            print("\t\t" " > Valor atual: ",co)
            while True:
                novovalor = leitura("\t\t" " > Digite o novo valor: ",  tipo='float')
                if novovalor < 0:
                    print("\t\t" ">> Valor inválido!")
                else:
                    conf = confirmacao()
                    antigovalor = co
                    if conf == True:
                        co = novovalor
                        altAmostra(connection, id, str, co)
                        print("\n\t\t" "Valor alterado!")
                    else:
                        co = antigovalor
                        print("\n\t\t > O valor NÃO foi alterado.")
                    break
        if alteracao == 5:
            str = "no2"
            print("\t\t" "Alterar o valor de NO2")
            print("\t\t" " > Valor atual: ",no2)
            while True:
                novovalor = leitura("\t\t" " > Digite o novo valor: ", tipo='float')
                if novovalor < 0:
                    print("\t\t" ">> Valor inválido!")
                else:
                    conf = confirmacao()
                    antigovalor = no2
                    if conf == True:
                        no2 = novovalor
                        altAmostra(connection, id, str, no2)
                        print("\n\t\t" "Valor alterado!")
                    else:
                        no2 = antigovalor
                        print("\n\t\t > O valor NÃO foi alterado.")
                    break
        if alteracao == 6:
            str = "so2"
            print("\t\t" "Alterar o valor de SO2")
            print("\t\t" " > Valor atual: ",so2)
            while True:
                novovalor = leitura("\t\t" " > Digite o novo valor: ", tipo='float')
                if novovalor < 0:
                    print("\t\t" ">> Valor inválido!")
                else:
                    conf = confirmacao()
                    antigovalor = so2
                    if conf == True:
                        so2 = novovalor
                        altAmostra(connection, id, str, so2)
                        print("\n\t\t > Valor alterado!")
                    else:
                        so2 = antigovalor
                        print("\n\t\t > O valor NÃO foi alterado.")
                    break
        if alteracao == 0:
            print("Saindo do menu de alterações...")
            break 
        if alteracao < 0 or alteracao > 6:
            print(f'{"Digite um índice válido!":^80}')

    return  ('\t\t\t\nAlterado com sucesso, Voltando Ao Menu')
    
def exibirTab(connection):
    cur = connection.cursor()

    sqlSelect= 'select id, mp10, mp25, o3, co, no2, so2 from amostras'
    cur.execute(sqlSelect)
        
    #column_names = [desc[0] for desc in cur.description]
    #print(column_names)

    rows = cur.fetchall()

    print(f'\n{"ID":^12} | {"MP 10":^12} | {"MP 2.5":^12} | {"O3":^12} | {"CO":^12} | {"NO2":^12} | {"SO2":^12}')
    for i in rows: 
        #print(i)
        #for i in row:
        id = i[0]
        mp10=i[1]
        mp25=i[2]
        o3=i[3]
        co=i[4]
        no2=i[5]
        so2=i[6]
        print('{0:^12} | {1:^12} | {2:^12} | {3:^12} | {4:^12} | {5:^12} | {6:^12}'.format(id,mp10,mp25,o3,co,no2,so2))

    return  

def delAmostra(connection):
    exibirTab(connection)
    cur = connection.cursor()

    id = leitura("\nDigite a o id da amostra que deseja excluir: ")

    sqlSelect= "delete from AMOSTRAS where id={}".format(id)
    opcao = confirmacao("excluir")
    if opcao == True:
        cur.execute(sqlSelect)
        return ('\t\t\t\nDeletado com sucesso, Voltando Ao Menu')
    else:
        return ('\t\t\t\nO item NÃO foi deletado, Voltando Ao Menu')
    
#return ('\t\t\t\nDeletado com sucesso, Voltando Ao Menu')

def classAmostra(connection):
    cur = connection.cursor()

    sqlSelect= 'select avg(mp10), avg(mp25), avg(o3), avg(co), avg(no2), avg(so2) from amostras'
    cur.execute(sqlSelect)

    #column_names = [desc[0] for desc in cur.description]
    
    #print(column_names)

    rows = cur.fetchall()

    for row in rows:
        mp10=row[0]
        mp25=row[1]
        o3=row[2]
        co=row[3]
        no2=row[4]
        so2=row[5]

        #print(row)
        print("Média mp10: ", mp10)
        print("\nMédia mp25: ", mp25)
        print("\nMédia o3: ", o3)
        print("\nMédia co: ", co)
        print("\nMédia so2: ", so2)

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
        print("\n\nQualidade do ar:", qldAr, "\n\nImplicacoes a saude: Nenhuma")
    elif qldAr == "Moderado": 
        print("\n\nQualidade do ar:", qldAr, "\n\nImplicacoes a saude: Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar sintomas como tosse seca e cansaço. A população, em geral, não é afetada.")
    elif qldAr == "Ruim": 
        print("\n\nQualidade do ar:", qldAr, "\n\nImplicacoes a saude: Toda a população pode apresentar sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta. Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar efeitos mais sérios na saúde.")
    elif qldAr == "Muito Ruim":
        print("\n\nQualidade do ar:", qldAr, "\n\nImplicacoes a saude: Toda a população pode apresentar sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta e ainda falta de ar e respiração ofegante. Efeitos mais graves à saúde de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas).")
    else: 
        print("\n\nQualidade do ar:", qldAr, "\n\nImplicacoes a saude: Toda a população pode apresentar sérios riscos de manifestações de doenças respiratórias e cardiovasculares. Aumento de mortes prematuras em pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas).")


    return ('\t\t\t\nClassificado com sucesso, Voltando Ao Menu')

#
def confirmacao(str = "alterar"):
	resp = ""
	if str == "alterar":
		str = "\n\t\tTem certeza que deseja alterar? (s/n): " 
	else:
		str = "\n\t\tTem certeza que deseja excluir? (s/n): "

	while resp != "s" or resp != "n":
		resp = input(str)
		if resp == "s":
			return True
		else:
			return False

#-------------INICIO SISTEMA----------------------

con = conexao()

menu = True
while menu == True:
    print('\n\n','='*75,'\n\n','\t'*4,'    MENU\n')
    print('\t'*3,' Sistema de Qualidade do Ar *\n')
    print('\t'*3,' [1]   ADICIONAR AMOSTRA')
    print('\t'*3,' [2]   ALTERAR AMOSTRA')
    print('\t'*3,' [3]   EXCLUIR AMOSTRA')
    print('\t'*3,' [4]   CLASSIFICAR AMOSTRA')
    print('\t'*3,' [5]   SAIR\n')

    while True:
        opcao=leitura('>> Digite a opção desejada: ')
        if opcao not in (1,2,3,4,5):
            print('Digite um valor válido.')
        else:
            if opcao == 1:
                print('\n\n','='*75,'\n\n','\t'*4,'    Adicionar\n')
                result = addAmostra(con)

                print(result)
            elif opcao == 2:
                print('\n\n','='*75,'\n\n','\t'*4,'    Alterar\n')
                result = menuAlt(con)
                con.commit()

                print(result)
            elif opcao == 3:
                print('\n\n','='*75,'\n\n','\t'*4,'    Excluir\n')
                result = delAmostra(con)
                con.commit()

                print(result)
            elif opcao == 4:
                print('\n\n','='*75,'\n\n','\t'*4,'    Classificar\n')
                result = classAmostra(con)
                con.commit()

                print(result)
            elif opcao == 5:
                print('\n\n','\t'*3,'Fechando programa...')
                print('\t'*3,'    Até Mais!!!\n')

                menu = False
            break
