from datetime import datetime

print('\n=======================================================\nRelatorio de trabalho\n=======================================================\n')
now = datetime.now().strftime(" %d/%m/%Y ")


while True: 
    try:
        
        print("Relatorio pre concluido informe as operações\n")
        print(f"Data: ==={now}===\n")
        
        cliente = input("Nome do cliente:\n")
        equipamento = input("Equipamento usado:\n")
        procedencia = input("Digite a procedencia:\n")     
        tecnico = ">>>>>>>>>>>>>>>>.\n"

        recebido = ['\nCLIENTE',cliente, '\nEQUIPAMENTO', equipamento, '\nPROCEDENCIA', procedencia, '\nDATA',now,'FIM...\n',tecnico]

        per = input("Finalizar o programa?\n1( sim )salva o arquivo\n===== ou =====\n2( Nâo ) não salva o arquivo\n")
       
        if per == '1':
            with open('report.txt','a')as arquivo:
                for lista in recebido:
                    arquivo.write(str(lista) + '\n')

                print('Ok finalizando programa arquivo salvo em (Report.txt)\n')
                break
        else:
            print('Ok finalizando programa ...\nNenhuma informação foi salva no arquivo')
            break       

    except:
        print('\n========================     Erro!    ================================')
        print('Algo deu errado verifique se esta informando as resposta corretamente!\n ') 