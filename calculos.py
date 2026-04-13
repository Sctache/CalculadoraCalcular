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

    return numero_final
