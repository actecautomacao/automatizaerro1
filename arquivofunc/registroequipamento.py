from registroindices import connect2


def connect1():

    codigoequipamento = str(input('Informe codigo do equipamento 4 digitos para proceguir:   '))
    while True:
        try:
            if len(codigoequipamento) != 4:
                print('Codido Invalido')
                break
            elif len(codigoequipamento) == 4:
                print('Equipamento registrado com sucesso')
                print(codigoequipamento)
                connect2()  # chamada da função dentro do arquivo registro de indices (registroindices.py)
        except ValueError:
            print('Valor invalido')

