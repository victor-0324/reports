"""
     Treinando a logica de programação 

    # tenho 42 gados
    Preciso separar os gados onde os gados numeros pares vão para o pasto numero 1 
    e gados com numeros inpas no pasto numero 2

    Regras:
1 - O algoritmo não poderá considerar que o usuário  irá repetir o número do gado na leitura
    ou seja não podera ter numero repitido .
2 - Os vetores devem armazenar os números de forma sequencial, 
    ou seja não poderá pular posições em seu armazenamento.
"""

pasto1 = []
pasto2 = []
print('Bem-vindo, esse programa vai separa os gados de acordo com a numeração\n')
numero_gado = int(input("Digite o tanto de gados da fazenda: "))  

while True:
    try:     
       
        gado = int(input('Digite a numeração do gado;\n'))
        if gado in pasto1 or gado in pasto2:
            print(f'\n=== O numero ({gado}) ja foi digitado antes ===\n')
            continue

        if gado > numero_gado:
            ver = input('A cabou a contagem? se sim digite 1 se não digite 2; ')
            if ver == '1':
                print(f'A contagem ficou assim\npasto1 {pasto1}\npasto2 {pasto2}')
                break
            elif ver == '2':
                print('Reiniciando')
                continue
            else:
                print('Se sim digite 1 se não digite 2')
        
        elif gado%2:
            print('\nO gado enformado (inpa) vai para o pasto numero 2')       
            pasto1.append(gado)
            pasto1.sort()
            for i in pasto1:
                print(i)
            i +- 1
            
        elif gado != gado%2:
            print('O gado enformado (pa) vai para o pasto numero 1')
            pasto2.append(gado)
            pasto2.sort()
            for i in pasto2:
                print(i)
            i +- 1

        else:
            print('Algo deu errado digite um numero valido !!')
    except:
        print('Algo deu errado !')
        break