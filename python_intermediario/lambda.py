# lista = [1, 3, 45, 12, 64, 3, 65, 1, 4, 9, 65]
# lista.sort()

# print(lista)
lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]


def ordena(item):
    return item['nome']


l1 = sorted(lista, key=lambda item: item['nome'])
for item in l1:
    print(item)
