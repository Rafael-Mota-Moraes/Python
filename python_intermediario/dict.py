pessoa = {
    'nome': 'Rafael',
    'sobrenome': 'Moreira',
    'idade': 18,
    'altura': 1.65,
    'enderecos': [
        {'rua': 'tal tal', 'numero': 123},
        {'rua': 'outra rya', 'numero': 321},
    ],
}

print(type(pessoa))
# print(pessoa)

pessoa2 = dict(nome='Rafael', sobrenome='Moreira')
# print(pessoa2)

for chave in pessoa:
    print(chave, pessoa[chave])
