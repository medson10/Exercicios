def exercicio1():
    vetorS = ""
    vetor = raw_input('Digite 5 numeros: ').split()
    for x in vetor:
        vetorS += " " + str(x)
    print(vetorS)


exercicio1()
