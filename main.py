from datetime import datetime

print('\n======================================================================\nRelatorio de trabalho\n======================================================================\n')
now = datetime.now().strftime("%d/%m/%Y ")

print(f"Current time: {now}") 

while True: 
    try:
        
        print("Relatorio pre concluido informe as operações\n")

        cliente = input("Nome do cliente:\n")
        equipamento = input("Equipamento usado;\n")
        procedencia = input("Digite a procedencia;\n") 
        data = input("Digite a data:\n")
        tecnico = print(">>>>>>>>>>>>>>>>.\n")

        recebido = ['CLIENTE',cliente, 'EQUIUPAMENTO', equipamento, 'PROCEDENCIA', procedencia, 'DATA:',data,'FIM...',tecnico]

        per = input("Finalizar o programa? 1( sim )salva o arquivo ou  2( Nâo ) não salva o arquivo\n")

        if per == '1':
            print('Ok finalizando programa')
            with open('recebido.txt','a')as arquivo:
                for lista in recebido:
                    arquivo.write(str(lista) + '\n')
            
            break

        else:
            print('Ok finalizando programa\nNenhuma informação foi salva no arquivo')
            break       

    except:
        print('\n========================     Erro!    ================================')
        print('Algo deu errado verifique se esta informando as resposta corretamente!\n ') 