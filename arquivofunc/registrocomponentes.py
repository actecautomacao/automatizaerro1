from registroman import gravaman

componentes = []
componentestemp = []


def connect3():

    while True:

        registcomponet = str(input('Informe o componente de manutenção para proceguir:  '))
        if len(registcomponet) != 6:
            print('indice Invalida')
            break
        else:
            print(registcomponet)
            confirm1 = int(input('Confirme operação (3) / (4) Finaliza Indices: '))
            if confirm1 != 3 and confirm1 != 4:
                print('Opção Invalida')
                break
            elif confirm1 == 3:
                componentestemp.append(registcomponet[:])
                componentes.append(componentestemp[:])
                componentestemp.clear()
                print(f'O indices registrado foi {componentes[:]}')
                resp = int(input('(0) para finalizar / (1) para continual'))
                if resp == 1:
                    continue
                elif resp == 0:
                    print('Indices Finalizados: ')
                    gravaman()
                elif confirm1 == 4:
                    print(f'Os indices registrados foram {componentes[:]}')
                    print('Indices finalizados')
