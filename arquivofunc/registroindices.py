from registrocomponentes import connect3

indices = []
indicestemp = []


def connect2():

    while True:

        registroindice = str(input('Informe o indice de manutenção para proceguir:  '))
        if len(registroindice) != 5:
            print('indice Invalida')

        else:
            print(registroindice)
            confirm1 = int(input('Confirme operação (3) / (4) Finaliza Indices: '))
            if confirm1 != 3 and confirm1 != 4:
                print('Opção Invalida')
                break
            elif confirm1 == 3:
                indicestemp.append(registroindice[:])
                indices.append(indicestemp[:])
                indicestemp.clear()
                print(f'O indices registrado foi {indices[:]}')
                resp = int(input('(0) para finalizar / (1) para continual'))
                if resp == 1:
                    continue
                elif resp == 0:
                    print('Indices Finalizados: ')
                    connect3()  # chamada da função dentro do arquivo registro de componentes
                    # (registrocomponentes.py)
                elif confirm1 == 4:
                    print(f'Os indices registrados foram {indices[:]}')
                    print('Indices finalizados')