lista = []

with open('tdd.txt', 'r') as file:
    for token in file:
        lista.append(token)

print(lista)