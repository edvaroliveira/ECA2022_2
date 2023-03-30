l = []
#menor = 9999999999999
#maior = -1
soma = 0
par = 0
impar = 0

#popular estrutura
for x in range(5):
    l.append(int(input("Digite um valor inteiro: ")))
print(l)

"""
for x in range(len(l)):
    soma += l[x]
    if l[x] % 2 == 0 and l[x] != 0:
        par+=1
    elif l[x] % 2 != 0 and l[x] != 0:
        impar+=1    
    
    if(l[x]>=maior):
        maior = l[x]

    if(l[x]< menor):
        menor = l[x]

print(l)
print(menor)
print(maior)
print(soma)
print(par)
print(impar)
"""
print(l)
print(min(l))
print(max(l))
print(sum(l))
print(par)
print(impar)



