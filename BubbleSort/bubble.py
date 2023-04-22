lista = [7, 5, 1, 8, 3]
n = len(lista)
for j in range(n - 1):
    for i in range(n-1):
        if lista[i] > lista[i + 1]:
            # Troca de elementos nas posições i e i +1
            lista[i], lista[i+1] = lista[i + 1], lista[i]
print(lista)
