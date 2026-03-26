"Criar um input no qual o usuário possa escrever quantos números quiser."

lista_numeros = []

while True:
    numeros_individuo = str(input('Quando finalizar, basta digitar .\nDigite 1 número por vez que você deseja para realizar a operação:'))
    if numeros_individuo == '.':
        break
    numeros_individuo = float(numeros_individuo)
    lista_numeros.append(numeros_individuo)
print(lista_numeros)