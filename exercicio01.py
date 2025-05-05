def somas_pares (lista):
    total = 0
    for i in lista:
        if i % 2 == 0:
            total += i
    return total

numeros = [1, 2, 3, 4, 5, 6]

print(somas_pares(numeros))


