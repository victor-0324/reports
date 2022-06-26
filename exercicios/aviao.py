
""" ma aeronave de grande porte é tanto
       que a medição muda de eixo, sendo utilizado litros por quilômetros,

Para criação do algoritmo solicitado deverão ser considerados os seguintes dados para o calculo desejado, são eles:
    - Média da aeronave em litros por quilômetros
    - Capacidade máxima em litros do tanque
    - Quantidade de quilômetros do trecho planejado
    - Quantidade de quilômetros do trecho alternativo
    - Quantidade de combustível já na aeronave
    
O algoritmo deve conter as seguintes regras
    - Uma aeronave deve sempre ser abastecida considerando o trecho planejado + trecho alternativo,
     visto que se o aeroporto de destino estiver com problemas, uma rota alternativa deverá ser realizada.
    - Além do trecho total, uma margem de 30% de combustível deverá ser adicionada, para que qualquer
     emergência a aeronave esteja com uma quantidade segura de combustível.
    - Se o trecho total mais a margem de segurança, extrapolarem a capacidade máxima de combustível
     do tanque da aeronave, uma mensagem de alerta deve ser mostrada na tela, dizendo a seguinte mensagem
      “Voo Reprovado, reveja seu planejamento.”. Caso contrário mostrar "Voo Aprovado, bom voo!"
    - Se o tanque suportar o trecho total mais a margem de segurança o algoritmo deverá mostrar na tela o valor
     do trecho principal, trecho alternativo, total do trecho com a margem de segurança, quantidade de combustível
      necessária para o trecho e quantidade necessária de abastecimento.
    - Use sub-rotinas para isolar as lógicas do algoritmo

Sequencia lógica do algoritmo
    - Leitura dos dados
    - Somar trecho planejado + trecho alternativo
    - Adicionar margem de segurança
    - Calcular a quantidade de combustível
    - Verificar se a quantidade de combustível comporta na aeronave
    - Verificar o quanto de combustível será necessário para abastecimento.
    - Mostrar resultados.
"""
def trajeto_total(km_auternativo: float, planejado_alternativo: float):
        planejado_alternativo = km_trajeto + km_auternativo
        trajeto_total = planejado_alternativo + (planejado_alternativo * 30/100)
        return trajeto_total

litros_quilometro = float(input('Quantos litros por quilometro aeronave faz:  '))
litros_tanque = float(input('Capacidade máxima em litros do tanque;  '))
litros_abordo = float(input('Quantidade de combustível já na aeronave; '))

km_trajeto = float(input('Quantos kilometros para chegar ao trecho planejado; '))
km_auternativo = float(input('Quantos kilometros para um trecho alternativo ;  '))
total = trajeto_total(km_auternativo, km_trajeto)
quilometro = litros_quilometro * total
trecho = km_trajeto + km_auternativo
conbustivel_necessario = trecho * litros_quilometro

if quilometro >= litros_tanque:
        print('Voo Reprovado, reveja seu planejamento\n')
        print(f'Trecho principal {km_trajeto}Km\n')
        print(f'Trecho alternativo {km_auternativo}Km\n')
        print(f'Total do trecho com a margem de segurança {total}Km\n')
        print(f'Quantidade de combustível necessária para o trecho {conbustivel_necessario} Litros\n')
        print(f'Combustivel necesario para abastecimento e {quilometro} Litros\n')
        print(f'Sua aeronave suporta a penas {litros_tanque} Litros\n')

else:
        print('Voo Aprovado, bom voo!\n')
        print(f'Trecho principal {km_trajeto}Km\n')
        print(f'Trecho alternativo {km_auternativo}Km\n')
        print(f'Total do trecho com a margem de segurança {total}Km\n')
        abasteca =  conbustivel_necessario - litros_abordo
        print(f'Quantidade de combustível necessária para o trecho {conbustivel_necessario} Litros\n')
        print(f'Combustivel necesario para abastecimento e {abasteca} Litros\n')