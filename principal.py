import calculos as cl

#Criar um input no qual o usuário sinalize qual operação deseje realizar (1 por vez)

operacao = input('(+, -, x, /)\nDigite a operação que você deseja realizar (1 por vez):')

"Criar um input no qual o usuário possa escrever quantos números quiser."

lista_numeros = []

while True:
    numeros_individuo = str(input('Quando finalizar, basta digitar "."\nDigite 1 número por vez que você deseja para realizar a operação:'))
    if numeros_individuo == '.':
        break
    numeros_individuo = float(numeros_individuo)
    lista_numeros.append(numeros_individuo)
print(lista_numeros)

#Ativar a função de processos (operações):
cl.processos(operacao, lista_numeros)
