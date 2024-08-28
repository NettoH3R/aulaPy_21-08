
try: 
    n = int(input("Digite a quantidade de notas a serem adicionadas na primeira lista: "))
    m = int(input("Digite a quantidade de notas a serem adicionadas na segunda lista: "))

    p1 = [float(input(f"Digite o {i}º numero:")) for i in range(1,n+1)]
    p2 = [float(input(f"Digite o {i}º numero:")) for i in range(1,m+1)]

    media_P1 = sum(p1) / len(p1)
    media_P2 = sum(p2) / len(p2)


    print(f"Média da turma na prova 1: {media_P1:.2f}")
    print(f"Média da turma na prova 2: {media_P2:.2f}")


    if media_P1 > media_P2:
        print("A turma obteve a melhor média na prova 1.")
    else:
        print("A turma obteve a melhor média na prova 2.")

except:
    print("Valor incorreto digitado")