import calculos as cl

lista_numeros = []
resultado = float(0)

while True:

    #Criar comando para que o código puxe o resultado encontrado anteriormente
    if resultado != 0:
        apagar_resultado = input(f'Você deseja que o resultado {resultado} seja apagado?\nSim/Não\n')

        if apagar_resultado.lower() == 'sim':
            lista_numeros.clear()
            #Criar um input no qual o usuário sinalize qual operação deseje realizar (1 por vez)   
            operacao = input('(+, -, x, /)\nDigite a operação que você deseja realizar (1 por vez):')
            while True:
                numeros_individuo = str(input('Quando finalizar, basta digitar "."\nDigite 1 número por vez NA ORDEM que você deseja para realizar a operação:'))
                if numeros_individuo == '.':
                    break
                numeros_individuo = float(numeros_individuo)
                lista_numeros.append(numeros_individuo)
                print(lista_numeros)
            #Ativar a função de processos (operações):
            resultado = float(cl.processos(operacao, lista_numeros))
            print(resultado)

        elif apagar_resultado.lower() == 'não' or 'nao':
            lista_numeros.clear()
            lista_numeros.append(resultado)
            operacao = input('(+, -, x, /)\nDigite a operação que você deseja realizar (1 por vez):')
            while True:
                numeros_individuo = str(input('Quando finalizar, basta digitar "."\nDigite 1 número por vez NA ORDEM que você deseja para realizar a operação:'))
                if numeros_individuo == '.':
                    break
                numeros_individuo = float(numeros_individuo)
                lista_numeros.append(numeros_individuo)
                print(lista_numeros)
            #Ativar a função de processos (operações):
            resultado = float(cl.processos(operacao, lista_numeros))
            print(resultado)
    
    if resultado == 0:
        #Criar um input no qual o usuário sinalize qual operação deseje realizar (1 por vez)   
        operacao = input('(+, -, x, /)\nDigite a operação que você deseja realizar (1 por vez):')
        while True:
            numeros_individuo = str(input('Quando finalizar, basta digitar "."\nDigite 1 número por vez NA ORDEM que você deseja para realizar a operação:'))
            if numeros_individuo == '.':
                break
            numeros_individuo = float(numeros_individuo)
            lista_numeros.append(numeros_individuo)
            print(lista_numeros)
        #Ativar a função de processos (operações):
        resultado = float(cl.processos(operacao, lista_numeros))
        print(resultado)
