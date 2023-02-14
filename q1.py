# Questão 1 -  vetor
# tamanho = 2 # especifico o tamanho do vetor para usar em todos
# v1 = [0] * tamanho
# v2 = [0] * tamanho
# s = [0] * tamanho
# #populo o vetor 1
# for x in range(len(v1)):
#     v1[x] = int(input('Digite um valor para o vetor 1: '))
# #populo o vetor 2
# for x in range(len(v2)):
#     v2[x] = int(input('Digite um valor para o vetor 2: '))
# #aplico a soma das posições de mesmo índice
# for x in range(len(s)):
#     s[x] = v1[x] + v2[x]
# #mostro o resultado
# print(s)

# Questão 1 - Matriz
# tamanho = 2
# l1 = [0] * tamanho
# l2 = [0] * tamanho
# l3 = [0] * tamanho
# soma = [0] * tamanho
# # construo a matriz a partir do append de 3 listas
# matriz = list([l1, l2, l3]) #podemos construir na mão tb
# # populo a matriz
# for i in range(len(matriz)):
#     for j in range(len(matriz[0])):
#         matriz[i][j] = int(input('Digite um valor para a matriz: '))
# # realizo a soma das linhas e armazeno em um vetor
# for i in range(len(matriz[0])):
#     soma[i] = matriz[0][i]+matriz[1][i]+matriz[2][i]
#
# print(matriz)
# print(soma)

# Questão 2 - contagem da letra B
# while True:
#     palavra = input("Digite uma palavra: ")
#     if palavra.count('b') >= 2: #aqui verifico se tem no mínimo duas letras B
#         break

# Questão 2 - das vogais de forma pythonica
# while True:
#     palavra = input("Digite uma palavra: ")
#     contador = palavra.count('a') + palavra.count('e') + palavra.count('i') + palavra.count('o') + palavra.count('u')
#     if contador >= 3:
#         break

# Questão 2 - Vogais de forma braçal
# cont=0
# while True:
#     palavra = input("Digite uma palavra: ")
#     for x in palavra:
#         if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
#             cont+=1
#     if cont >= 3:
#         break
