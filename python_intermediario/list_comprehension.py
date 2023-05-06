# print(list(range(10)))
lista = []

for numero in range(10):
    lista.append(numero)

# print(lista)
lista = [numero for numero in range(10)]
# print(lista)

# Mapeamento de dados em list comprehension

produtos = [
    {'nome': 'p1', 'preco': 20},
    {'nome': 'p2', 'preco': 10},
    {'nome': 'p3', 'preco': 30},
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.5}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]

print(*novos_produtos, sep='\n')

# mais de um for

lista = []
# for x in range(3):
#     for y in range(3):
#         lista.append((x, y))
# print(lista)

lista = [
    (x, y)
    for x in range(3)
    for y in range(3)
]

print(lista)
