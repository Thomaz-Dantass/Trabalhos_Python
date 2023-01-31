nomes= []
telefones =[]
operacao =0

while operacao != 8 or operacao > 8 :
    print ("\nAgenda Telefonica\n\n1-listar contatos\n2-Inserir contato\n3-Alterar contato\n4-Buscar contato\n5-Remover contato\n6-Salvar em arquivo de texto\n7-Gerar HTML\n8-Sair")
    operacao=int(input("sua escolha:\n"))

    if operacao == 2:
        n = input("digite o nome do seu contato:\n")
        numero = int(input("digite o numero do seu contato:"))
        nomes.append(n)
        telefones.append(numero)
        print("Contato salvo!\n")

    elif operacao == 1:
        print("\nlista de contatos!\n")
        for x in range (0,len(nomes)):
            print(nomes[x]," ====== ",telefones[x])

    elif operacao == 3:
        encontrado = False
        escolha = input("alterar o contato de:")
        for x in range(0,len(nomes)):
            if nomes[x] == escolha:
                encontrado = True
                n = str(input("digite o novo nome do seu contato:"))
                numero = int(input("digite o novo numero do seu contato:"))
                nomes[x]= n
                telefones[x]= numero
                print("\nContato alterado!\n")
        if not encontrado:
           print('\nContato não encontrado!\n')

    elif operacao == 4:
        encontrado = False
        escolha= str(input("Quem você deseja buscar? "))
        for x in range(0,len(nomes)):
            if nomes[x] == escolha:
                encontrado = True
                print(nomes[x],"=====",telefones[x])
        if not encontrado:
            print('Contato não encontrado!\n')

    elif operacao == 5:
            encontrado = False
            escolha = input("quem deseja remover? ")
            for x in range(0,len(nomes)):
                if nomes[x] == escolha:
                    encontrado = True
                    nomes.remove(escolha)
                    print("\nContato removido!")
            if not encontrado:
                print('Contato não encontrado!\n')
                
    elif operacao == 6:
        with open("agenda_telefonica.txt","w") as arquivo:
            arquivo.write("Lista telefonica!")
            for x in range(0,len(nomes)):
                arquivo.write("\n")
                arquivo.write(str(nomes[x]))
                arquivo.write("----")
                arquivo.write(str(telefones[x]))
                arquivo.write("\n")
        print("Gerado Arquivo de Texto!")
    elif operacao == 7:
        with open("agenda_telefonica.html","w") as arquivo:
            arquivo.write("<DOCTYPE!html>")
            arquivo.write("<html>")
            arquivo.write("<head>")
            arquivo.write("<title> listatelefonica </title>")
            arquivo.write("</head>")
            arquivo.write("<body>")
            arquivo.write("<table border = '1'>")
            
            for x in range(0,len(nomes)):
                arquivo.write("<tr>\n")
                arquivo.write("<td> \n")
                arquivo.write(str(nomes[x]))
                arquivo.write("----")
                arquivo.write(str(telefones[x]))
                arquivo.write("</td \n>")
            arquivo.write("\n")
            arquivo.write("</tr> \n")
            arquivo.write("</table> \n")
            arquivo.write("</html> \n")
            print("Gerado arquivo HTML!")
            
    elif operacao > 8:
        print("escolha uma das opções apresentadas!")