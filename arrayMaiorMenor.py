l = []
#menor = 9999999999999
#maior = -1

#popular estrutura
for x in range(5):
    l.append(int(input("Digite um valor inteiro: ")))
print(l)

"""
for x in range(len(l)):
    if(l[x]>=maior):
        maior = l[x]

    if(l[x]< menor):
        menor = l[x]

print(l)
print(menor)
print(maior)
"""
print(l)
print(min(l))
print(max(l))


