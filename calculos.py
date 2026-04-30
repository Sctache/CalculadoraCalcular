#Operações utilizando Funções
def processos (parametro_operacao, lista):
    if parametro_operacao == '+':
        numero_final = sum(lista)

    elif parametro_operacao == '-':
        x = lista[0]
        for i in lista[1:]:
            subtraindo = x - i
            x = subtraindo
        numero_final = x

    elif parametro_operacao == 'x':
        y = lista[0]
        for i in lista[1:]:
            multiplicando = y * i
            y = multiplicando
        numero_final = y

    elif parametro_operacao == '/':
        #pensando na lista vazia.
        if lista == []:
            divisor = float(input('Digite o Divisor:\n'))
            dividendo = float(input('Digite o Dividendo:\n'))
            numero_final = dividendo / divisor 
        #caso já tenha um número.
        elif lista != []:
            pergunta_dividendo = input('Deseja que o número anterior seja o Dividendo? (sim ou não)\n')
            if pergunta_dividendo.strip().lower() == 'sim':
                divisor = float(input('Digite o Divisor:\n'))
                numero_final = lista[0] / divisor
            
            elif pergunta_dividendo.strip().lower() == 'não' or 'nao':
                print('Número anterior identificado como Divisor da Operação seguinte!')
                dividendo = float(input('Digite o Dividendo:\n'))
                numero_final = dividendo / lista[0]

    return numero_final
