

from registroequipamento import connect1


while True:
    userman = str(input('Informe usuario para processeguir: '))
    try:
        if len(userman) != 3:
            print('Usuario Invalido!')
        elif len(userman) == 3:
            print('Usuario registrado com sucesso')
            print(userman)
            connect1()  # chamada da função dentro do arquivo registro de equipamentos registroequipamentos.py
    except ValueError:
        print('Erro de valor')



