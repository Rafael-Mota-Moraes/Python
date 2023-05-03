import copy


pessoa = {
    'nome': 'Rafael',
    'sobrenome': 'Moreira',
    'idade': 19
}

print(len(pessoa))
print(pessoa.__len__())
print(list(pessoa.keys()))

for chave, valor in pessoa.items():
    print(chave, valor)

pessoa.setdefault('idade', None)
print(pessoa['idade'])

# Shallow copy e deep copy

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [1, 2, 3]
}

# d2 = d1.copy()
d2 = copy.deepcopy(d1)
d2['c1'] = 100
d2['l1'][1] = 999
print(d1)
print(d2)

pessoa_2 = {
    'nome': 'Rafael',
    'sobrenome': 'Moreira'
}

print(pessoa_2.get('nome'))
print(pessoa_2.get('sobrenome'))
print(pessoa_2.get('idade', None))

ultima_chave = pessoa_2.popitem()
print(ultima_chave)
pessoa_2.update({
    'nome': 'novo valor',
    'idade': 30
})
print(pessoa_2)
