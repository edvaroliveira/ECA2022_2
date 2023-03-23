l=[]
for x in range(5):
    valor = int(input("Digite um valor: "))
    l.append(valor)
valorProcurado = int(input("Digite um valor a ser procurado: "))
if valorProcurado in l:
    print(f" O valor {valorProcurado} está na posição {l.index(valorProcurado)} do vetor.")