try:
    n = int(input("Digite a quantidade de números a serem adicionadas na primeira lista: "))
    m = int(input("Digite a quantidade de números a serem adicionadas na segunda lista: "))

    l1 = [int(input(f"Digite o {i}º número:")) for i in range(1,n+1)]
    l2 = [int(input(f"Digite o {i}º número:")) for i in range(1,m+1)]

    l3 = l1 + l2

    l3.sort()

    print(l3)

except:
    print("Valor incorreto digitado")