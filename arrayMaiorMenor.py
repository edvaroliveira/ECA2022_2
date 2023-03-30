l = []
#menor = 9999999999999
#maior = -1
soma = 0

#popular estrutura
for x in range(5):
    l.append(int(input("Digite um valor inteiro: ")))
print(l)

"""
for x in range(len(l)):
    soma += l[x]
    if(l[x]>=maior):
        maior = l[x]

    if(l[x]< menor):
        menor = l[x]

print(l)
print(menor)
print(maior)
print(soma)
"""
print(l)
print(min(l))
print(max(l))
print(sum(l))


